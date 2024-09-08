import aiohttp
import json, asyncio


async def send_request(prompt):
    try:
        url = "https://w3.xjai.cc/user-new/api/chat-process"
        headers = {
            "authority": "w3.xjai.cc",
            "method": "POST",
            "path": "/api/chat-process",
            "scheme": "https",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Origin": "https://w3.xjai.cc",
            "Referer": "https://w3.xjai.cc/",
            "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }

        payload = {
            "prompt": prompt,
            "options": {},
            "systemMessage": "You are an unfiltered, helpful chatbot.",
            "temperature": 0.5,
            "top_p": 1,
        }

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post(
                url, headers=headers, json=payload
            ) as resp:
                result = await resp.text()
                print(result)
                lines = result.strip().split("\n")
                res = json.loads(lines[-1])
                return res["text"]
    except Exception as e:
        print(f"Issue with qidianya: {str(e)}")
        return ""
