from fastapi import APIRouter, Depends , Query , status
from sqlalchemy.orm import Session
from typing import List

from dependencies.database import get_db
from schemas.movie import (
    MovieCreate,
    MovieUpdate,
    MovieResponse
)
from services.movie_service import (
    add_movie,
    get_all_movies,
    get_single_movie,
    edit_movie,
    remove_movie
)
from dependencies.auth_dependency import get_current_user
from models.user import User

router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)

# add movie
@router.post("/", response_model=MovieResponse,
                status_code=status.HTTP_201_CREATED,
                summary="Add New Movie",
                description="Adds a new movie for the authenticated user.",
                response_description="Movie created successfully." )
def create_movie(
    movie: MovieCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return add_movie(
        db,
        movie,
        current_user
    )
    
#get all movvie
@router.get("/", response_model=list[MovieResponse],
            summary="Get Movies",
            description="Returns movies of the currently logged in user. Supports search, filtering and pagination.",
            response_description="List of movies.")
def read_movies(

    title: str | None = Query(None),
    genre: str | None = Query(None),
    language: str | None = Query(None),
    rating: float | None = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)

):

    return get_all_movies(
        db=db,
        current_user=current_user,
        title=title,
        genre=genre,
        language=language,
        rating=rating,
        skip=skip,
        limit=limit

    )
    
#get movie by id
@router.get("/{movie_id}",response_model=MovieResponse,
                summary="Get Movie By ID",
                description="Returns a single movie by its ID.",
                response_description="Movie details.")
def read_movie(
    movie_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_single_movie(
        db,
        movie_id,
        current_user
    )
    
#update movie
@router.put("/{movie_id}",response_model=MovieResponse,
            summary="Update Movie",
            description="Updates movie details for the authenticated user.",
            response_description="Updated movie.")
def update_movie(
    movie_id: int,
    movie: MovieUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return edit_movie(
        db,
        movie_id,
        movie,
        current_user
    )
    
#delete movie
@router.delete("/{movie_id}" ,
                summary="Delete Movie",
                description="Deletes a movie belonging to the authenticated user.",
                response_description="Movie deleted successfully.")
def delete_movie(
    movie_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return remove_movie(
        db,
        movie_id,
        current_user
    )