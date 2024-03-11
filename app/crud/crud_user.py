from app.models import User
from app.db.connection_engine import session
from typing import Optional, List

class CrudUser:

    @staticmethod
    def create_user(name: str, budget: float, email: str) -> Optional[User]:
        db = None
        try:
            db = session()
            new_user_object = User(name=name, budget=budget, email=email)
            db.add(new_user_object)
            db.commit()
            db.flush()
            db.refresh(new_user_object)
        except Exception as e:
            print(e)
            return None
        finally:
            db.close()
        return new_user_object

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        db = None
        try:
            db = session()
            result = db.query(User).filter(User.id == user_id).first()
            return result
        except:
            return None
        finally:
            db.close()


    @staticmethod
    def remove_user(active: bool) -> int:
        db = None
        try:
            db = session()
            result = db.query(User).filter(User.active == active).all()
            print()
            if not result:
                return False
            db.delete(result)
            db.commit()

            return len(result)
        except:
            return 0
        finally:
            db.close()

    @staticmethod
    def update_user(user_id: int, user_update: dict):
        db = None
        try:
            db = session()
            user_from_db = db.query(User).filter(User.id == user_id).first()
            if not user_update:
                return None

            if 'id' in user_update.keys():
               return None

            for k,v in user_update.items():
                if not v:
                    continue
                if k not in user_from_db.__dict__.keys():
                    continue
                setattr(user_from_db, k, v) if getattr(user_from_db, k) != v else None

            result = user_from_db
            db.add(result)
            db.commit()
            db.refresh(result)
            return result
        except Exception as e:
            print(e)
            return None
        finally:
            db.close()


user = CrudUser

