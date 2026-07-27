from pydantic import BaseModel, Field


# Movie Create Schema
class MovieCreate(BaseModel):

    title: str = Field(..., min_length=1, max_length=100)
    genre: str = Field(..., min_length=2, max_length=50)
    language: str = Field(..., min_length=2, max_length=50)
    release_year: int = Field(..., ge=1900, le=2100)
    rating: float = Field(..., ge=0, le=10)
    duration: int = Field(..., gt=0)


# Movie Update Schema
class MovieUpdate(BaseModel):

    title: str | None = Field(default=None, min_length=1, max_length=100)
    genre: str | None = Field(default=None, min_length=2, max_length=50)
    language: str | None = Field(default=None, min_length=2, max_length=50)
    release_year: int | None = Field(default=None, ge=1900, le=2100)
    rating: float | None = Field(default=None, ge=0, le=10)
    duration: int | None = Field(default=None, gt=0)


# Movie Response Schema
class MovieResponse(BaseModel):

    id: int
    title: str
    genre: str
    language: str
    release_year: int
    rating: float
    duration: int
    owner_id: int

    class Config:
        from_attributes = True