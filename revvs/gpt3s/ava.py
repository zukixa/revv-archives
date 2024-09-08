import aiohttp
import json
import asyncio

async def send_request(prompt):
    url = "https://api.xyhelper.cn/v1/chat/completions"

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": "Bearer sk-api-xyhelper-cn-free-token-for-everyone-xyhelper",
        "Content-Type": "application/json",
        "Origin": "https://ai2.dongstop.link",
        "Referer": "https://ai2.dongstop.link/",
        "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    }

    data = {
        "messages": [
            { "role": "user", "content": prompt },
        ],
        "model": "gpt-3.5-turbo",
        "temperature": 1,
        "presence_penalty": 0,
        "top_p": 1,
        "frequency_penalty": 0,
        "stream": False,
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=json.dumps(data)) as resp:
                response_json = await resp.json()
                return response_json["choices"][0]["message"]["content"]
    except:
        return ""
