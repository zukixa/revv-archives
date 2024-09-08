import random
import asyncio
from playwright.async_api import Playwright, async_playwright
import json
import uuid


async def get_response(prompt, negative_prompt, engine):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://sexy.ai")

        id = "7cc96903-4298-4252-9dde-c45322e6f1b6"  # "74b62ca1-370a-446d-8f8d-6b606e3305b7"
        print(id)
        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "173",
            "Content-Type": "text/plain;charset=UTF-8",
            "Host": "api.sexy.ai",
            "Origin": "https://sexy.ai",
            "Referer": "https://sexy.ai/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
        }
        data = {
            "sessionID": id,
            "prompt": prompt,
            "negprompt": negative_prompt,
            "seed": random.randrange(10**15, 10**16),
            "steps": 20,
            "modelName": engine,
            "subseed": 0,
            "subseed_strength": 0,
        }
        # send api request
        api_context = await playwright.request.new_context()
        resp = await api_context.post(
            "https://api.sexy.ai/generateImage",
            headers=headers,
            data=data,
        )
        text = await resp.text()
        print(text)
        data = json.loads(text)
        imageID = data["payload"]["imageID"]
        ignoredWords = data.get("payload", {}).get("ignoredWords", None)
        areWeOut = "pending"
        headers2 = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "77",
            "Content-Type": "text/plain;charset=UTF-8",
            "Host": "api.sexy.ai",
            "Origin": "https://sexy.ai",
            "Referer": "https://sexy.ai/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "macOS",
        }
        data2 = {
            "sessionID": id,
            "imageID": imageID,
        }
        timeCounter = -1
        while areWeOut == "pending":
            resp = await api_context.post(
                "https://api.sexy.ai/getImageStatus",
                headers=headers2,
                data=data2,
            )
            text = await resp.text()
            timeCounter += 1
            print(text)
            await asyncio.sleep(8)
            data = json.loads(text)
            if data["payload"]["status"] != "pending":
                await browser.close()
                return data["payload"]["url"], ignoredWords
            elif timeCounter > 6:
                await browser.close()
                return "Request failed to materialize.", ignoredWords
