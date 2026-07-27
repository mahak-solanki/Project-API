from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base


class Movie(Base):

    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    genre = Column(String(100), nullable=False)
    language = Column(String(100), nullable=False)
    release_year = Column(Integer)
    rating = Column(Float)
    duration = Column(Integer)
    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )
    owner = relationship(
        "User",
        back_populates="movie"
    )