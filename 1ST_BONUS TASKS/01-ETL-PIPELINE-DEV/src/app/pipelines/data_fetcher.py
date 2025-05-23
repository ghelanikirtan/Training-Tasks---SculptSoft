import requests
import json
from typing import List, Optional, Dict
from datetime import datetime
from careerjet_api_client import CareerjetAPIClient
# 
from src.app import get_logger
from src.app.models.job import JobData


class DataFetcher:
    """Fetches the Job Openings data from the careersjet api using CareerjetAPIClient.
    
    This module is solely responsible of extraction of the job data, based on keyword, location and pagesize passed... 
    """
    
    
    def __init__(self):
        self.cj_cli = CareerjetAPIClient("en_US")
        self.logger = get_logger(__name__)
        
    def extract_data(self, keyword: str, location :str = 'India', pagesize: int = 1) -> Optional[List[JobData]]:
        """Extracts the data from an API.
        
        :param keyword(str): Enter the searching keyword related to the type of the job required.
        :param location(str): Enter the Location
        :param pagesize(int): Enter the number of pages to fetch. (defult = 1).
        """
        
        jobs = []
        
        try:
            
            if not keyword or not location:
                self.logger.error(f"keyword and location parameter is mandatory field!")
                return 
            
            if keyword and location:
                
                search_params = {
                    'keywords': keyword,
                    'location': location,
                    'affid': 'temp',
                    'user_ip': '11.22.33.44',
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'url': 'https://www.example.com/jobs',
                    'pagesize': pagesize
                }

                response : dict = self.cj_cli.search(search_params)


                if response:
                    job_data : List[dict] = response["jobs"]
                    
                    for job in job_data:
                        
                        jobs.append(
                            JobData(
                                title = job['title'],
                                description= job['description'],
                                company= job['company'],
                                url = job['url'],
                                posted_date= self.convert_date_obj(job['date'])
                            )
                        )
                    
                    self.logger.info("Extracted the data successfully...")
                    del search_params

                else:
                    self.logger.warning(f"Empty response from careerjet api endpoint")
                
                return jobs

        except Exception as e:
            self.logger.error(f"Error occurred in extracting the data: {e}")
            return []
            
    @staticmethod
    def convert_date_obj(date_string: str) -> datetime:
        return datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S GMT")