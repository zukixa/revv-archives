import random
import asyncio
import aiohttp
import json
import uuid
from curl_cffi.requests import AsyncSession

async def get_self_user(session, idd):
    self_user_url = "https://api.sexy.ai/getSelfUser"
    params = {
        "sessionID": idd,
        "isAtLeast18Confirmed": "true",
    }
    response = await session.get(self_user_url, params=params)
    status = response.status_code
    print(response.text)
    if status == 200:
        print('success')
        data = response.json()
        return data
    else:
        return None

async def get_response(prompt, negative_prompt, engine):
    async with AsyncSession(impersonate="chrome107") as session:
        idd = "26837b65-f0f9-47ff-b120-011b06905659"
        self_user_data = await get_self_user(session, idd)
        if self_user_data is None:
            print("Failed to get self user data.")
            return
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://sexy.ai",
            "Referer": "https://sexy.ai/",
            "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }
        data = {
            "modelName": engine,
            "folderID": "",
            "prompt": prompt,
            "negprompt": negative_prompt,
            "restoreFaces": True,
            "sessionID": idd,
            "width": 768,
            "height": 768,
            "steps": 20,
            "seed": random.randint(1, 760547),
            "subseed": 0,
            "subseed_strength": 0.1,
            "sampler": "DPM++ 2M Karras",
            "cfgscale": 7,
        }

        # send api request
        resp = await session.post(
            "https://api.sexy.ai/generateImage",
            headers=headers,
            json=data,
        )
        text = resp.text
        data = json.loads(text)
        print(data)
        imageID = data.get("payload", {}).get("imageID", None)  # data["imageID"]

        censored = data.get("hasError")
        if censored:
            return (
                "https://cdn.discordapp.com/attachments/408486840677695498/1146757482904031302/Screenshot_2023-08-31_at_12.43.50_PM.png",
                f"{prompt} or {negative_prompt}",
            )

        ignoredWords = data.get("payload", {}).get("ignoredWords", None)
        areWeOut = "pending"
        headers2 = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://sexy.ai",
            "Referer": "https://sexy.ai/",
            "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }
        timeCounter = -1
        while areWeOut == "pending":
            await asyncio.sleep(2)
            resp = await session.get(
                f"https://api.sexy.ai/getItemStatus?imageID={imageID}&sessionID={idd}",  # getImageStatus",
                headers=headers2,
            )
            text = resp.text
            timeCounter += 1
            if text:
                data = json.loads(text)
                if data.get("payload", {}).get("status", None) != "pending":
                    return data["payload"]["url"], ignoredWords
                elif timeCounter > 6:
                    return "Request failed to materialize.", ignoredWords