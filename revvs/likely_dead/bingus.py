import aiohttp
import json
import asyncio


async def send_request(prompt: str):
    url = "https://chatgpt.yourhana.ai/conversation"
    headers = {
        "Accept": "text/event-stream",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://pandora-ai.netlify.app",
        "Referer": "https://pandora-ai.netlify.app/",
        "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }
    data = {
        "message": prompt + "#nosearch",
        "stream": False,
        "clientOptions": {"clientToUse": "bing"},
        "shouldGenerateTitle": False,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, headers=headers, data=json.dumps(data)
        ) as response:
            print(await response.text())
            t = (await response.json())["response"]
            print(t)
            return t
