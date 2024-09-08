import requests
import re

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from time import time
import base64


def encrypt(secret_key, plain_text):
    secret_key = secret_key.encode(
        "utf-8"
    )  # The key is now encoded to bytes using UTF-8
    cipher = AES.new(secret_key, AES.MODE_ECB)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return base64.b64encode(cipher_text).decode("utf-8")


secret_key = "14487141bvirvvG"


def generate_secret():
    current_time = str(int(time())).encode("utf-8")  # get the current Unix timestamp
    return encrypt(secret_key, current_time)  # encrypt it using the given key


def get_value(prompt):
    ans = ""
    url = "https://api.gptplus.one/chat-process"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "http://bot.gogpt.site",
        "Referer": "http://bot.gogpt.site/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }

    data = {
        "prompt": prompt,
        "options": {},
        "systemMessage": "You are ChatGPT, the version is GPT3.5, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
        "temperature": 0.8,
        "top_p": 1,
        "secret": generate_secret(),
    }
    resp = requests.post(
        url, headers=headers, json=data, verify=False
    )  # stream=True, verify=False)
    # Regular expression pattern to search for the specified substring
    pattern = r'"text":"(.*?)","detail":'
    # Perform the regular expression search
    result = re.findall(pattern, resp.text)
    print(resp.text)
    # Extract and print the desired substring
    if result:
        ans = result[-1]
    return ans


if __name__ == "__main__":
    print(get_value("Hello World"))
