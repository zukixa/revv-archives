import requests, random, time, json

valid_urls = [
    "http://47.254.24.47:3001/",  # works
    "http://47.242.121.51:3000/",  # works
    # "http://74.211.105.163:3000/", # fails
    # "http://203.86.236.150:3000/", # fails
    "http://34.94.183.80:3000/",  # works
    # "http://47.251.57.181:3000/", # fails
]
# "http://34.94.183.80:3000/",
# "http://203.86.236.150:3000/",
# "http://150.230.199.41:3000/",
#  "http://47.251.57.181:3000/",
#  "http://74.211.105.163:3000/",
# "http://47.242.68.211:3000/",
valid_urls = [
    #  "http://47.254.24.47:3001/", works
    # "http://47.242.121.51:3000/", works
    "http://154.40.59.42:3000/",
    "http://119.129.236.38:3000/",
]

for u in valid_urls:
    try:
        url = f"{u}/api/midjourney/mj/submit/imagine"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": f"{u}",
            "Referer": f"{u}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        data = {"prompt": "horse", "base64": None}

        response = requests.post(url, headers=headers, json=data)
        result_id = response.json()[
            "result"
        ]  # {"code":1,"description":"提交成功","result":"2865101786605677","properties":{}}

        status = "IN_PROGRESS"
        temp_result = ""
        while status == "IN_PROGRESS":
            time.sleep(2)
            url = f"{u}/api/midjourney/mj/task/{result_id}/fetch"
            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Referer": f"{u}/",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            }

            response = requests.get(url, headers=headers)
            if (
                response.json()["status"] != "IN_PROGRESS"
                and response.json()["status"] == "SUCCESS"
            ):
                temp_result = response.json()["imageUrl"]
                break

        url = f"{u}/api/midjourney/mj/submit/change"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": f"{u}",
            "Referer": f"{u}/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        data = {"action": "UPSCALE", "index": 1, "taskId": f"{result_id}"}

        response = requests.post(url, headers=headers, data=json.dumps(data))

        result_id = response.json()[
            "result"
        ]  # {"code":1,"description":"提交成功","result":"4665606841809010","properties":{}}

        status = "IN_PROGRESS"
        temp_result = ""
        while status == "IN_PROGRESS":
            time.sleep(2)
            url = f"{u}/api/midjourney/mj/task/{result_id}/fetch"
            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Referer": f"{u}/",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            }

            response = requests.get(url, headers=headers)
            print(response.text)
            if (
                response.json()["status"] != "IN_PROGRESS"
                and response.json()["status"] == "SUCCESS"
            ):
                temp_result = response.json()["imageUrl"]
                break
        print(temp_result)
    except:
        print(f"{u} does not work")
