import aiohttp
import asyncio
import json


async def send_request(prompt):
    try:
        # Specify the URL where the POST request should be sent
        url = "https://func-chat-service-chat-ngjrwhswfl.us-west-1.fcapp.run/completion"

        # Define the headers for the request
        headers = {
            "Content-Type": "application/json",
        }

        # Define the payload for the request
        payload = {
            "temperature": 0.8,
            "max_tokens": 3000,
            "common_info": {"token": "xD"},
            "messages": [{"role": "user", "content": f"{prompt}"}],
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers=headers, data=json.dumps(payload)
            ) as resp:
                response = await resp.json()
                return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Issue with funcchat: {str(e)}")
        return ""

