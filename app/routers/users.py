from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_db
from app.models import User

router = APIRouter(prefix="/api/users", tags=["Usuarios"])


def _get_user_or_404(db: Session, user_id: int) -> User:
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user


@router.get("", response_model=list[schemas.UserRead])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    user = User(name=payload.name, email=payload.email)
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está registrado")
    db.refresh(user)
    return user


@router.get("/count", response_model=schemas.UserCount)
def user_count(db: Session = Depends(get_db)):
    total = db.scalar(select(func.count()).select_from(User)) or 0
    return {"total_users": total}


@router.get("/{user_id}", response_model=schemas.UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return _get_user_or_404(db, user_id)


@router.get("/{user_id}/stats", response_model=schemas.UserRead)
def user_stats(user_id: int, db: Session = Depends(get_db)):
    return _get_user_or_404(db, user_id)


@router.put("/{user_id}", response_model=schemas.UserRead)
def update_user(user_id: int, payload: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = _get_user_or_404(db, user_id)

    if payload.name is not None:
        user.name = payload.name
    if payload.email is not None:
        user.email = payload.email

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está registrado")
    db.refresh(user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = _get_user_or_404(db, user_id)
    db.delete(user)
    db.commit()
    return None
