FROM python:3.9-slim

WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia script
COPY loadtest.py .

# Cria diretório para reports
RUN mkdir -p /app/reports

CMD ["python", "loadtest.py"]