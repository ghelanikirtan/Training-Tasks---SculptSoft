from typing import List, Optional, Dict, Literal
from sqlalchemy import String, Column, Integer, TIMESTAMP
from sqlalchemy import func
from src.app.schemas.base import Base



class RawJob(Base):
    
    __tablename__ = 'jobs_raw_data'
    
    job_id : int = Column(Integer, primary_key =True)
    title: str = Column(String, nullable = False)
    description: str = Column(String)
    company: str =  Column(String)
    url: Optional[str] =  Column(String)
    posted_date: TIMESTAMP =  Column(TIMESTAMP)
    locations: Optional[str] =  Column(String)
    salary_type: Optional[str] =  Column(String)
    salary_currency_code: Optional[str] =  Column(String)
    salary: Optional[str] =  Column(String)
    salary_min: Optional[str] =  Column(String)
    salary_max: Optional[str] =  Column(String)
    site: Optional[str] =  Column(String)
    updated_at: TIMESTAMP =  Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    