import aiohttp
import asyncio
import json

async def send_request(prompt):
    tries = 0
    while tries < 60:
        try:
            tries += 1
            url = "https://mixtral.replicate.dev/api"
            headers = {
                'Content-Type': 'text/plain;charset=UTF-8',
            }
            payload = json.dumps({
                "prompt": f"<s>[INST] {prompt} [/INST]\n",
                "model": "mistralai/mixtral-8x7b-instruct-v0.1",
                "temperature": 1,
                "topP": 0.9,
                "maxTokens": 1024
            })
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=payload) as response:
                    response_text = await response.text()
                    if response_text == "":
                        raise Exception("empty")
                    return response_text
        except:
            tries += 1
    return ""
            
