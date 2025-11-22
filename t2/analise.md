# ✅ **1. Estudo Técnico das Métricas do Relatório**

Seu ambiente está configurado com:

* **Replica set MongoDB com 3 membros**
* **READ_PREFERENCE = secondaryPreferred**
* **WRITE_CONCERN = 1**
* **CHAOS_FAILURE_CHANCE = 1.0** → falhas aleatórias o tempo todo
* App NodeJS com injeção de falhas internas
* Load test com 80% leituras, 20% escritas

Vamos analisar cada resultado.

---

## 📌 **1.1 Resultados de Performance**

### **Escritas (POST)**

| Métrica        | Valor               | Interpretação                                      |
| -------------- | ------------------- | -------------------------------------------------- |
| Total de Reqs  | 872                 | Poucas requisições de escrita, como esperado (20%) |
| Erros          | **150 erros (17%)** | Valor alto → problemas causados por falha no líder |
| Latência Média | 383ms               | Indicativo de espera por eleição de novo primário  |
| P95            | ~2004ms             | Muitas escritas demorando **~2 segundos**          |
| P99            | ~2006ms             | Tempo típico de *failover* no MongoDB              |

📌 **Conclusão**:
O comportamento é totalmente compatível com **replica set durante falhas constantes** →
quando o primário cai, o cluster fica **indisponível para escrita** entre 1,5 e 2,5 segundos.

---

### **Leituras (GET)**

| Métrica        | Valor   | Interpretação                       |
| -------------- | ------- | ----------------------------------- |
| Total          | 3366    | Muitas, por causa do READ_RATIO=0.8 |
| Erros          | 0       | Excelente → replicação suportou bem |
| Latência Média | 21ms    | Baixa, mesmo com falhas             |
| P95/P99        | 55–77ms | Alta estabilidade                   |

📌 **Conclusão:**
Como você usa **secondaryPreferred**, quando o primário cai **as leituras continuam**, pois o cliente pode continuar lendo dos secundários.

Esses números provam que:

✔ O sistema continua lendo mesmo com falhas
❌ Escritas sofrem com indisponibilidade temporária

---

## 📌 **1.2 Timeline de Disponibilidade**

O timeline mostra claramente:

* Momentos **🟩** = cluster estável
* Momentos **🟥/UNSTABLE** = falhas injetadas interrompem *writes*

### O padrão típico:

1. Sistema estável com baixa latência
2. Falha é injetada → primário cai → cluster leva ~2s para eleger um novo primário
3. Durante esse tempo:

   * *Writes* → falham ou atrasam muito
   * *Reads* → continuam funcionando
4. Nova eleição ocorre → estabilidade volta

Esse ciclo se repete porque **CHAOS_FAILURE_CHANCE = 1.0**.

### Exemplos claros no timeline:

* **5s–15s**: aumento brutal de latência e vários erros (🟥)
* Logo após, a estabilidade volta (17s, 18s)
* Outro período de instabilidade entre 19s–28s
* Mesmo padrão nos segundos 34–42

➡️ Isso é exatamente o comportamento esperado de um sistema distribuído **fortemente dependente de um líder**, como o MongoDB.

### Conclusão Geral da Timeline

* **Reads seguem funcionando quase sempre**
* **Writes falham durante failover**
* O sistema recupera autonomia rapidamente
* A latência explode nos momentos de eleição do primário
* O comportamento confirma um ambiente com **replicação real**, **falhas reais**, e **failover real**

---

# ✅ **2. Relacionando Métricas com as Perguntas do Trabalho**

Agora vou responder as questões (a), (b) e (c) usando evidências do relatório.
Você pode copiar e colar para o trabalho.

---

## 📌 **a) O que acontece se um dos servidores web ou do banco de dados falhar?**

### **Quando um servidor web (app Node) falha:**

* O app roda em **um único container**, então:

  * Se falhar → o sistema **inteiro cai**
  * O loadtester mostra períodos com “UNSTABLE” com **latências altíssimas** (ex: 489ms–1006ms)

📌 *Seu sistema atual não replica o servidor web.*

---

### **Quando um servidor de banco MongoDB falha:**

Como você tem **3 réplicas em replica set**, o comportamento é:

### ✔ Falha de um secundário

* **Leituras continuam** (READ_PREFERENCE = secondaryPreferred)
* Não há impacto perceptível
* Isso é confirmado pelos **zero erros em GET**

### ✔ Falha do primário

Aqui está o fenômeno mais importante:

* O cluster fica **temporariamente sem líder**
* Escritas não podem ser aplicadas
* Latência de escrita vai para **~2 segundos**
* Muitas escritas falham
* Após nova eleição, tudo volta ao normal

📌 Evidência:

* 150 erros de escrita
* P95/P99 = ~2000ms
* Picos UNSTABLE em múltiplos momentos

### ✔ Conclusão para a pergunta (a)

> Se um servidor web falhar, o sistema fica indisponível porque não há réplicas da aplicação.
> Se um servidor do banco (secundário) falhar, o sistema continua operando normalmente para leituras.
> Se o primário falhar, ocorre um período de indisponibilidade de escrita e aumento de latência até que um novo primário seja eleito (~2 segundos), mas as leituras continuam funcionando.

---

## 📌 **b) Quantas réplicas serão usadas? Como atualizar? Qual protocolo? Como impacta na solução?**

### ✔ Réplicas utilizadas:

* **3 réplicas MongoDB** (mongo1, mongo2, mongo3)
* Isso forma um **replica set** tolerante a falhas (1 falha tolerada)

### ✔ Atualização das réplicas (synchronization)

MongoDB replica set usa:

* **Protocolo Oplog → Asynchronous replication**
* Escritas vão **primeiro para o primário**,
* Secundários replicam lendo o `oplog.rs`

### ✔ Protocolo de atualização:

MongoDB uses **Raft-like election mechanics** (inspirado em Raft):

1. Cliente envia WRITE → primário recebe
2. Primário escreve no oplog
3. Secundários replicam
4. Em caso de falha do primário:

   * Eleição automática
   * Maioria do cluster elege novo primário

### ✔ Impactos na sua solução

1. **WRITE_CONCERN = 1**

   * Escritas são consideradas concluídas **antes de replicar para outros nós**
   * Isso melhora performance
   * Mas causa inconsistência temporária
   * E aumenta a chance de **perda de escrita** durante falhas (evidência: 150 erros)

2. **READ_PREFERENCE = secondaryPreferred**

   * Você lê dos secundários
   * Por isso os GET não falham no relatório
   * Mesmo durante failover do primário

3. **Impacto geral**

   * Leitura escalável e resiliente
   * Escrita vulnerável a falhas do primário
   * Replicação torna o sistema tolerante a até **1 falha simultânea**
   * Latência explode durante eleição (p95 = ~2 segundos)

---

## 📌 **c) Os servidores são stateful ou stateless? Como isso impacta?**

### ✔ MongoDB

É **stateful** → mantém dados locais
Impacto:

* Precisa de volumes persistentes
* Depende de replicação para consistência
* Falhas exigem eleição de primário
* Latência de failover aparece nas métricas (picos de 2 segundos)

### ✔ Servidor Web (Node)

É **stateless**
O serviço Node:

* Não guarda sessões
* Não armazena dados localmente
* Depende totalmente do MongoDB

Impacto:

* Fácil escalonar horizontalmente (você *poderia* replicar o app)
* Porém, **você atualmente roda apenas 1 instância**, então:

  * Se o container cair → a aplicação cai, mesmo que o banco continue funcionando

### ✔ Conclusão da (c)

> O banco de dados é stateful e exige replicação para garantir tolerância a falhas.
> A aplicação é stateless, permitindo escalabilidade horizontal, porém isso não está sendo explorado no momento — existe apenas uma réplica do app, tornando esse componente um ponto único de falha.
