from sqlalchemy import String, Column, Integer, TIMESTAMP
from sqlalchemy import func
from src.app.schemas.base import Base

class Job(Base):
    
    __tablename__ = "jobs"
    
    job_id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable = False)
    description: str = Column(String)
    company: str = Column(String)
    url: str = Column(String)
    posted_date: TIMESTAMP = Column(TIMESTAMP)
    updated_at: TIMESTAMP = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    def __repr__(self) -> str:
        return f'Job(job_id={self.job_id}, title={self.title}, description={self.description}, url={self.url}, posted_date={self.posted_date}, updated_at={self.updated_at}'