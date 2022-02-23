from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.schemas import Profile, ProfileCreate, ProfileDelete, ProfileUpdate

router = APIRouter()


@router.post("/create")
async def create_profile(db: AsyncSession = Depends(deps.get_db)):
    return {"detail": "create profile"}


@router.get("/list")
async def list_profile(db: AsyncSession = Depends(deps.get_db)):
    return {"detail": "list profile"}


@router.get("/get/{id}")
async def get_profile(id: int, db: AsyncSession = Depends(deps.get_db)):
    return {"detail": id}


@router.put("/update/{id}")
async def update_profile(id: int, db: AsyncSession = Depends(deps.get_db)):
    return {"detail": id}


@router.delete("/delete/{id}")
async def delete_profile(id: int, db: AsyncSession = Depends(deps.get_db)):
    return {"detail": id}
