import httpx
import json
import asyncio


async def fetch_image(prompt):
    url = "https://chat-a.nbclass.me/api/images"
    headers = {
        "Content-Type": "text/plain;charset=UTF-8",
        "Accept": "*/*",
        "Origin": "https://chat-a.nbclass.me",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://chat-a.nbclass.me/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
    }
    data = {
        "password": "",
        "model": "Midjourney",
        "prompt": prompt,
        "serverId": "",
        "channelId": "",
        "type": "imagine",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=json.dumps(data))
        print(response.text)
        job_id = response.json()["id"]

        url = f"https://chat-a.nbclass.me/api/images?model=Midjourney&jobId={job_id}"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://chat-a.nbclass.me/",
            "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        }
        fif = None
        while True:
            await asyncio.sleep(5)
            response = await client.get(url, headers=headers)
            data = response.json()
            if "images" in data:
                if data["images"]:
                    fif = data
                    break

        url = "https://chat-a.nbclass.me/api/images"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://chat-a.nbclass.me",
            "Referer": "https://chat-a.nbclass.me/",
            "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        }
        data = {
            "password": "",
            "model": "Midjourney",
            "prompt": fif["prompt"],
            "serverId": "",
            "channelId": "",
            "type": "upscale",
            "customId": fif["images"][0]["actions"][0][0]["id"],
            "index": 1,
            "messageId": fif["id"],
            "imageId": fif["images"][0]["id"],
            "clientId": fif["client_id"],
        }

        response = await client.post(url, headers=headers, data=json.dumps(data))

        while True:
            url = f"https://chat-a.nbclass.me/api/images?model=Midjourney&jobId={fif['id']}"
            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://chat-a.nbclass.me/",
                "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "macOS",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            }
            await asyncio.sleep(5)
            response = await client.get(url, headers=headers)
            data = response.json()
            if "images" in data:
                if data["images"]:
                    if len(data["images"]) > 1:
                        fif = data
                        break
    print(fif["images"][1]["url"])
    return fif["images"][1]["url"]
