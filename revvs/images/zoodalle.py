import aiohttp
import asyncio
import uuid
import json
import time

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://zoo.replicate.dev",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}


async def fetch_prediction(prompt):
    data = {
        "prompt": prompt,
        "version": "dall-e",
        "source": "openai",
        "model": "DALL-E",
        "anon_id": str(uuid.uuid4()),
        "submission_id": str(uuid.uuid4()),
        "id": str(uuid.uuid4()),
        "created_at": time.strftime(
            "%Y-%m-%dT%H:%M:%S.%fZ", time.gmtime()
        ),  # current timestamp
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://zoo.replicate.dev/api/predictions",
            headers=headers,
            data=json.dumps(data),
        ) as post_response:
            text = await post_response.text()
            print(text)
            post_response_json = json.loads(text)
            print(post_response_json["output"][0])
            return post_response_json["output"][0]
