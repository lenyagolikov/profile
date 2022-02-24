from fastapi import status
from httpx import AsyncClient

from app.schemas import ProfileResponse


async def test_success_delete_profile(async_client: AsyncClient):
    await async_client.post("/profile/create", json={"name": "allison"})
    
    resp = await async_client.delete("/profile/delete/1")
    assert resp.status_code == status.HTTP_200_OK

    data = resp.json()
    assert ProfileResponse(**data) 


async def test_not_found_delete_profile(async_client: AsyncClient):
    resp = await async_client.delete("/profile/delete/2")
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
