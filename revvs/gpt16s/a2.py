# key =
import aiohttp
import json
import asyncio
from curl_cffi.requests import AsyncSession


async def send_request(prompt: str):
    try:
        url = "https://aappt.opao.xyz/api/openai/v1/chat/completions"  # "http://api.webraft.in:59925/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoaWhpamljNjM0IiwiaWF0IjoxNzAxMjIxNTMwLCJleHAiOjE3MDE0ODA3MzB9.VlsiJCOJQNJy9HjhbxS9sux7sS_R6pOBXiMMGlPMXxBxJWFURhDKWxdie-hGFGgb0AvyOorLhLG16jz6R3fBAw",
            "Cookie": "JSESSIONID=0D88B189F2710F655182C3F88C84812D",
        }
        data = {
            "messages": [
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "model": "2号3.5和谐-16k",
            "temperature": 1,
            "presence_penalty": 0,
            "frequency_penalty": 0,
        }
        async with AsyncSession(impersonate="edge101") as session:
            resp = await session.post(url, headers=headers, data=json.dumps(data))
            js = resp.json()
         #   print(js)
            a = js["choices"][0]["message"]["content"]
            return a
    except:
        return ""
