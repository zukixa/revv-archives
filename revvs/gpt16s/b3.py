import aiohttp, re
import random
async def send_request(prompt):
    urls = ['159.69.90.241:8443', '96.9.210.194:2333', '65.108.111.110:8443']# '54.183.92.245:443', '65.109.25.165:443']

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "gpt-3.5-turbo-16k",
        "temperature": 1,
    }

    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        tries = 0
        evaluated_s = None
        while tries < 3:
            try:
                url = random.choice(urls)
                headers["Authority"] = url
                headers["Origin"] = "https://" + url
                headers["Referer"] = "https://" + url

                async with session.post(
                    "https://" + url + "/api/openai/v1/chat/completions",
                    headers=headers,
                    json=data,
                ) as resp:
                    r = await resp.text()
                    matches = re.findall('"content":"(.*?)"', r, re.DOTALL)
                    if matches == []:
                        matches = re.findall('"content": "(.*?)"', r, re.DOTALL)
                    evaluated_s = matches[0].replace("\\n","\n").replace("\\t","\t").replace("\\r","\r").replace("\\","")
                    break
            except Exception as e:
                print(str(e))
                tries += 1
        return evaluated_s