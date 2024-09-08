import aiohttp
import asyncio
import re
import json


async def send_request(prompt):
    try:
        async with aiohttp.ClientSession() as session:
            # Login part
            data = {
                "account": "免费使用GPT3.5模型@163.com",
                "password": "659e945c2d004686bad1a75b708c962f",
            }
            headers = {
                "authority": "ai.berlin4h.top",
                "method": "POST",
                "path": "/api/login",
                "scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/json",
                "token": "undefined",
                "Origin": "https://ai.berlin4h.top",
                "Referer": "https://ai.berlin4h.top/",
                "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"macOS"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            }

            async with session.post(
                "https://ai.berlin4h.top/api/login", headers=headers, json=data
            ) as response:
                if response.status != 200:
                    return f"Error: {response.status}"
                resp_json = await response.json()
                print(response.status)
                print(resp_json["data"]["token"])
                token = resp_json["data"]["token"]

            # Chat completions part
            data = {
                "prompt": prompt,
                "parentMessageId": "",
                "options": {
                    "model": "gpt-3.5-turbo",
                    "temperature": 0.5,
                    "presence_penalty": 0,
                    "frequency_penalty": 0,
                    "max_tokens": 1888,
                },
            }

            headers = {
                "authority": "ai.berlin4h.top",
                "method": "POST",
                "path": "/api/chat/completions",
                "scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/json",
                "Origin": "https://ai.berlin4h.top",
                "Referer": "https://ai.berlin4h.top/",
                "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"macOS"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "token": token,
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            }
            await asyncio.sleep(3)
            async with session.post(
                "https://ai.berlin4h.top/api/chat/completions",
                headers=headers,
                json=data,
            ) as response:
                resp_text = await response.text()
                print(resp_text)
                pattern = re.compile(r"\"content\":\s*\"(.*?)\"")
                matches = pattern.findall(resp_text)
                ans = ""
                for match in matches:
                    ans += match
                print(ans)
                return ans
    except Exception as e:
        print(f"Issue with Berlin: {str(e)}")
        return ""

