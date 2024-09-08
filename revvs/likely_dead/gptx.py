import httpx
import re
import asyncio


async def send_request(prompt: str):
    url = "http://chatgpt.bybyte.cn/api/chat-process"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "chatgpt.bybyte.cn",
        "Origin": "http://chatgpt.bybyte.cn",
        "Referer": "http://chatgpt.bybyte.cn/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }

    data = {"prompt": prompt, "options": {}}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        res = response.text
        pattern = re.compile(r"\"text\":\s*\"(.*?)\"")
        matches = pattern.findall(res)
        ans = matches[-1] if matches else None
        print(ans)
        return ans

