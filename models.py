from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class ActorsToMovies(Base):
    __tablename__ = 'movies_to_actors'

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    actors_num = Column(Integer)
    year = Column(Integer)

    cast = relationship('Actor', secondary='movies_to_actors', back_populates='movie_list')


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String, index=True)
    age = Column(Integer)

    movie_list = relationship('Movie', secondary='movies_to_actors', back_populates='cast')