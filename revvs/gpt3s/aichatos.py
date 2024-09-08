import aiohttp
import asyncio
import time

try:
    from .. import gp as gp
except:
    import gp as gp


async def send_request(prompt):
    try:
        ans = ""
        url = "https://api.binjie.fun/api/generateStream"
        headers = {
            "Host": "api.binjie.fun",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Referer": "https://chat2.aichatos.top/",
            "Origin": "https://chat2.aichatos.top",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Connection": "keep-alive",
            "TE": "trailers",
        }

        data = {
            "prompt": prompt,
            "userId": "",
            "network": True,
            "system": "Answer in English.",
            "withoutContext": False,
            "stream": False,
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
                        resp.raise_for_status()
                        text = await resp.text()
                        ans = text.encode("utf-8-sig").decode("utf-8")
                        print(ans)
                        return ans
            except Exception as e:
                print(f"Issue with Aichatos: {str(e)}")
                continue
    except Exception as e:
        print(f"Issue with Aichatos: {str(e)}")
        return ""

