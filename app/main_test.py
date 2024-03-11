from crud import user
from schemas import UserOut, UpdateUser
import pandas as pd
from db import engine
def test_user_create() -> UserOut:
    user_retrieved = user.create_user('Jovan', 600, 'jwWofsveanss.nknk@gmail.com')
    user_retrieved = UserOut(
      **user_retrieved.__dict__
    )
    return user_retrieved


# update_user_object = UpdateUser(budget=300, name="Dragan")
# update_element= user.update_user(user_id=3, user_update=update_user_object.dict())
# print(update_element.is_rich)

# if update_element:
#     update_element = UserOut(**update_element.__dict__)
# print(update_element)

#
# user_from_db = user.get_user_by_id(1)
# print(user_from_db.email)
# print(user.remove_user(user_from_db.id))

# data = {
#     'name': ["Dragan","Nikola","Marko"],
#     'budget': [2_500_000, 500_000, 450_000],
#     'email': ['hanotefs451@cmheia.com','aanotef451s@cmheia.com','banotef45s1@cmheia.com']
# }
#
# df = pd.DataFrame(data)
# df.to_sql('user_frame', engine, index=False, if_exists='replace')

df = pd.read_sql_query("SELECT * from user", engine)
print(df)