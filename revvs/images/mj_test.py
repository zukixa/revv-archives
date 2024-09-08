import asyncio
import aiohttp
import json


async def submit_and_fetch(prompt, u):
    mj_api = ""
    url_s = ""
    url_f = ""
    headers = ""
    payload = ""
    u = u[1:]
    if "246" in u:
        mj_api = "OTP"
        url_s = "http://203.186.246.162:8090/mj-api/mj/submit/imagine"
        url_f = "http://203.186.246.162:8090/mj-api/mj/task/{id}/fetch"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "203.186.246.162:8090",
            "Mj-Api-Secret": mj_api,
            "Referer": "http://203.186.246.162:8090/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }
        payload = {"prompt": prompt}
        print(url_s)
        async with aiohttp.ClientSession() as session:
            # Post the prompt and get the task id
            async with session.post(url_s, headers=headers, json=payload) as response:
                response_dict = await response.json()
                print(response_dict)
                if response_dict["code"] == 1:
                    task_id = response_dict["result"]
                else:
                    print(f'Error: {response_dict["description"]}')
                    return None

            # Fetch the task until its state is either 'SUCCESS' or 'FAILURE'
            while True:
                async with session.get(
                    url_f.format(id=task_id), headers=headers
                ) as response:
                    task_info = await response.json()
                    if task_info["status"] in ["SUCCESS", "FAILURE"]:
                        if task_info["status"] == "SUCCESS":
                            a = task_info.get("imageUrl")
                            print(a)
                            return a
                        else:
                            return None
                # not to hammer the server, wait for a brief period of time
                await asyncio.sleep(1)

    elif "218" in u:
        url_s = "http://45.76.218.50:3000/api/midjourney/task/submit"
        url_f = "http://45.76.218.50:3000/api/midjourney/task/status/{id}"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Referer": "http://45.76.218.50:3000/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }
        payload = {
            "prompt": prompt,
            "images": [],
            "action": "IMAGINE",
            "cmd": None,
            "index": None,
            "taskId": None,
        }
        print(url_s)
        async with aiohttp.ClientSession() as session:
            # Post the prompt and get the task id
            async with session.post(url_s, headers=headers, json=payload) as response:
                response_dict = await response.json()
                print(response_dict)
                if response_dict["taskId"]:
                    task_id = response_dict["taskId"]
                else:
                    print(f'Error: {response_dict["description"]}')
                    return None

            # Fetch the task until its state is either 'SUCCESS' or 'FAILURE'
            while True:
                async with session.get(
                    url_f.format(id=task_id), headers=headers
                ) as response:
                    task_info = await response.json()
                    print(task_info)
                    if task_info["status"] in ["SUCCESS", "FAILURE"]:
                        if task_info["status"] == "SUCCESS":
                            try:
                                a = task_info["uri"]
                            except:
                                return ""
                            print(a)
                            return a
                        else:
                            return None
                # not to hammer the server, wait for a brief period of time
                await asyncio.sleep(1)
