# import strawberry
from flask import Flask, escape, request
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
 
app = Flask(__name__)

# @strawberry.type
# class User:
#     name: str
#     age: int

# @strawberry.type
# class Query:
#     @strawberry.field
#     def user(self) -> User:
#         return User(name="Patrick", age=100)

# schema = strawberry.Schema(query=Query)
router = FastAPI()

@router.get('/gql')
def gql():
  return f'you success !'

if __name__ == "__main__":
    app.run()