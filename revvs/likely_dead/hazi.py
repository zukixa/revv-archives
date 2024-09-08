import httpx
import json


async def post_request(prompt: str):
    url = "https://hazi-response.vercel.app/api/generate/chat"

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json; charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Gola/25 CFNetwork/1408.0.4 Darwin/22.5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }

    data = {
        "model": "gpt-4-0613",
        "messages": [
            {"role": "user", "content": prompt},
        ],
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=json.dumps(data))
        return response.json()["answer"]
