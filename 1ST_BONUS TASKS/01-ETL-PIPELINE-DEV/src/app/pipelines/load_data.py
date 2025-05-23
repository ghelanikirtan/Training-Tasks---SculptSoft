from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List, Optional 
from src.app.schemas.base import Base
from src.app.schemas.job import Job
from src.app.constants import DB_URL
from src.app import get_logger
from logging import Logger

class LoadData:
    
    def __init__(self):
        self.engine = create_engine(DB_URL)
        self._SessionMaker = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.logger : Logger = get_logger(__name__)
    
    def load_to_sql(self, job: Job):
        session = self._SessionMaker()
        try:
            session.begin()
            
            session.add(job)
            session.commit()
            
            self.logger.info(f"Data Load to SQLite DB success! [single job]")
            
        except Exception as e:
            session.rollback()
            self.logger.warning(f"Data Loading Failed! Rolling Back [single job]")
        finally:
            self.logger.info(f"Closing session! [single job]")
            session.close()
            
    def load_all_jobs(self, jobs: List[Job]):
        
        session = self._SessionMaker()
        try:
            session.begin()
            session.add_all(jobs)
            session.commit()
            self.logger.info(f"Data Load to SQLite DB success! [multiple jobs]")
        except Exception as e:
            session.rollback()
            self.logger.warning(f"Data Loading Failed! Rolling Back. [multiple jobs]: {e}")
        finally:
            self.logger.info(f"Closing Session! [multiple jobs]")