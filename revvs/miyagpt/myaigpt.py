import aiohttp
import asyncio
import json, random


async def send_request(prompt):
    try:
        X_TOKEN = random.choice(
            [
                "391b097e-1f85-4fb4-b7c9-bb372b7c1e2a",
                "7b40cf79-7867-4baa-9009-8efe3dc126d7",
                "b753b4b1-b47b-462a-aa5d-c4ddce2084a8",
                "4fb17e06-8fc5-48d1-9557-b017b7bf323c",
                "ba29b342-f5dd-458c-8eb2-fb650e38078c",
                "476cb8e5-2110-4417-96bb-07044cf7b8cb",
                "6343d849-1247-44a4-a22f-c167732188e6",
            ]
        )
        async with aiohttp.ClientSession() as session:
            # Create Session
            url = "https://www.miyadns.com/api/Chat/CreateSession"
            headers = {
                "authority": "www.miyadns.com",
                "method": "GET",
                "path": "/api/Chat/CreateSession",
                "scheme": "https",
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Cookie": f"X-TOKEN={X_TOKEN}",
                "Referer": "https://www.miyadns.com/",
                "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"macOS"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                "X-Token": X_TOKEN,
            }

            async with session.get(url, headers=headers) as resp:
                r = await resp.json()
                id = r["result"]
                print(id)

            # Create Message
            headers = {
                "authority": "www.miyadns.com",
                "Path": "/api/Chat/CreateMessage",
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/json",
                "Cookie": f"X-TOKEN={X_TOKEN}",
                "Origin": "https://www.miyadns.com",
                "Referer": "https://www.miyadns.com/",
                "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"macOS"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                "X-Token": X_TOKEN,
            }
            url = "https://www.miyadns.com/api/Chat/CreateMessage"
            data = {
                "sessionId": str(id),
                "msg": f"{prompt}\n",
                "messageType": "chat",
            }

            async with session.post(url, headers=headers, json=data) as resp:
                r = await resp.json()
                print(r)
            print("id check again")
            print(id)
            url = f"https://www.miyadns.com/api/Chat/Gpt?sessionId={id}&version=2"
            async with session.post(url=url, headers=headers) as resp:
                print("we are inside")
                r = await resp.text()
                print(r)
            url = "https://www.miyadns.com/api/Chat/DelSession"
            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Cookie": f"X-TOKEN={X_TOKEN}",
                "Referer": "https://www.miyadns.com/",
                "Sec-Ch-Ua": '"Not;A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"macOS"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                "X-Token": X_TOKEN,  # replace with your X-Token
            }
            params = {"sid": str(id)}  # replace with your sid
            async with session.get(url, headers=headers, params=params) as resp:
                print(resp.status)
                print(await resp.text())
            return r
    except Exception as e:
        print(str(e))
        return ""
