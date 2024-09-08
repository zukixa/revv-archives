import httpx, re
import json
import asyncio


async def send_request(prompt: str):
    url = "https://free.chatgpt.org.uk/api/openai/v1/chat/completions"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://free.chatgpt.org.uk",
        "Referer": "https://free.chatgpt.org.uk/",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "stream": True,
        "model": "google-gemini-pro",
        "temperature": 0.5,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "top_p": 1,
    }
    try:
        async with httpx.AsyncClient(timeout=300) as client:
            response = await client.post(url, headers=headers, json=payload)
            print(response.text)
            pattern = re.compile(r"\"content\":\s*\"(.*?)\"")
            matches = pattern.findall(response.text)
            
            # This list will hold unique responses
            unique_responses = []
            ans = ""
            for match in matches:
                # Check if the response already exists before appending
                if match not in unique_responses:
                    unique_responses.append(match)
                    ans += match

            ans = ans.replace("\\n", "\n").replace("\\", '"')
            return ans
    except Exception as e:
        return ""