from fastapi import FastAPI
# from sqlalchemy.orm import Session

from models import Base
from database import engine, get_db
from gql.queries import graphql_app


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)


app.include_router(graphql_app, prefix="/graphql")
