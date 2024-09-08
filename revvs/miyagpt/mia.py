import aiohttp
import uuid
import json

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "www.miyagpt.com",
    "Origin": "https://www.miyagpt.com",
    "Referer": "https://www.miyagpt.com/",
    "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "X-Token": "c045fbb3-2287-4e94-b9b6-77d5f51143d3",
}


async def send_request(prompt):
    payload = {
        "message": prompt,
        "sessionId": str(uuid.uuid4()),
        "version": "2",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url="https://www.miyagpt.com/api/Chat/Gpt",
            headers=headers,
            data=json.dumps(payload),
        ) as response:
            a = await response.text()
            print(a)
            return a


