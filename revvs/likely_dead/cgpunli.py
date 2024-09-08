import asyncio
from playwright.async_api import Playwright, async_playwright
from collections import OrderedDict
import re
import time


async def get_response(prompt):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.chatgptunli.com/chatgpt/")
        cookies = await page.context.cookies()
        cookies = {d["name"]: d["value"] for d in cookies}
        cooki = OrderedDict()
        cooki["_ga"] = cookies["_ga"]
        cooki["_ga_B0SG0H6HVH"] = cookies["_ga_B0SG0H6HVH"]
        cooki["__gads"] = cookies["__gads"]
        cooki["__gpi"] = cookies["__gpi"]
        cookie_str = ""
        for key, value in cooki.items():
            cookie_str += f"{key}={value}; "
        headers = {
            "Cookie": cookie_str,
            "Referer": "https://www.chatgptunli.com/chatgpt/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        }
        data = {
            "id": None,
            "chatId": "default",
            "session": "N/A",
            "clientId": "9ds6v6h63v4",
            "contextId": 382,
            "messages": [
                {
                    "id": "vxp92lcx2vb",
                    "role": "assistant",
                    "content": "Hi! How can I help you?",
                    "who": "AI: ",
                    "html": "Hi! How can I help you?",
                    "timestamp": int(time.time()),
                }
            ],
            "newMessage": prompt,
        }
        # send api request
        api_context = await playwright.request.new_context()
        resp = await api_context.post(
            "https://www.chatgptunli.com/wp-json/mwai-bot/v1/chat",
            headers=headers,
            data=data,
        )
        # print the return from the streamed request above
        answer = await resp.json()
        print(answer)
        await browser.close()
        return answer["reply"]


async def main():
    ans = await get_response("Hello World")
    print(ans)

