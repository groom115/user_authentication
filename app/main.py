from fastapi import FastAPI
from app.model import PostSchema, UserLoginSchema, UserSchema
from app.auth.jwt_handler import signJWT, decodeJWT

app = FastAPI()

posts = [
    {"id": 1, "Name": "Abhishek", "clas": 8},
    {"id": 2, "Name": "Karim", "clas": 12},
    {"id": 3, "Name": "shukla", "clas": 15},
]

users = []


# for testing
@app.get("/", tags=["test"])
def greet():
    return {"helloword": 1}


# get posts
@app.get("/posts", tags=["posts"])
def get_post():
    return posts


# get post by id
@app.get("/post/{id}", tags=["post"])
def get_post_by_id(id: int):
    try:
        if id > len(posts):
            return {"error": "id doesnt exists"}
        for post in posts:
            if post["id"] == id:
                return post
    except Exception as err:
        raise err


# add students
@app.post("/posts", tags=["addUser"])
def add_user(detail: PostSchema):
    detail = detail.dict()
    detail["id"] = len(posts) + 1
    posts.append(detail)
    return posts


# user signup
@app.post("/user/signup", tags=["user"])
def signup(user: UserSchema):
    users.append(user)
    return signJWT(user.email)


# check user signed in or not
def check_user_login(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False


# user login
@app.post("/user/login", tags=["login"])
def user_login(user: UserLoginSchema):
    if check_user_login(user):
        print(True)
        return signJWT(user.email)
    else:
        return {"error": "user doesnt exist"}
