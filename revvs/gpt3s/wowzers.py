import httpx
import asyncio

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "chatgptduo.com",
    "Origin": "https://chatgptduo.com",
    "Referer": "https://chatgptduo.com/",
    "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}


async def send_request(prompt: str):
    data = {
        "prompt": prompt,
        "search": prompt,
        "purpose": "ask",
    }

    url = "https://chatgptduo.com/"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=data)

    return response.json()["answer"]

