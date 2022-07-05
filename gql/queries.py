from typing import Optional, List

from fastapi import Depends
from strawberry.types import Info
from strawberry.fastapi import GraphQLRouter
import strawberry

from database import get_db
import models
from .schemas import MovieType, ActorType, MovieInput


async def get_context(custom_value=Depends(get_db)):
    return {"db": custom_value}


@strawberry.type
class Query:

    @strawberry.field
    def hello(self, user_name: Optional[str] = None) -> str:
        name = user_name or 'random guy'
        return f"Welcome {name} to graphql API !"

    @strawberry.field
    def movies(self, info: Info) -> List[MovieType]:
        db = info.context['db']
        movie_list = db.query(models.Movie)
        return movie_list

    @strawberry.field
    def actors(self, info: Info) -> List[ActorType]:
        db = info.context['db']
        actor_list = db.query(models.Actor).all()
        return actor_list


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_movie(
        self, 
        movie: MovieInput, 
        info: Info
        ) -> MovieType:
        db = info.context['db']

        db_movie = models.Movie(**movie.__dict__)
        db.add(db_movie)
        db.commit()
        db.refresh(db_movie)

        return movie

schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(
  schema,
  context_getter=get_context,
)