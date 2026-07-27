from sqlalchemy.orm import Session

from models.movie import Movie
from models.user import User
from schemas.movie import MovieCreate, MovieUpdate
from repositories.movie_repository import (
    create_movie,
    get_movies,
    get_movie_by_id,
    update_movie,
    delete_movie
)

#create movie
def add_movie(
    db: Session,
    movie_data: MovieCreate,
    current_user: User
):

    movie = Movie(
        title=movie_data.title,
        genre=movie_data.genre,
        language=movie_data.language,
        release_year=movie_data.release_year,
        rating=movie_data.rating,
        duration=movie_data.duration,
        owner_id=current_user.id
    )

    return create_movie(db, movie)

#get all movies
def get_all_movies(
    db: Session,
    current_user: User,
    title: str | None = None,
    genre: str | None = None,
    language: str | None = None,
    rating: float | None = None,
    skip: int = 0,
    limit: int = 10
):

    return get_movies(
        db=db,
        owner_id=current_user.id,
        title=title,
        genre=genre,
        language=language,
        rating=rating,
        skip=skip,
        limit=limit
    )
    
#get single movie
def get_single_movie(
    db: Session,
    movie_id: int,
    current_user: User
):

    movie = get_movie_by_id(
        db,
        movie_id
    )

    if not movie:
        raise ValueError("Movie not found.")

    if movie.owner_id != current_user.id:
        raise ValueError("Unauthorized access.")

    return movie

#update movie
def edit_movie(
    db: Session,
    movie_id: int,
    movie_data: MovieUpdate,
    current_user: User
):

    movie = get_movie_by_id(
        db,
        movie_id
    )

    if not movie:
        raise ValueError("Movie not found.")

    if movie.owner_id != current_user.id:
        raise ValueError("Unauthorized access.")

    update_data = movie_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(movie, key, value)

    update_movie(db)

    return movie

#delete movie
def remove_movie(
    db: Session,
    movie_id: int,
    current_user: User
):

    movie = get_movie_by_id(
        db,
        movie_id
    )

    if not movie:
        raise ValueError("Movie not found.")

    if movie.owner_id != current_user.id:
        raise ValueError("Unauthorized access.")

    delete_movie(
        db,
        movie
    )

    return {
        "message": "Movie deleted successfully."
    }