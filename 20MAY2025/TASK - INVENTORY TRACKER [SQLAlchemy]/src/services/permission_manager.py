
from typing import List, Optional
from sqlalchemy import select, update, delete, insert
from sqlalchemy import and_
from sqlalchemy.orm import relationship
# 
from src.services.database import DatabaseService
from src.models.user import User
from src.models.permission import Permission, user_permissions


class PermissionManager:
    
    def __init__(self, services: DatabaseService = None):
        self.services = services if services else DatabaseService()
        self.conn =self.services.conn
        self._SessionMaker = self.services.Session
        self.session = self.services.session
        
        self.is_permitted: bool = False

    def create_permissions(self, permission: Permission):
        session = self._SessionMaker()
        try:
            session.add(permission)
            session.commit()
        except Exception:
            session.rollback()
            print(f"Error creating permission.")
            raise
        finally:
            session.close()
    
    def add_user(self, user:User):
        session = self._SessionMaker()
        try:
            session.add(user)
            session.commit()
        except Exception:
            session.rollback()
            print(f'Error adding user')
            raise
        finally:
            session.close()
            
    
    def grant_permission(self, user_id: int, permission_id: int) -> bool:
        
        session = self._SessionMaker()
        try:
            
            session.begin()
            
            # select user (if exists)
            user = session.execute(
                select(User).where(User.user_id == user_id)
            ).scalars().first()

            if not user:
                raise ValueError(f"User with ID {user_id} does not exist.")
            
            permission = session.execute(
                select(Permission).where(Permission.permission_id == permission_id)
            ).scalars().first()
            
            if not permission:
                raise ValueError(f"Permission with ID {permission_id} does not exists")

            existing = session.execute(
                select(user_permissions).where(
                    and_(
                        user_permissions.c.user_id == user_id,
                        user_permissions.c.permission_id == permission_id
                    )
                )
            ).scalars().first()
            
            if existing:
                session.commit()
                return False # permission already granted...
            
            session.execute(
                insert(user_permissions).values(
                    user_id = user_id,
                    permission_id = permission_id
                )
            )
            session.commit()
            return True

        except Exception as e:
            session.rollback()
            print(f"Error granting permission: {e}")
            raise
        finally:
            session.close()
        

    def revoke_permission(self, user_id: int, permission_id: int) -> bool:
        session = self._SessionMaker()
        try:
            session.begin()
            
            existing = session.execute(
                select(user_permissions).where(
                    and_(
                        user_permissions.c.user_id == user_id,
                        user_permissions.c.permission_id == permission_id
                    )
                )
            ).scalars().first()
            
            if not existing:
                session.commit()
                return False #nothing to revoke...
            
            session.execute(
                delete(user_permissions).where(
                    and_(
                        user_permissions.c.user_id == user_id,
                        user_permissions.c.permission_id == permission_id
                    )
                )
            )

            session.commit()
            return True
        
        except Exception as e:
            session.rollback()
            print(f"Error Revoking permissino: {e}")
            raise
        finally:
            session.close()
            
        
    