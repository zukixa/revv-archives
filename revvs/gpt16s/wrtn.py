import aiohttp
import asyncio

async def send_request(prompt):
    # The URL to which the POST request is made
    url = "https://dimension8ai.com/d8-gm-serv/bot/gen_sentence/"

    # Headers as specified in the HTTP request
    headers = {
        "Content-Type": "application/json",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "macOS",
        "Origin": "http://125.227.53.125:10063",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "http://125.227.53.125:10063/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }

    # The data to be sent with the POST request
    data = {
        "usersay": prompt,
        "model_name": "Taiwan-LLaMa2",
        "system_prompt": "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. You are built by NTU Miulab by Yen-Ting Lin for research purpose.",
        "max_new_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 50
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                # Ensure that we catch exceptions related to network errors
                response.raise_for_status()  
                json_response = await response.json()
                return (json_response["text"])
    except:
        return None