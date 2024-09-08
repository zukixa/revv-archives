import asyncio
from playwright.async_api import async_playwright
import aiohttp
import time
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=100
)

# Get list of user agents.
user_agents = user_agent_rotator.get_user_agents()


async def main():
    prompt = "hello world"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://curva.onrender.com/")

        # Extract cookies
        cookies = await context.cookies()
        print(cookies)
        cookie_str = "; ".join([f"{cookie.name}={cookie.value}" for cookie in cookies])
        print(cookie_str)
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Cookie": cookie_str,
            "Origin": "https://curva.onrender.com",
            "Referer": "https://curva.onrender.com/c/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": user_agent_rotator.get_random_user_agent(),
        }

        async with aiohttp.ClientSession() as session:
            json_payload = {
                "conv": "NSkNHob3",
                "context": "",
                "prompt": prompt,
                "model": "gpt4_t05",
                "web": "BASIC",
                "t": int(time.time()),
                "tz": -7,
            }
            async with session.post(
                "https://curva.onrender.com/api/chat",
                headers=headers,
                json=json_payload,
            ) as response:
                result = await response.json()
                print(result)

        await browser.close()

