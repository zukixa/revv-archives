import aiohttp
import json
import asyncio
import re

try:
    from .. import gp as gp
except:
    import gp as gp
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://chatanywhere.cn",
    "Referer": "https://chatanywhere.cn/",
    "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "macOS",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}


async def send_request(prompt):
    url = "https://chatanywhere.cn/v1/chat/gpt/"

    data = {
        "list": [
            {
                "content": prompt,
                "role": "user",
                "nickname": "",
                "time": "08-06 17:11",
                "isMe": True,
            },
        ],
        "title": "hello",
        "prompt": prompt,
        "temperature": 0.5,
        "models": "61490748",
        "continuous": True,
    }
    pxs = await gp.get_proxy()
    for px in pxs:
        try:
            async with aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(ssl=False)
            ) as session:
                async with session.post(
                    url, headers=headers, data=json.dumps(data), proxy=px, timeout=10
                ) as response:
                    response_text = await response.text()
                    print(response_text)
                    return response_text
        except Exception as e:
            print(f"Issue with chatty: {str(e)}")
            continue
    return ""
