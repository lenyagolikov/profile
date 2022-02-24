from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.api import deps
from app.schemas import (
    Profile,
    ProfileCreate,
    ProfileUpdate,
    ProfileResponse,
)


router = APIRouter()


@router.post("/create", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_profile(payload: ProfileCreate, db: AsyncSession = Depends(deps.get_db)):
    id = await crud.profile.create(db, payload)
    return ProfileResponse(id=id)


@router.get("/list", response_model=List[Profile])
async def get_all_profiles(db: AsyncSession = Depends(deps.get_db)):
    profiles = await crud.profile.get_all(db)
    return profiles


@router.get("/get/{id}", response_model=Profile)
async def get_one_profile(id: int, db: AsyncSession = Depends(deps.get_db)):
    profile = await crud.profile.get_by_id(db, id)
    if profile is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="profile not found")
    return profile


@router.put("/update/{id}", response_model=ProfileResponse, response_model_exclude_unset=True)
async def update_profile(id: int, payload: ProfileUpdate, db: AsyncSession = Depends(deps.get_db)):
    profile = await crud.profile.get_by_id(db, id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="profile not found")
    id = await crud.profile.update(db, profile, payload)
    return ProfileResponse(id=id)


@router.delete("/delete/{id}", response_model=ProfileResponse)
async def delete_profile(id: int, db: AsyncSession = Depends(deps.get_db)):
    profile = await crud.profile.get_by_id(db, id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="profile not found")
    id = await crud.profile.delete(db, profile)
    return ProfileResponse(id=id)
