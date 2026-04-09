from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def get_user():
    return {"message": "Hi"}

@app.get("/posts")
def get_posts():
    return {"data": "Your post"}

@app.post("/create")
def create_post(post: Post):
    print(post.rating)
    return {"data": "new_post"}