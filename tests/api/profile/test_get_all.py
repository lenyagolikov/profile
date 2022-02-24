from fastapi import status
from httpx import AsyncClient

from app.schemas import Profile


async def test_success_get_all_profiles(async_client: AsyncClient):
    await async_client.post("/profile/create", json={"name": "allison"})

    resp = await async_client.get("/profile/list")
    assert resp.status_code == status.HTTP_200_OK

    data = resp.json()[0]
    assert Profile(**data)
