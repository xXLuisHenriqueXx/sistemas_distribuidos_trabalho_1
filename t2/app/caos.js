import { exec } from "child_process";
import util from "util";
import mongoose from "mongoose";

const execPromise = util.promisify(exec);

const CHAOS_CHANCE = parseFloat(process.env.CHAOS_FAILURE_CHANCE || "0");
const KILL_LEADER = (process.env.CHAOS_KILL_LEADER || "false") === "true";
const CHECK_INTERVAL_MS = 5000;
const DOWNTIME_MS = 10000;

let isChaosRunning = false;

async function getTargetContainer() {
  if (KILL_LEADER) {
    try {
      if (mongoose.connection.readyState === 1) {
        const status = await mongoose.connection.db
          .admin()
          .command({ isMaster: 1 });
        if (status.primary) {
          const leader = status.primary.split(":")[0];
          console.log(
            `CHAOS INTELLIGENCE: Líder identificado como '${leader}'.`,
          );
          return leader;
        }
      }
      console.log(
        "CHAOS: Não foi possível identificar o líder (sem conexão?). Escolhendo aleatório...",
      );
    } catch (e) {
      console.error("CHAOS: Erro ao detectar líder:", e.message);
    }
  }

  const nodes = ["mongo1", "mongo2", "mongo3"];
  const target = nodes[Math.floor(Math.random() * nodes.length)];
  if (!KILL_LEADER)
    console.log(`CHAOS: Modo Aleatório. Alvo sorteado: '${target}'.`);
  return target;
}

async function triggerChaos() {
  if (isChaosRunning) return;
  isChaosRunning = true;

  const targetContainer = await getTargetContainer();

  console.log(`CHAOS MONKEY: Sorteio realizado! Alvo: ${targetContainer}`);

  try {
    await execPromise(`docker kill ${targetContainer}`);
    console.log(`CHAOS MONKEY: '${targetContainer}' MORTO (SIGKILL)!`);

    if (KILL_LEADER) {
      console.log("(Líder morto, uma nova eleição deve começar agora!)");
    }

    setTimeout(async () => {
      try {
        console.log(`CHAOS MONKEY: Revivendo '${targetContainer}'...`);
        await execPromise(`docker start ${targetContainer}`);
        console.log(`CHAOS MONKEY: '${targetContainer}' reiniciado.`);
      } catch (e) {
        console.error(`Erro ao reviver ${targetContainer}:`, e.message);
      } finally {
        isChaosRunning = false;
      }
    }, DOWNTIME_MS);
  } catch (err) {
    console.error("Falha ao executar comando Docker:", err.message);
    isChaosRunning = false;
  }
}

export function startChaosMonkey() {
  if (CHAOS_CHANCE <= 0) {
    console.log("Chaos Monkey desativado.");
    return;
  }

  console.log(`Chaos Monkey ATIVADO!`);
  console.log(`Chance: ${CHAOS_CHANCE * 100}% a cada 5s`);
  console.log(
    `Modo: ${KILL_LEADER ? "MATAR O LÍDER (Sempre força eleição)" : "ALEATÓRIO (Pode matar secundários)"}`,
  );

  setInterval(() => {
    if (!isChaosRunning) {
      const r = Math.random();
      if (r < CHAOS_CHANCE) {
        triggerChaos();
      }
    }
  }, CHECK_INTERVAL_MS);
}
