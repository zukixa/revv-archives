import aiohttp
import urllib.parse
import asyncio, re
try:
    from valid_reverses.gp import gp
except:
    import valid_reverses.gp as gp
async def send_request(prompt):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://simsimi.vn",
            "Referer": "https://simsimi.vn/",
            "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        data = {"text": urllib.parse.quote(prompt), "lc": "en"}
        url = "https://simsimi.vn/web/simtalk"
        # Define the proxy
        proxy = "http://103.9.206.186:10008"
        pxs = await gp.get_proxy()
        for px in pxs:
            try:
                async with aiohttp.ClientSession(
                    connector=aiohttp.TCPConnector(ssl=False)
                ) as session:
                    async with session.post(
                        url, data=data, proxy=px, timeout=10
                    ) as resp:
                        rj = await resp.json()
                        print(rj)
                        return rj["success"]
            except Exception as e:
                print(f"Issue with simsimi: {str(e)}")
                continue
        return "issue detected, zukijourney invite: https://discord.gg/kvYDFZY7XZ"