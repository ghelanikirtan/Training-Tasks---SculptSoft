FROM python:3.10-slim
COPY . /ETL
WORKDIR /ETL
COPY requirements.txt .
RUN piip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "scheduler.py"]
