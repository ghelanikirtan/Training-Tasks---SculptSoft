FROM python:3.10-slim
COPY . /ETL
WORKDIR /ETL
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "scheduler.py"]
