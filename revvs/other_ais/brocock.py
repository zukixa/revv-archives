import time
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from binascii import b2a_hex
import aiohttp
import json
import asyncio


async def make_request(prompt: str):
    # Getting the current timestamp & converting it to string
    current_time = str(int(time.time()))

    # Defining the secret key
    secret_key = b"UkXp2s5v8y/B?D(G+KbPeShVmYq3t6w9"

    # Defining the AES cipher object
    cipher = AES.new(secret_key, AES.MODE_ECB)

    # Encrypting the data
    ciphertext = cipher.encrypt(pad(current_time.encode(), AES.block_size))

    # Converting ciphertext to hex
    ciphertext_hex = b2a_hex(ciphertext)

    # Define the URL
    url = "https://bratgpt.com/api/generate"

    # Define the request headers
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://bratgpt.com",
        "referer": "https://bratgpt.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "token": ciphertext_hex.decode(),
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }

    # Define the request data
    data = {"prompt": [{"role": "user", "content": prompt}]}

    # Make the POST request
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            print(response.status)
            print(await response.text())

