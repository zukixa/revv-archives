import secrets
import string
import random
import aiohttp

try:
    from .. import gp as gp
except:
    import gp as gp


async def send_request(prompt: str) -> str:
    id_length = 32
    generated_id = secrets.token_hex(id_length)

    length = 12
    charset = string.ascii_uppercase + string.ascii_lowercase + string.digits
    sesh_id = "".join(random.choice(charset) for _ in range(length))

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Cookie": f"fingerprint={generated_id}",
        "Referer": "https://www.zaimaai.cn/",
        "Content-Type": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "Origin": "https://www.zaimaai.cn",
        "DNT": "1",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
    }

    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI. Knowledge cutoff: 2021-09 Current model: GPT-4 Current time: 8/12/2023, 2:10:02 AM",
            },
            {"role": "user", "content": prompt.strip()},
        ],
        "is_sse": True,
        "service": "openaigpt",
        "model": "gpt-3.5-turbo",
        "temperature": 0.5,
        "presence_penalty": 0,
        "visitor_id": generated_id,
        "session_id": sesh_id,
        "app_name": "zaimaai_web",
        "prompt": [
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI. Knowledge cutoff: 2021-09 Current model: GPT-4 Current time: 8/12/2023, 2:10:02 AM",
            },
            {"role": "user", "content": prompt.strip()},
        ],
    }
    pxs = await gp.get_proxy()
    for px in pxs:
        try:
            async with aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(ssl=False)
            ) as session:
                async with session.post(
                    "https://www.zaimaai.cn/api/zaimaai/chat",
                    headers=headers,
                    json=data,
                    proxy=px,
                    timeout=10,
                ) as resp:
                    text = await resp.text()
                    if '"code":"' in text or "text is too long" in text:
                        print(text)
                        continue
                    print(text)
            return text
        except Exception as e:
            print(f"Issue with zaimaa: {str(e)}")
            continue
    return ""
