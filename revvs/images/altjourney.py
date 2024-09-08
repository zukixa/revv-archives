import aiohttp
import asyncio
import random
import json

try:
    from . import mj_test as mj
except:
    import mj_test as mj


valid_urls_old = [
    "http://122.233.166.88:27716/"
    # "http://47.254.24.47:3001",
    # "http://47.242.121.51:3000/",
    # "http://154.40.59.42:3000",
    #   "http://150.230.199.41:3000/",
    #  "http://173.242.120.185:80",
    # "http://173.242.120.185:3000",
    # "http://119.129.236.38:3000/",
    #   "http://chat-gpt-midjourney-lac-theta.vercel.app/",
    #  "mj",
]
valid_urls = [
    #  ("http://119.8.184.19:3000/", "123456"),
    #  ("http://45.76.218.50:3000/", "123456"),
    #  ("http://154.40.59.42:3000/", "123456"),
    #  ("http://190.92.246.189:3000/", "123456"),
    #  ("http://122.233.166.88:27716/", "123456"),
    ("http://165.154.57.78:3010/", "123456"),
 #   ("chttp://45.76.218.50:3000/", "1234"),
  #  ("chttp://203.186.246.162:8090", ""),
]


async def fetch_image(prompt):
    uple = random.choice(valid_urls)
    u = uple[0]
    if "c" in u:
        return await mj.submit_and_fetch(prompt, u)
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": f"Bearer ak-{uple[1]}",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": f"{u}",
        "Referer": f"{u}/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    if "chat-gpt-midjourney" in u:
        headers["Authorization"] = "Bearer ak-123"
   # if "218" in u:
    prompt += " --relax"
    async with aiohttp.ClientSession() as session:
        url = f"{u}/api/midjourney/mj/submit/imagine"
        data = {"prompt": prompt, "base64": None}

        async with session.post(url, headers=headers, json=data) as response:
            result = await response.json()
            result_id = result["result"]

        status = "IN_PROGRESS"
        while status == "IN_PROGRESS":
            await asyncio.sleep(4)
            url = f"{u}/api/midjourney/mj/task/{result_id}/fetch"

            async with session.get(url, headers=headers) as response:
                result = await response.json()

                if result["status"] == "SUCCESS" or result["status"] == "FAILURE":
                    temp_result = result.get("imageUrl")
                    break

    #      url = f"{u}/api/midjourney/mj/submit/change"
    #      data = {"action": "UPSCALE", "index": 1, "taskId": f"{result_id}"}
    #
    #       async with session.post(url, headers=headers, json=data) as response:
    #          result = await response.json()
    #         result_id = result["result"]
    #
    #       status = "IN_PROGRESS"
    #      while status == "IN_PROGRESS":
    #         await asyncio.sleep(4)
    #        url = f"{u}/api/midjourney/mj/task/{result_id}/fetch"

    #       async with session.get(url, headers=headers) as response:
    #          result = await response.json()

    #         if result["status"] == "SUCCESS":
    #            temp_result = result["imageUrl"]
    #           break

    return temp_result


