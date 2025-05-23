from typing import Dict, List, Optional
from datetime import datetime 
from src.app.schemas.job import Job
from src.app.models.job import JobData

class TransformData:
    
    def transform_job(self, job:JobData) -> Optional[Job]:

        return Job(
            title=job.title,
            description=job.description,
            url = job.url, 
            company= job.company,
            posted_date=job.posted_date
        )
        
    def transform_all_jobs(self, jobs: List[JobData]) -> List[Job]:
        return [self.transform_job(job) for job in jobs]
        
        
        
        