import httpx
import json


async def send_request(prompt):
    try:
        url = "https://feel-gpt.top/chat"

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://feel-gpt.top",
            "Referer": "https://feel-gpt.top/chat",
            "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }

        form_fields = {
            "model": (None, "gpt-3.5-turbo"),
            "max_tokens": (None, "2048"),
            "top_p": (None, "1"),
            "temperature": (None, "0.5"),
            "presence_penalty": (None, "0"),
            "frequency_penalty": (None, "0"),
            "messages": (None, json.dumps([{"role": "user", "content": prompt}])),
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, files=form_fields)
            print(response.text)
            if response.status_code == 200:
                return response.text
            else:
                return ""
    except Exception as e:
        print(f"Issue with feelgpt3: {str(e)}")
        return ""
