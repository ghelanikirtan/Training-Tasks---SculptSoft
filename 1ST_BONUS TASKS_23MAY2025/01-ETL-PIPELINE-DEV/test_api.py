from careerjet_api_client import CareerjetAPIClient

from src.app.models.job import JobData

import json

class DF:
    def __init__(self):
        self.cj_cli = CareerjetAPIClient('en_US')
    
    def extract(self,kw: str = "Engineer", location: str = "USA", ps : int = 100):
        jobs = []
        
        search_params = {
                    'keywords': kw,
                    'location': location,
                    'affid': 'temp',
                    'user_ip': '11.22.33.44',
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'url': 'https://www.example.com/jobs',
                    'pagesize': ps
                }

        response : dict = self.cj_cli.search(search_params)
        print(json.dumps(response, indent=2))
        

df = DF()

df.extract()