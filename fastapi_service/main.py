from fastapi import FastAPI, Header, HTTPException
import httpx
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

DJANGO_URL = os.getenv("DJANGO_BASE_URL", "http://localhost:8000")


@app.get("/public-data/")
async def public_data(Authorization: str = Header(None)):
    if not Authorization:
        raise HTTPException(status_code=401, detail="No token provided")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{DJANGO_URL}/api/protected-data/",
                headers={"Authorization": Authorization},
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                return {
                    "data": "some public data",
                    "user": data["user"]
                }
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

