import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

async def get_car_image_url(query: str) -> str:
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_ACCESS_KEY}&per_page=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            if data["results"]:
                return data["results"][0]["urls"]["regular"]
            return None
