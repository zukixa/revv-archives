import httpx
import json, re
import asyncio


async def send_request(prompt):
    # Specify the URL
    url = "https://bot9.bp2.skybyte.me/api/chat-process"

    # Specify the headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://bot9.bp2.skybyte.me",
        "Referer": "https://bot9.bp2.skybyte.me/",
        "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }

    # Specify the data to be sent in JSON format
    data = {
        "prompt": prompt,
        "options": {},
        "systemMessage": "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
        "temperature": 0.5,
        "top_p": 1,
    }

    # Convert python dictionary to json
    json_data = json.dumps(data)

    # Make the POST request
    tries = 0
    while tries < 5:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, headers=headers, data=json_data)
                break
        except:
            await asyncio.sleep(2)
            tries += 1
    if tries == 5:
        return ""
    res = response.text
    #  print(res)
    pattern = re.compile(r"\"text\":\s*\"(.*?)\"")
    matches = pattern.findall(res)
    ans = ""
    for match in matches:
        ans = match
    ans = repr(ans)
    print(ans)
    return ans[1:-1]


