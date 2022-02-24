from fastapi import status
from httpx import AsyncClient

from app.schemas import ProfileResponse


async def test_success_create_profile(async_client: AsyncClient):
    payload = {
        "name": "allison",
        "sex": 0
    }
    resp = await async_client.post("/profile/create", json=payload)
    assert resp.status_code == status.HTTP_201_CREATED

    data = resp.json()
    assert ProfileResponse(**data) 


async def test_invalid_create_profile(async_client: AsyncClient):
    payload = {}
    resp = await async_client.post("/profile/create", json=payload)
    assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
