from fastapi import status
from httpx import AsyncClient

from app.schemas import ProfileResponse


async def test_success_update_profile(async_client: AsyncClient):
    await async_client.post("/profile/create", json={"name": "allison"})
    
    payload = {
        "name": "lenyagolikov"
    }
    resp = await async_client.put("/profile/update/1", json=payload)
    assert resp.status_code == status.HTTP_200_OK

    data = resp.json()
    assert ProfileResponse(**data) 


async def test_not_found_update_profile(async_client: AsyncClient):
    payload = {
        "name": "lenyagolikov"
    }
    resp = await async_client.put("/profile/update/2", json=payload)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
