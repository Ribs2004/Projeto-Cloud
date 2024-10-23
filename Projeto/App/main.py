from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import hashlib
import jwt
import requests
import json
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from dotenv import load_dotenv

load_dotenv()

# Ativar venv: source .venv/bin/activate 
# Rodar fastapi: uvicorn main:app --reload 

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# JWT secret key
SECRET_KEY = "dajsbdhb1"

# HTTPBearer for token-based authentication
bearer_scheme = HTTPBearer()

# User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Projeto')

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to generate JWT token with expiration time
def create_jwt_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return token

# Function to verify JWT token
def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# Registration endpoint
@app.post('/register', tags=['SignUp'])
def register(name: str, email: str, password: str, db: Session = Depends(get_db)):
    # Check if email already exists
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
   
    new_user = User(name=name, email=email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    token_data = {'user_id': new_user.id, 'email': new_user.email}
    token = create_jwt_token(token_data)
    return {'token': token}

# Login endpoint
@app.post('/login', tags=['SignIn'])
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email or password")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if user.password != hashed_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email or password")
    
    token_data = {'user_id': user.id, 'email': user.email}
    token = create_jwt_token(token_data)
    return {'token': token}


# Country information endpoint
@app.get("/consultar", tags=['Consult'])
def consultar_country(name: str = Query(..., description="Digite o nome do país que deseja pesquisar"), credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Extract the token from the Authorization header
    token = credentials.credentials
    
    verify_jwt_token(token)

    # Get country information
    url = f"https://restcountries.com/v3.1/name/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if isinstance(data, list) and len(data) > 0:
            data[0].pop("translations", None)
            data[0].pop("fifa", None)
        return {"country_data": data}
    elif response.status_code == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to retrieve country data")
