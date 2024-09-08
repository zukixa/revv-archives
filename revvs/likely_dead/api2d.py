import asyncio
import aiohttp
import json
import random
import string


url = "https://stream.api2d.net/v1/chat/completions"


async def get_response(prompt, key):
    # print(f"key: {key}")
    data = {
        "messages": [{"content": prompt, "role": "user"}],
        "temperature": 0.60000000000000001,
        "model": "gpt-4",
        "max_tokens": 1000,
        "stream": True,
    }

    contents = []
    headers = {
        "Accept": "text/event-stream",
        "Content-Type": "application/json",
        "Authorization": f"Bearer fk{key}",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, headers=headers, data=json.dumps(data)
        ) as response:
            while True:
                line = await response.content.readline()
                if not line:
                    break
                line = line.decode("utf-8")
                if line.startswith("data:"):
                    try:
                        content = json.loads(line[5:])["choices"][0]["delta"]["content"]
                        contents.append(content)
                    except:
                        pass

    return "".join(contents)
