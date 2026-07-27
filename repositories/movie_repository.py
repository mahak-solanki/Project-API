from sqlalchemy.orm import Session
from models.movie import Movie


def create_movie(db: Session, movie: Movie):
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

#get movies
def get_movies(
    db: Session,
    owner_id: int,
    title: str | None = None,
    genre: str | None = None,
    language: str | None = None,
    rating: float | None = None,
    skip: int = 0,
    limit: int = 10
):

    query = db.query(Movie).filter(
        Movie.owner_id == owner_id
    )

    # Search by Title
    if title:
        query = query.filter(
            Movie.title.ilike(f"%{title}%")
        )

    # Filter by Genre
    if genre:
        query = query.filter(
            Movie.genre == genre
        )

    # Filter by Language
    if language:
        query = query.filter(
            Movie.language == language
        )

    # Filter by Rating
    if rating:
        query = query.filter(
            Movie.rating >= rating
        )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_movie_by_id(db: Session, movie_id: int):
    return (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )


def update_movie(db: Session):
    db.commit()


def delete_movie(db: Session, movie: Movie):
    db.delete(movie)
    db.commit()