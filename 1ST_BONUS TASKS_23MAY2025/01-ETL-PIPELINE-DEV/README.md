# TASK: Data Pipeline Development:

## Title: Build a Mini Ingestion and Processing Pipeline. [ETL]

- Build an entire ETL [Extract, Transform, and Load Pipeline]

Following Requirements Met:

- Used `careerjet_api_client` to fetch the job posting data. -> Builf an Extraction Pipeline.
- Used `pydantic` Validation Models to store the extracted data... (Eventually this was the basic Transformation Library).
- Used `sqlalchemy` to LOAD the data into the database (Right now using local sqlite database).
- Implemented proper `logging` using logging module instead of normal printing.
- Structured the code in proper modular approach. [Proper Directory Structured formed with organized modules]

**BONUS Things Implemented:**

- Build a `scheduler` using `APScheduler` module and can be activated by `python scheduler.py` command. This will run an Entire ETL pipeline at every 24 hours.
- Containerize an Entire pipeline into **Docker**!

## Steps to run:

**Step 1.:**

`pip install -r requirements.txt`

**Step 2.:** [To check single time ETL pipeline run]

```
python main.py
```

**Step 3.:** [To activate the automated scheduler (24 hrs interval auto run)]

```
python scheduler.py
```
