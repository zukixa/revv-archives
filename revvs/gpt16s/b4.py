import aiohttp, string, random, uuid, json, re, asyncio


# A helper function to generate random strings
def random_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


def extract_second_message_text(response):
    # Extract all data lines from the response
    data_lines = re.findall(r"data: (.*)", response)

    # Return None if we have less than 2 data lines
    if len(data_lines) < 2:
        return None

    # Parse the second data line as JSON
    data_json = json.loads(data_lines[-2])

    # Return the "text" field, or None if it doesn't exist
    return data_json.get("text")


async def send_request(prompt: str):
    # Generate random values for the fields
    random_value = random_string(10) + "@gmail.com"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://multibotapp.com",
        "Referer": "https://multibotapp.com/register",
    }

    data = {
        "name": random_value,
        "username": random_value,
        "email": random_value,
        "password": random_value,
        "confirm_password": random_value,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://multibotapp.com/api/auth/register",
            headers=headers,
            json=data,
        ) as response:
            response_data = await response.text()
            print(response_data)
            set_cookie_value = response.headers["Set-Cookie"]
            print("Set-Cookie:", set_cookie_value)

            if response.status != 200:
                print("Registration request failed.")
                return

            headers["Cookie"] = set_cookie_value
            headers["Authorization"] = (
                "Bearer " + set_cookie_value.split("=")[1].split(";")[0]
            )
            headers.pop("Referer")
            headers["Referer"] = "https://multibotapp.com/chat/new"

            data = {
                "sender": "User",
                "text": prompt,
                "current": True,
                "isCreatedByUser": True,
                "parentMessageId": "00000000-0000-0000-0000-000000000000",
                "conversationId": None,
                "messageId": str(uuid.uuid4()),
                "error": False,
                "generation": "",
                "responseMessageId": None,
                "overrideParentMessageId": None,
                "endpoint": "openAI",
                "model": "openai/gpt-4-1106-preview",
                "chatGptLabel": None,
                "promptPrefix": None,
                "temperature": 0.5,
                "top_p": 1,
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "token": None,
                "isContinued": False,
            }

            async with session.post(
                "https://multibotapp.com/api/ask/openAI",
                headers=headers,
                json=data,
            ) as response:
                print(await response.text())
                final_text = extract_second_message_text(await response.text())
                print(final_text)
                return final_text if final_text else ""

