import strawberry

@strawberry.type
class MovieType:
    title: str
    actors_num: int
    year: int

@strawberry.input
class MovieInput:
    title: str
    actors_num: int
    year: int


@strawberry.type
class ActorType:
    name: str
    surname: str
    age: int