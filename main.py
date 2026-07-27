from fastapi import FastAPI
from routers.auth_router import router as auth_router
from routers.movie_router import router as movie_router
app = FastAPI(
    title="Movie Collection API",
    description="Production Ready FastAPI Project",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(movie_router)
@app.get("/")
def home():
    return {
        "message": "Movie Collection API Running Successfully"
    }