import aiohttp
import ssl, json
import uuid

async def send_request(prompt):
    try:
        async with aiohttp.ClientSession() as session:
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            
            url = "https://45.83.205.173/settings"
            headers = {
                "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "macOS",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Origin": "https://45.83.205.173",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://45.83.205.173/settings/mistral-medium",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
            }
            payload = {
                "searchEnabled": True,
                "ethicsModalAccepted": True,
                "ethicsModalAcceptedAt": None,
                "activeModel": "mistral-medium",
                "hideEmojiOnSidebar": False,
                "shareConversationsWithModelAuthors": True,
                "customPrompts": {
                    "mistral-tiny": "",
                    "mistral-medium": ""
                },
                "assistants": [],
                "recentlySaved": True
            }
            
            # First POST request to update settings
            async with session.post(url, json=payload, headers=headers, ssl=ssl_context) as response:
                if 'Set-Cookie' in response.headers:
                    cookie = response.headers['Set-Cookie'].split(" ")[0]
                else:
                    print('No Set-Cookie header in response')
                    return None
            
            # Update headers with received cookie
            headers["Cookie"] = cookie
            
            # Define POST request to initiate conversation
            post_url = "https://45.83.205.173/conversation"
            post_data = {
                "model": "mistral-medium",
                "preprompt": ""
            }
            
            # Send the POST request to initiate conversation
            async with session.post(post_url, headers=headers, json=post_data, ssl=ssl_context) as post_response:
                post_response_data = await post_response.json()
                cvid = post_response_data["conversationId"]
            
            # Define the URL and payload for sending inputs in conversation
            url = f"https://45.83.205.173/conversation/{cvid}"
            headers["Referer"] = f"https://45.83.205.173/conversation/{cvid}"
            payload = {
                "inputs": prompt,
                "id": str(uuid.uuid4()),
                "is_retry": False,
                "is_continue": False,
                "web_search": False,
                "files": []
            }
            
            # Send the inputs in conversation
            async with session.post(url, headers=headers, json=payload, ssl=ssl_context) as response:
                response_data = await response.text()
                lines = response_data.strip().split("\n")
                ans = ""
                for line in lines:
                    ans += (json.loads(line)).get("token","")
                return ans
    except:
        return ""    