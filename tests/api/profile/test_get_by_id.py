from fastapi import status
from httpx import AsyncClient

from app.schemas import Profile


async def test_success_get_by_id_profile(async_client: AsyncClient):
    await async_client.post("/profile/create", json={"name": "allison"})

    resp = await async_client.get("/profile/get/1")
    assert resp.status_code == status.HTTP_200_OK

    data = resp.json()
    assert Profile(**data)


async def test_not_found_get_by_id_profile(async_client: AsyncClient):
    resp = await async_client.get("/profile/get/2")
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
