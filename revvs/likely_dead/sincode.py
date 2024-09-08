import asyncio
from playwright.async_api import Playwright, async_playwright
from collections import OrderedDict
import base64
import io
from PIL import Image
import re

import random
import string


async def random_string(length):
    # Combine lowercase letters, uppercase letters, and digits
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Generate a random string of the specified length
    return "".join(random.choice(chars) for i in range(length))


async def get_response(prompt):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://app.baseten.co/apps/1Bbgjg0/operator_views/6PJApo0")
        await page.click(".clickable-element.bubble-element.Group.cmhaJq")
        # Locate the input element using its class name
        input_element = page.locator(".bubble-element.Input.cmivc0.a1683497998577x9849")
        # Fill the input element with the desired value
        string = await random_string(8)
        await input_element.fill(f"{string}@gmail.com")
        # Locate the First Name input element using its class name
        first_name_input = page.locator(
            ".bubble-element.Input.cmivaW0.a1683497998577x9849"
        )

        # Fill the First Name input element with the desired value
        await first_name_input.fill("John")

        # Locate the Last Name input element using its class name
        last_name_input = page.locator(
            ".bubble-element.Input.cmivaZ0.a1683497998577x9849"
        )

        # Fill the Last Name input element with the desired value
        await last_name_input.fill("Doe")
        # Locate the password input element using its id
        password_input = page.locator("#pw")

        # Fill the password input element with the desired value
        await password_input.fill("your_password")

        # recaptchav3

        cookies = await page.context.cookies()
        print(cookies)
        cookies = {d["name"]: d["value"] for d in cookies}
        cooki = OrderedDict()
        for key in [
            "_ga_NYTBYY5CMZ",
            "_ga",
            "csrftoken",
            "__hstc",
            "hubspotutk",
            "__hssrc",
            "__hssc",
            "__cf_bm",
            "intercom-id-kol4lyw4",
            "intercom-session-kol4lyw4",
            "intercom-device-id-kol4lyw4",
            "mp_ee10470651a1b51008f32cde33152c0b_mixpanel",
        ]:
            value = cookies.get(key)
            if value is not None:
                cooki[key] = value
        cookie_str = ""
        for key, value in cooki.items():
            cookie_str += f"{key}={value}; "
        # Request headers
        headers = {
            "POST": "/applications/1Bbgjg0/production/worklets/M0kMMkq/invoke",
            "Host": "app.baseten.co",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://app.baseten.co/apps/1Bbgjg0/operator_views/6PJApo0",
            "Content-Type": "application/json",
            "X-CSRFToken": cooki["csrftoken"],
            "X-OPERATING-WORKFLOW-ID": "1Bbgjg0",
            "Origin": "https://app.baseten.co",
            "Connection": "keep-alive",
            "Cookie": cookie_str,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }

        data = {"worklet_input": {"prompt": prompt}}
        # send api request
        api_context = await playwright.request.new_context()
        resp = await api_context.post(
            "https://app.baseten.co/applications/1Bbgjg0/production/worklets/M0kMMkq/invoke",
            headers=headers,
            data=data,
        )
        outputImage = await resp.json()
        data = outputImage["worklet_output"][22:]
        data = data.encode()
        data = re.sub(rb"[^a-zA-Z0-9%s]+" % b"+/", b"", data)  # normalize
        missing_padding = len(data) % 4
        if missing_padding:
            data += b"=" * (4 - missing_padding)
        return data
