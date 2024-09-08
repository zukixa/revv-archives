import aiohttp
import requests, time, re, pymailtm, string, random
from pymailtm.pymailtm import MailTm
from TempMail import TempMail
import asyncio
import aiohttp
import asyncio
import aiofiles
import json


def generate_random_string(length):
    letters = string.ascii_letters  # Get all the ASCII letters
    result_str = "".join(
        random.choice(letters) for _ in range(length)
    )  # Choose 5 at random
    return result_str


# Define the URL
url = "https://www.papayagpt.com/app/ai/message/send"


async def generate_cookie():
    async with aiohttp.ClientSession() as session:
        r = await session.get("https://www.papayagpt.com/app/user/register")
        magic_cookie = r.cookies.get("PHPSID")
        await asyncio.sleep(2)

        url = "https://www.papayagpt.com/app/user/captcha/email/register"

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://www.papayagpt.com",
            "Referer": "https://www.papayagpt.com/app/user/register",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": f"PHPSID={magic_cookie.value}",
        }

        mailtm = MailTm()
        acc = None
        while not acc:
            await asyncio.sleep(2)
            try:
                acc = mailtm.get_account()
            except:
                acc = None
        print(acc.address)  # this is the email i need to input in the actual thing
        email = str(acc.address)  # Please replace None with your email

        data = {"email": email}
        response = await session.post(url, headers=headers, data=data)

        # Please remember to replace synchronus MailTm library pymailtm with asynchronous library to avoid blocking IO
        msg = acc.wait_for_message()
        verification_code = re.search(
            r'<div style="text-align: center; font-size: 36px; margin-top: 20px; line-height: 44px;">(.*?)</div>',
            str(msg),
        )
        code = verification_code.group(1)
        print("found code")
        print(code)
        #   code = None  # After you extract the code, replace None with the code

        url = "https://www.papayagpt.com/app/user/register"

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://www.papayagpt.com",
            "Referer": "https://www.papayagpt.com/app/user/register",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": f"PHPSID={magic_cookie.value}",
        }

        data = {
            "email": email,
            "username": generate_random_string(10),
            "password": generate_random_string(10),
            "mobile_code": code,
        }
        await asyncio.sleep(3)
        response = await session.post(url, headers=headers, data=data)
        print(await response.text())
        print(magic_cookie.value)
        await asyncio.sleep(5)
        async with aiofiles.open(
            "/home/valid_reverses/papaya_cookie.json", mode="w"
        ) as f:
            await f.write(json.dumps({"magic_cookie": magic_cookie.value}))
        return magic_cookie.value


async def generate_cookie_and_store():
    async with aiohttp.ClientSession() as session:
        r = await session.get("https://www.papayagpt.com/app/user/register")
        # ... your other steps go here...
        magic_cookie = r.cookies.get("Papaya_UwU")
        print(magic_cookie)
        await asyncio.sleep(2)
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://www.papayagpt.com",
            "Referer": "https://www.papayagpt.com/app/user/register",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": f"Papaya_UWU={magic_cookie.value}",
        }

        tm = TempMail()
        inb = TempMail.generateInbox(tm)

        emails = None
        url = "https://www.papayagpt.com/app/user/captcha/email/register"
        print(inb.address)  # this is the email i need to input in the actual thing
        email = str(inb.address)
        data = {"email": email}
        response = await session.post(url, headers=headers, data=data)
        tries = 0
        flag = False
        # emails = TempMail.getEmails(tm, inbox=inb)
        while not flag and tries < 20:
            await asyncio.sleep(2)
            tries += 1
            emails = TempMail.getEmails(tm, inbox=inb)
            if emails:
                break
        msg = str(emails[0].html)
        verification_code = re.search(
            r'<div style="text-align: center; font-size: 36px; margin-top: 20px; line-height: 44px;">(.*?)</div>',
            str(msg),
        )

        code = verification_code.group(1)
        url = "https://www.papayagpt.com/app/user/register"
        print(magic_cookie)
        print(magic_cookie.value)
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://www.papayagpt.com",
            "Referer": "https://www.papayagpt.com/app/user/register",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": f"PHPSID={magic_cookie.value}",
        }

        data = {
            "email": email,
            "username": "@" + generate_random_string(10),
            "password": "@" + generate_random_string(10),
            "mobile_code": code,
        }
        # The second to last POST request where you grasp the magic_cookie
        res = await session.post(url=url, headers=headers, data=data)
        # Grasping the magic_cookie from the response
        # Storing magic_cookie in a JSON file
        async with aiofiles.open(
            "/home/valid_reverses/papaya_cookie.json", mode="w"
        ) as f:
            await f.write(json.dumps({"magic_cookie": magic_cookie.value}))
        print(magic_cookie.value)
        return magic_cookie.value


async def send_request(prompt):
    with open(
        "/home/valid_reverses/papaya_cookie.json", "r"
    ) as f:
        data = json.load(f)

    # Access the cookie
    magic_cookie = data["magic_cookie"]
    # Define the headers
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": f"Papaya_UwU={magic_cookie}",
        "Origin": "https://www.papayagpt.com",
        "Referer": "https://www.papayagpt.com/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    # Define the POST body data in dictionary form
    data = {
        "rolePrompt": "",
        "roleId": "1",
        "model": "gpt-4",
        "prompt": prompt,
    }
    tries = 0
    while tries < 5:
        tries += 1
        # Use aiohttp's ClientSession to manage connection pooling
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url,
                headers=headers,
                data=data,
            ) as res:
                tx = await res.text()
                print(tx)
                if (
                    "error" in tx
                    or "register to use" in tx
                    or "violation and has been banned" in tx
                ):
                    magic_cookie = await generate_cookie_and_store()
                    headers["Cookie"] = f"Papaya_UwU={magic_cookie}"
                    continue
                pattern = re.compile(r"\"content\":\s*\"(.*?)\"")
                matches = pattern.findall(tx)
                ans = ""
                for match in matches:
                    ans += match
                print(ans)
                return ans

