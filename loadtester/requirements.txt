FROM python:3.11-slim
WORKDIR /test
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY loadtest.py .
CMD ["python", "loadtest.py"]
