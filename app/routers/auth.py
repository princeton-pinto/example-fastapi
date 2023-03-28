from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, models, utils, oauth2
from ..database import get_db


router = APIRouter(
    tags=['Authentication']
)

@router.post("/login", response_model=schemas.Token)
def login(user_credetials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
# def login(user_credetials: schemas.UserLogin, db: Session = Depends(get_db)):

    # OAuth2PasswordRequestForm returns dict in the format {"username":"DanaWhite@ufc.com","password":"ufcpresident"}, so replace field "email" below to "username"

    user = db.query(models.User).filter(models.User.email == user_credetials.username).first()
    # user = db.query(models.User).filter(models.User.email == user_credetials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    if not utils.verify(user_credetials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    #create token
    access_token = oauth2.create_access_token(data= {"user_id": user.id})

    #return token
    return {"access_token": access_token, "token_type": "bearer"}