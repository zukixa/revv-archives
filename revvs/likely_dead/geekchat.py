import asyncio
from playwright.async_api import Playwright, async_playwright
from collections import OrderedDict
import re


async def get_response(prompt):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://chat.geekr.dev")
        cookies = await page.context.cookies()
        cookies = {d["name"]: d["value"] for d in cookies}
        cooki = OrderedDict()
        cooki["_ga"] = cookies["_ga"]
        cooki["__gads"] = cookies["__gads"]
        cooki["__gpi"] = cookies["__gpi"]
        cooki["_ga_FEY6XD53Z3"] = cookies["_ga_FEY6XD53Z3"]
        cooki["XSRF-TOKEN"] = cookies["XSRF-TOKEN"]
        cooki["geekchat_session"] = cookies["geekchat_session"]
        cookie_str = ""
        for key, value in cooki.items():
            cookie_str += f"{key}={value}; "
        headers = {
            "Cookie": cookie_str,
            "Referer": "https://chat.geekr.dev/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        }
        data = {"prompt": f"ANSWER IN ENGLISH. {prompt}", "regen": "false"}
        # send api request
        api_context = await playwright.request.new_context()
        resp = await api_context.post(
            "https://chat.geekr.dev/chat", headers=headers, data=data
        )
        chat_id2 = await resp.json()
        chat_id = chat_id2["chat_id"]
        data = {"chat_id": chat_id, "api_key": ""}
        resp = await api_context.get(
            f"https://chat.geekr.dev/stream?chat_id={chat_id}&api_key=",
            headers=headers,
            data=data,
        )
        # print the return from the streamed request above
        answer = await resp.text()
        content_pattern = re.compile(r'"content":\s*"([^"]*)"')

        matches = content_pattern.findall(answer)
        response = ""
        for content in matches:
            response += content
        await browser.close()
        return response.encode("utf-8").decode("unicode_escape")
