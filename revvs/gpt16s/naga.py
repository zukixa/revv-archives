import aiohttp
import json
import random


async def send_request(prompt):
    try:
        keys = [
            "houefouwehoNIWemOIRVyNworiNUVOIuwOIFN"
        ]
        key = random.choice(keys)
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
            "Origin": "https://chat.ylokh.xyz",
            "Referer": "https://chat.ylokh.xyz/",
            "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        }
        messages = [
            {"role": "user", "content": prompt},
        ]

        payload = {
            "messages": messages,
            "model": "gpt-3.5-turbo-1106",
            "temperature": 0.5,
            "presence_penalty": 0,
            "top_p": 1,
            "frequency_penalty": 0,
            "allow_fallback": False,
            "stream": False,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url="https://api.naga.ac/v1/chat/completions",
                headers=headers,
                data=json.dumps(payload),
            ) as response:
                js = await response.json()
                print(js)
                if "error occurred" in str(js).lower():
                    return ""
                return js["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Issue with naga: {str(e)}")
        return ""
