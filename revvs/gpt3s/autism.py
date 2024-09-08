import aiohttp
import asyncio
import random, re
import string
import json


def random_string(length):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


async def fetch(session, url, headers, prompt):
    data = {"input": prompt, "inputHistory": [], "outputHistory": []}
    async with session.post(url, headers=headers, data=json.dumps(data)) as response:
        return await response.text()


async def send_request(prompt):
    try:
        headers = {
            "Accept": "text/event-stream",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Flag-Real-Time-Data": "false",
            "Origin": "https://koala.sh",
            "Referer": "https://koala.sh/chat",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            #  "Visitor-Id": random_string(15)
        }
        url = "https://koala.sh/api/usage/"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                js = await response.json()
                print(js)
                headers["Visitor-Id"] = js["key"].split("visitorId:")[1]
            html = await fetch(session, "https://koala.sh/api/gpt/", headers, prompt)
            pattern = re.compile(r'data: "(.*?)"')
            matches = pattern.findall(html)
            concatenated = "".join(matches)
            final = concatenated.replace("\\n", "\n")
            print(final)
            return final
    except Exception as e:
        print(f"Issue with autism: {str(e)}")
        return ""


#asyncio.run(send_request("hi"))
