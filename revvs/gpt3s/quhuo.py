import re

import aiohttp
import json


async def send_request(prompt):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "http://104.243.20.14:3002",
        "Referer": "http://104.243.20.14:3002/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    }

    base_url = "http://104.243.20.14:3002"
    async with aiohttp.ClientSession() as session:
        data = {"prompt": prompt, "options": {}}
        response = await session.post(
            f"{base_url}/api/chat-process", headers=headers, data=json.dumps(data)
        )

        response_text = await response.text()

        # split by lines
        lines = response_text.split("\n")

        last_text = None
        # process lines one by one
        for line in lines:
            matches = re.findall('"text":"(.*?)"', line)
            if matches:
                last_text = matches[
                    0
                ]  # get the only item (the behavior of findall and text is different here)
        return str(last_text)
