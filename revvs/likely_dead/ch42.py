import requests

import hashlib


import hashlib
import random
import string


def generate_hash(content, hash_length=512):
    encoded = content.encode("utf-8")
    hashed = hashlib.sha256(encoded).hexdigest()
    return hashed[:hash_length]


def shuffle(items, seed):
    random.seed(seed)
    random.shuffle(items)
    return items


def get_charset(length):
    return string.digits + string.ascii_letters[:length]


def rand_int(min_val, max_val, seed=None):
    if seed is not None:
        random.seed(seed)
    return random.randint(min_val, max_val)


content = "some content to hash"
seed = rand_int(0, 1000000)
charset = get_charset(64)
shuffled = shuffle(list(charset), seed)

hash_input = [
    shuffled[rand_int(0, len(shuffled))],
    *[(shuffled[charset.index(c)]) for c in content],
]

hash_str = "".join(hash_input)
hash_value = generate_hash(hash_str, 512)


prompt = "hello!"

# Set the URL for auth check
url_check_auth = "https://cch137.link/api/auth/check"

# Set the headers
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Origin": "https://cch137.link",
    "Referer": "https://cch137.link/c/",
    "Content-Length": "0",
}

# Make the request
response = requests.post(url_check_auth, headers=headers)

# Capture the Set-Cookie header
set_cookie = response.headers["Set-Cookie"]

# Print Set-Cookie
print(set_cookie)

# Set the URL for curva check
url_check_curva = "https://cch137.link/api/curva/check"

# Update headers with the Set-Cookie captured from the first response
headers.update({"Cookie": set_cookie})

# Make the second request
response = requests.post(url_check_curva, headers=headers)

# Capture the Set-Cookie header
set_cookie = response.headers["Set-Cookie"]

# Print Set-Cookie
print(set_cookie)

import requests
import json
import os
import base64
import time


# Function to generate encoded string
def generate_id():
    random_bytes = os.urandom(8)
    encoded_string = base64.b64encode(random_bytes).decode()
    return encoded_string


conv_id = generate_id()

# Set the URL for curva answer
url_curva_answer = "https://cch137.link/api/curva/answer"

# Set the headers
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Cookie": set_cookie,
    "Hash": str((prompt, "MD5")),
    "Origin": "https://cch137.link",
    "Referer": "https://cch137.link/c/",
}

# Set the JSON data for the request
data = {
    "conv": conv_id,
    "messages": [{"role": "user", "content": prompt}],
    "model": "gpt4",
    "temperature": 0.5,
    "t": int(time.time() * 1000),  # Current Unix timestamp in milliseconds
    "tz": 2,
}

# Send the POST request
response = requests.post(url_curva_answer, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    print("Success!")
    print(response.text)
else:
    print("Failed!")

import requests
import json

# Set the URL for curva conv
url_curva_conv = "https://cch137.link/api/curva/conv"

# Set the headers
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Cookie": set_cookie,
    "Content-Length": "78",
    "Origin": "https://cch137.link",
    "Referer": f"https://cch137.link/c/{conv_id}",
}

# Set the JSON data for the request
data = {
    "id": conv_id,
    "name": "",
    "config": "model=gpt4&temperature=0.5&context=true",
}

# Send the PUT request
response = requests.put(url_curva_conv, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    print("Success!")
    print(response.text)
else:
    print("Failed!")
