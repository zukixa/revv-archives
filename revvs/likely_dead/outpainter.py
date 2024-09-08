import uuid, requests, time

image_data = None
prompt = "balls"
url = "https://outpainter.app/api/prediction"
headers = {
    "Accept": "/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "text/plain;charset=UTF-8",
    "Origin": "https://outpainter.app",
    "Referer": "https://outpainter.app/",
    "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
id = str(uuid.uuid4())
ws_key = "93c5d2bd-b309-4e48-b5c2-89ecf1332950"
mask = None
with open("/home/valid_reverses/mask.txt", "r") as file:
    # Replace 'filename.txt' with your file's name
    mask = file.readline().strip()
    # The strip function removes the newline character at the end of the line
    data = {
        "ws_key": id,
        "input": {
            "image": image_data,
            "mask": mask,
            "prompt": prompt,
            "guidance_scale": 7.5,
            "num_inference_steps": 20,
            "num_outputs": 1,
        },
    }

response = requests.post(url, headers=headers, json=data)
print("resp:")
print(response.json())
webhook_url = response.json()["webhook"]
while True:
    response_webhook = requests.get(webhook_url)
    if response_webhook.json()["status"] == "succeeded":
        output_url = response_webhook.json()["url"][0]
        print("Output URL: ", output_url)
        break
    else:
        print("Status: ", response_webhook.json()["status"])
        time.sleep(5)  # Wait for 5 seconds before the next request

        headers = {
            "Sec-Websocket-Key": "J9C2whGd3fILw4InUKaKtw==",
            # other headers...
        }

websocket_key = headers.get("Sec-Websocket-Key")
