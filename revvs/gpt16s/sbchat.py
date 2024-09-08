import aiohttp
import asyncio
import json, re


async def send_request(prompt):
    try:
        session_url = "https://chat.sb-chat.com/setsession.php"
        stream_url = f"https://chat.sb-chat.com/stream.php?user=BbhEKf7G49472054"

        session_headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://chat.sb-chat.com",
            "Referer": "https://chat.sb-chat.com/index.php?i=1005",
            "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

        stream_headers = {
            "Accept": "text/event-stream",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Referer": "https://chat.sb-chat.com/index.php?i=1005",
            "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }

        session_payload = {
            "message": prompt,
            "model": "13",
            "role": "",
            "context": "[]",
            "user": "BbhEKf7G49472054",
            "conversationid": "",
        }

        async with aiohttp.ClientSession(headers=session_headers) as session:
            async with session.post(
                session_url, data=session_payload
            ) as session_response:
                if session_response.status == 200:
                    async with session.get(
                        stream_url, headers=stream_headers
                    ) as stream_response:
                        if stream_response.status == 200:
                            response_text = await stream_response.text()
                            pattern = re.compile(r"\"content\":\s*\"(.*?)\"")
                            matches = pattern.findall(response_text)
                            ans = ""
                            for match in matches:
                                ans += match
                            ans = ans.replace("\\n", "\n").replace("\\", '"')
                            return ans
    except Exception as e:
        print(f"Issue with sb: {str(e)}")
        return ""
