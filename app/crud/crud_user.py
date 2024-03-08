from app.models import User
from app.db.connection_engine import session
from typing import Optional

class CrudUser:

    @staticmethod
    def create_user(name: str, budget: float, email: str) -> bool:
        db = None
        try:
            db = session()
            new_user_object = User(name=name, budget=budget, email=email)
            db.add(new_user_object)
            db.commit()
            db.flush()
        except Exception as e:
            print(e)
            return False
        finally:
            db.close()
        return True
    pass


user = CrudUser

