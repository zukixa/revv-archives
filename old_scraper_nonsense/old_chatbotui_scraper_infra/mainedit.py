import json
import requests
import concurrent.futures

chatbotui_test_data = json.dumps(
    {
        "model": {
            "id": "gpt-3.5-turbo-16k",
            "name": "GPT-3.5-TURBO-16K",
            #   "maxLength": 12000,
            #   "tokenLimit": 4000,
        },
        "messages": [
            {
                "role": "user",
                "content": "SAY THE LETTER B. ONLY SAY THE LETTER B, NOTHING ELSE. JUST SAY THE LETTER B. THIS IS A TEST, ONLY SAY THE LETTER B.",
            }
        ],
        "key": "",
        "prompt": "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
    }
)


def check_url(url):
    try:
        r = requests.post(
            f"https://{url}/api/chat",
            timeout=30,
            data=chatbotui_test_data,
            verify=False,
        )
        if r.text and (r.text[0] == "B"):  # or "api" in r.text):
            print(r.text)
            return url
    except Exception as e:
        print(f"Issue with {url}: {str(e)}")


urls_found =[]#= ['221.153.252.68:443', '143.64.43.104:3007', '198.46.190.193:443']
with open("/home/Free-ChatGPT-ChatBot/api-chu-ip.txt", "r") as f:
    urls_found = [line.strip() for line in f]

valid_urls = []

with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    future_to_url = {executor.submit(check_url, url): url for url in urls_found}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            result = future.result()
        except Exception as exc:
            print(f"{url} generated an exception: {exc}")
        else:
            if result is not None:
                valid_urls.append(result)

print("Valid URLs:")
print(valid_urls)
