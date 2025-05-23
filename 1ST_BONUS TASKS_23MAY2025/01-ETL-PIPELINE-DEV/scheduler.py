from apscheduler.schedulers.background import BackgroundScheduler
import time 
from datetime import datetime
# 
from src.app.pipelines.etl import ETLPipeline

from src.app import get_logger



etl_pipeline = ETLPipeline()
logger = get_logger(__name__)


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(etl_pipeline.invoke, "interval", args=(100,), hours=15)
    scheduler.start()
    logger.info("Scheduler started. Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(60)
    
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info(f"Scheduler Stopped.")


# RUN SCHEDULER
start_scheduler()