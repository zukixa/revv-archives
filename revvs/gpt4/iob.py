import aiohttp

headers = {
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': 'Bearer null',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

async def send_request(prompt):
    url = f'https://chat.icoding.ink/api/v1/chatgpt/gpt-4/questions?prompt={aiohttp.helpers.quote(prompt)}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                response.raise_for_status()
                return await response.text()
    except:
        return ""