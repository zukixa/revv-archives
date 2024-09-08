import asyncio
from playwright.async_api import Playwright, async_playwright
from collections import OrderedDict
import base64
import io
from PIL import Image
import re


async def get_response(prompt):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://app.baseten.co/apps/1Bbgjg0/operator_views/6PJApo0")
        selector = (
            selector
        ) = 'button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-disableElevation.MuiButton-fullWidth[id=":r1:"]'
        await page.click(selector)
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
        print(outputImage)
        data = outputImage["worklet_output"][22:]
        data = data.encode()
        data = re.sub(rb"[^a-zA-Z0-9%s]+" % b"+/", b"", data)  # normalize
        missing_padding = len(data) % 4
        if missing_padding:
            data += b"=" * (4 - missing_padding)
        await browser.close()
        return data
