from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import Profile
from app.schemas import ProfileCreate, ProfileUpdate


async def create(db: AsyncSession, payload: ProfileCreate) -> int:
    profile = Profile(**payload.dict())
    db.add(profile)
    await db.commit()
    return profile.id


async def get_all(db: AsyncSession) -> List[Profile]:
    profiles = await db.execute(select(Profile))
    return profiles.scalars().all()


async def get_by_id(db: AsyncSession, id: int) -> Profile:
    profile = await db.execute(select(Profile).where(Profile.id == id))
    return profile.scalar()


async def update(db: AsyncSession, profile: Profile, payload: ProfileUpdate) -> int:
    payload = payload.dict(exclude_unset=True)
    for field, value in payload.items():
        setattr(profile, field, value)
    db.add(profile)
    await db.commit()
    return profile.id


async def delete(db: AsyncSession, profile: Profile) -> int:
    await db.delete(profile)
    await db.commit()
    return profile.id
