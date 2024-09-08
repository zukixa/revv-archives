import aiohttp
import json


async def send_request(prompt):
    url = "https://pocket.daku.tech/pocketai/api/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://pocket.daku.tech",
        "Referer": "https://pocket.daku.tech/pocketai/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    }
    data = {
        "prompt": prompt,
        "model": "gpt-3.5-turbo-16k",
        "plugin": "vanilla",
        "pocketai": True,
        "temperature": "0.8",
        "memories": False,
        "Abstract": False,
        "key": "null",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, headers=headers, data=json.dumps(data)
        ) as response:
            rd = json.loads(await response.text())
            print(rd["choices"][0]["message"]["content"])
            return str(rd["choices"][0]["message"]["content"])


