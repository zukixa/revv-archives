import aiohttp
import asyncio

# define headers
headers = {
    "Accept": "application/json",
 #   "Accept-Encoding": "gzip, deflate, br",
 #   "Accept-Language": "en-US,en;q=0.9",
 #   "Origin": "https://anonchatgpt.com",
 #   "Referer": "https://anonchatgpt.com/",
 #   "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
 #   "Sec-Ch-Ua-Mobile": "?0",
 #   "Sec-Ch-Ua-Platform": '"macOS"',
 #   "Sec-Fetch-Dest": "empty",
 #   "Sec-Fetch-Mode": "cors",
 #   "Sec-Fetch-Site": "same-site",
  #  "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    "Cookie": "session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiI0YTA2ZWZmNy01YzI4LTRiNGMtYTcyMS0yNGU5MzE1ZTI0MWMiLCJ2ZXJpZmllZEF0IjoxNjk5MDkxNzkyNDQxLCJpYXQiOjE2OTkwOTE3OTJ9.d7e51SOReTxgrhS2kGzeUf7idj7Bv1_sYZZGIcbCzQA;"
}

# define the GET request as a coroutine
async def send_request(prompt):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.anonchatgpt.com/query", params={"queryText":prompt}, headers=headers) as resp:
                js = await resp.json()
                print(js)
                print(js["responseText"])
                return js["responseText"]
    except Exception as e:
        print(f"Issue with anonchat: {str(e)}")
        return ""
