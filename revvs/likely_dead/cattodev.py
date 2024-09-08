import aiohttp
import asyncio
import json


async def make_request():
    url = "https://stream.api2d.net/v1/chat/completions"
    headers = {
        "Accept": "text/event-stream",
        "Content-Type": "application/json",
        "Authorization": "Bearer fk186035-irVwQKdoHJhfZQN3qKnho2XVdj4rIgaY",
        "Cache-Control": "no-cache",
        "Content-Length": "132",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
    }

    payload = {
        "messages": [{"content": "Hello", "role": "user"}],
        "temperature": 0.20000000000000001,
        "model": "gpt-4",
        "max_tokens": 1500,
        "stream": True,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=payload) as response:
            response_text = await response.text()
            print(response_text)


async def main():
    await make_request()


