from core.database import Session_local

def get_db():
    db =  Session_local()
    try:
        yield db
    finally:
        db.close()
        
# bar bar db = session_loacl nhi likhna pdega
#db : depends(get_db) se fastapi khud session bnna dega or close krdega
