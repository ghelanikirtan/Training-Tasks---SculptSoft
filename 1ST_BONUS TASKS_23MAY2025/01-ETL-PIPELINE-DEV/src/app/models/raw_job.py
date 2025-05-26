from typing import Optional, Dict, Any, Literal
from pydantic import BaseModel
from datetime import datetime 


class RawJobData(BaseModel):
    
    title: str
    description: str
    company: str 
    url: Optional[str]
    posted_date: datetime
    locations: Optional[str]
    salary_type: Optional[str]
    salary_currency_code: Optional[str]
    salary: Optional[str]
    salary_min: Optional[str]
    salary_max: Optional[str]
    site: Optional[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Converting the object data into dictionery format..."""
        return {
            'title': self.title,
            'description': self.description,
            'company': self.company,
            'url' : self.url if self.url else None,
            'posted_date': self.posted_date,
            'locations': self.locations if self.locations else None,
            'salary_type': self.salary_type if self.salary_type else None,
            'salary_currency_code' : self.salary_currency_code if self.salary_currency_code else None ,
            'salary': self.salary if self.salary else None ,
            'salary_min': self.salary_min if self.salary_min else None,
            'salary_max': self.salary_max if self.salary_max else None, 
            'site': self.site if self.site else None
        }
