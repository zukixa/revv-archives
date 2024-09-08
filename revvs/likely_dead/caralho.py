import aiohttp
import asyncio
import json


async def send_request(prompt):
    url = "https://gcode-api-ia.glitch.me/randomuser"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.gptnerdes.com",
        "Referer": "https://www.gptnerdes.com/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            print(await response.text())
            response_json = await response.json()
            sessionId = response_json["session"]
            userId = response_json["user_id"]

        url = f"https://gcode-api-ia.glitch.me/persons?session={sessionId}"
        async with session.get(url, headers=headers) as response:
            pass

        other_id = 34838348  # known GPT-3.5, but its autistically system prompted by the creator
        url = f"https://gcode-api-ia.glitch.me/add-friend?session={sessionId}&other_id={other_id}"
        async with session.get(url, headers=headers) as response:
            pass

        url = "https://gcode-api-ia.glitch.me/question"
        headers["Content-Type"] = "application/json"
        data = {
            "session": sessionId,
            "message": prompt,
            "model_id": 34838348,
            "context": [],
        }

        async with session.post(
            url, headers=headers, data=json.dumps(data)
        ) as response:
            response_json = await response.json()
            answer = response_json["message"]

    return answer
