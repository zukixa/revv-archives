import aiohttp
import json
import asyncio
import openai


async def send_request(prompt: str):
    url = "https://chat.aiptl.com/api/openai/v1/chat/completions"  # "http://api.webraft.in:59925/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "user", "content": prompt},
    ]
    data = {"model": "gpt-3.5-turbo-16k", "messages": messages, "stream": False}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(data)) as resp:
            js = await resp.json()
            a = js["choices"][0]["message"]["content"]
        #    print(a)
            return a


