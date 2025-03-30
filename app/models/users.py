from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    username:str
    password:str
    email:str
    phone:str
    
users_db = [User(id=1, username="Madriñan", password="0510", email="jmadrinanpinzon@gmail.com", phone="3104384713"),
            User(id=2, username="Juan", password="1005", email="juann@gmail.com", phone="3104384713"),
            User(id=3, username="Pedro", password="5511", email="pedro@gmail.com", phone="3104384713")]

@app.get("/users")
async def users():
    return users_db

#Path
@app.get("/user/{id}")
async def user(id: int):
    return search_validation(id)

@app.post("/user/")
async def createUser(user: User):
    if type(search_validation(user.id)) == User:
        return "Este usuario ya existe"
    else:
        users_db.append(user)



#Query
@app.get("/userquery/")
async def user(id: int):
    return search_validation(id)
    
def search_validation(id: int):
    users = filter(lambda user:user.id == id, users_db)
    try :
        return list(users)[0]
    except: 
        return "Id Incorrecto 🎈"

    