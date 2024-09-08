import re
import json
import aiohttp


# Define the async function
async def send_request(prompt):
    try:
        url = "https://ai.mindtastik.com/aichatbots/php/api.php"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-origin",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Sec-Fetch-Mode": "cors",
            "Origin": "https://ai.mindtastik.com",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "Referer": "https://ai.mindtastik.com/agency/?chat=AI+Chatbot+Pro",
        }

        a = '[{"role":"system","content":"You are ChatGPT, a large language model that knows everything in detail. Answer in as many details as possible."},{"role":"assistant","content":"I am an AI Chatbot that knows almost anything, and I am powered by ChatGPT API & GPT-4. I can help you with any task."},{"role":"user","content":"Hello my name is sam"}]'
        arr = json.loads(a)

        # Replace the desired value
        for item in arr:
            if item["role"] == "user":
                item["content"] = prompt
        # Convert back to a JSON string
        array_chat = json.dumps(arr)
        data = {
            "array_chat": array_chat,
            "employee_name": "AI Chat Pro",
            "model": "gpt-3.5-turbo",
            "temperature": "0.5",
            "frequency_penalty": "0",
            "presence_penalty": "0",
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=data) as response:
                # assert response.status == 200
                res = await response.text()
                print(res)
                pattern = re.compile(r"\"content\":\s*\"(.*?)\"")
                matches = pattern.findall(res)
                ans = ""
                for match in matches:
                    ans += match
                return ans
    except Exception as e:
        print(f"Issue with mindtastik: {str(e)}")
        return ""
