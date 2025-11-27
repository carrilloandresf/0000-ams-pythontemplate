from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter(prefix="/api/stats", tags=["Estadísticas"])


@router.get("/user-count")
def user_count(db: Session = Depends(get_db)):
    result = db.execute(text("CALL user_count()"))
    row = result.fetchone()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay datos disponibles")
    return {"total_users": row[0]}


@router.get("/user-stats/{user_id}")
def user_stats(user_id: int, db: Session = Depends(get_db)):
    result = db.execute(text("CALL user_stats(:user_id)"), {"user_id": user_id})
    row = result.fetchone()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    user_data = result.keys()
    return dict(zip(user_data, row))
