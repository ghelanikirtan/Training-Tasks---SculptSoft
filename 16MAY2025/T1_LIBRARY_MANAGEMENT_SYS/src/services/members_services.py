from typing import List, Optional
from src.services.database import DatabaseService
from src.models.member import MEMBER

class MemberServices(DatabaseService):
    
    def __init__(self):
        super().__init__()
    
    def get_member_by_id(self, member_id: int) -> tuple[int, MEMBER]:
        try:
            query = f"""
            SELECT member_id, f_name, l_name, email, phone from members
            where member_id = {member_id}
            """
            records = self.cursor.execute(query)
            records = records.fetchall()
            
            member_id:int = None
            member: MEMBER = None
            for row in records:
                member_id = row[0]
                member = MEMBER(
                    f_name = row[1],
                    l_name = row[2],
                    email = row[3],
                    phone = row[4]
                )
                
            return (member_id, member)
            
        except Exception as e:
            print(f"An error occured [get_member_by_id()]: {e}")
            return None
        
    def get_all_members(self) -> List[tuple[int, MEMBER]]:
        try:
            query = f"""
            SELECT member_id, f_name, l_name, email, phone from members
            """
            records = self.cursor.execute(query)
            records = records.fetchall()
            
            members = []
            for row in records:
                member_id = row[0]
                member = MEMBER(
                    f_name = row[1],
                    l_name = row[2],
                    email = row[3],
                    phone = row[4]
                )
                members.append((member_id, member))
                
            return members
            
        except Exception as e:
            print(f"An error occured [get_member_by_id()]: {e}")
            return []
        
        