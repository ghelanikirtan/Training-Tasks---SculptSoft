from typing import List, Dict, Optional
from datetime import datetime
import time
# 
from src.app.pipelines.data_fetcher import DataFetcher
from src.app.pipelines.transform_data import TransformData
from src.app.pipelines.load_data import LoadData
# 
from src.app.schemas.job import Job
from src.app.models.job import JobData
# 
from src.app.constants import KEYWORDS, COUNTRIES
from src.app import get_logger



class ETLPipeline:
    
    def __init__(self):
        self.logger = get_logger(__name__)
        self.extraction_pipeline = DataFetcher()
        self.transformation_pipeline = TransformData()
        self.load_pipeline = LoadData()

    def invoke(self, pagesize: int = 10):
        start_time = datetime.now()
        self.logger.info(f"Started an ETL pipeline...")
        for keyword in KEYWORDS:
            for country in COUNTRIES:
                extracted_data = self.extraction_pipeline.extract_data(keyword=keyword, location=country, pagesize=pagesize)
                transformed_data = self.transformation_pipeline.transform_all_jobs(extracted_data)
                self.load_pipeline.load_all_jobs(transformed_data)
        
        end_time = datetime.now()
        self.logger.info(f"""ETL pipeline stopping!
                         Took {end_time-start_time} seconds. of execution.""")
        
        
        
                
                