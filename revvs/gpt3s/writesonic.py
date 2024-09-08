import aiohttp
import json


async def send_request(prompt: str):
    try:
        url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium&language=en"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Friday/4 CFNetwork/1408.0.4 Darwin/22.5.0",
            "X-Api-Key": "e771bc2d-8feb-4f71-a06a-8b5f2f28b4e5",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
        }
        data = {
            "enable_memory": False,
            "input_text": prompt,
            "enable_google_results": False,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers=headers, data=json.dumps(data)
            ) as response:
                resp = await response.json()
                return resp["message"]
    except Exception as e:
        print(f"Issue with writesonic: {str(e)}")
        return ""

