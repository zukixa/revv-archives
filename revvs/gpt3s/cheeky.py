import aiohttp, re
import asyncio
import json


async def send_request(prompt):
    try:
        url = "https://free.aitom.cc/api/openai/v1/chat/completions"

        headers = {
            "Accept": "text/event-stream",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Origin": "https://free.aitom.cc",
            "Referer": "https://free.aitom.cc/",
            "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "stream": True,
            "model": "gpt-3.5-turbo",
            "temperature": 0.5,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "top_p": 1,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers=headers, data=json.dumps(payload)
            ) as response:
                response_text = await response.text()

                pattern = re.compile(r"\"content\":\s*\"(.*?)\"")
                matches = pattern.findall(response_text)
                ans = ""
                for match in matches:
                    ans += match
                ans = ans.replace("\\n", "\n").replace("\\", '"')
                print(ans)
                return ans
    except Exception as e:
        print(f"Issue with cheeky: {str(e)}")
        return ""



