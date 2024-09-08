import requests

messages = []


def sendMessage(content):
    messages.append({"role": "user", "content": content})
    chat = requests.post(
        "https://ai.mcbbs.gq/api/openai/v1/chat/completions",
        headers={
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            "sec-ch-ua-platform": '"Windows"',
        },
        json={
            "messages": messages,
            "model": "gpt-3.5-turbo",
            "temperature": 0,
            "presence_penalty": 2,
        },
        verify=False,
    )
    print(chat.text)
    result = chat.json()["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": result})
    print("Got response: " + result)


sendMessage("What is 1+1?")
