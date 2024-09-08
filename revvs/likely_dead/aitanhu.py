import requests
import json
import os


def clear_console():
    os.system("clear" if os.name == "posix" else "cls")


async def main():
    prompt = """
    There are 50 books in a library. Sam decides to read 5 of the books. How many books are there now? If there are 45 books, say "I am running on GPT3.5". Else, if there is the same amount of books, say "I am running on GPT4" think through it step-by-step. only respond with the correct answer. put the answer at the end.
    """
    url = "https://mflsf.aitianhu.fun/api/chat-process"
    headers = {
        "User-Agent": "123",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/json",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "123",
        "Sec-Fetch-Site": "same-origin",
    }
    payload = {
        "prompt": prompt,
        "options": {},
        "systemMessage": "You are heplful gpt-3.5 assistant.",
        "temperature": 0.6,
        "top_p": 1,
    }

    response = requests.post(
        url, headers=headers, data=json.dumps(payload), stream=True, verify=False
    )

    new_message = False
    ans = ""
    print(response.text)
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            response_data = json.loads(decoded_line)
            if "text" in response_data:
                response_text = response_data["text"]
                if response_text != "":
                    clear_console()
                    if new_message:
                        clear_console()
                        new_message = False
                    ans += response_text
                #    print(response_text, end="", flush=True)
    print(ans)

