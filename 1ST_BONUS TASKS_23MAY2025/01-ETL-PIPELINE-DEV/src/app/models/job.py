# from sqlalchemy import 
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime 

class JobData(BaseModel):
    
    title: str 
    description: str 
    company: str 
    url : Optional[str] 
    posted_date : datetime 
    
    def to_dict(self) -> Dict[str, Any]:
        """Converting the Object data into dictionery format."""
        return {
            'title': self.title,
            'description': self.description,
            'company': self.company,
            'url': self.url,
            'posted_date' : self.posted_date
        }

        

    
# from datetime import datetime

# date_string = "Mon, 05 May 2025 07:50:47 GMT"
# dt_object = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S GMT")

# print(dt_object)
# print(type(dt_object))    