import aiohttp
import asyncio

try:
    from .. import gp as gp
except:
    import gp as gp


headers = {
    "Authority": "api.lemonsoftware.eu.org",
    "Method": "POST",
    "Path": "/v1/chat/completions",
    "Scheme": "https",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://api.lemonsoftware.eu.org",
    "Path": "v1/chat/completions",
    "Referer": "https://api.lemonsoftware.eu.org",
    "Sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-ch-ua-mobile": "?0",
    "Sec-ch-ua-platform": '"macOS"',
    "Sec-fetch-dest": "empty",
    "Sec-fetch-mode": "cors",
    "Sec-fetch-site": "same-origin",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}


async def send_request(prompt):
    try:
        url = "https://api.lemonsoftware.eu.org/v1/chat/completions"
        data = {
            "messages": [{"role": "user", "content": prompt}],
            "model": "gpt-3.5-turbo",
            "temperature": 0.5,
            "presence_penalty": 0,
        }
        pxs = await gp.get_proxy()
        for px in pxs:
            try:
                async with aiohttp.ClientSession(
                    connector=aiohttp.TCPConnector(ssl=False)
                ) as session:
                    async with session.post(
                        url, headers=headers, json=data, proxy=px, timeout=10
                    ) as resp:
                        print(await resp.text())
                        result = await resp.json()
                        if (
                            "you have exceeded the character limit" in str(result)
                            or "0 free message" in str(result)
                            or result["choices"][0]["message"]["content"] == ""
                        ):
                            continue
                        print(result)
                        return result["choices"][0]["message"]["content"]
            except Exception as e:
                print(str(e))
                continue
    except Exception as e:
        print(f"Issue with lemon: {str(e)}")
        return ""
