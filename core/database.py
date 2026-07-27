#ye file pure project ki database manager ogi koi dusri file create engine nhi likhegi

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker , declarative_base
# from core.config import settings


# engine = create_engine(
#     settings.DATABASE_URL,
#     connect_args= {"check_same_thread" : False}
# )

# Session_local = sessionmaker(
#     autocommit = False,
#     autoflush= False,
#     bind= engine
# )

# Base  = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)
print(settings.DATABASE_URL)


Session_local = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()