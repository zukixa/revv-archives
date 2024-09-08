import json
import aiohttp


async def send_request(prompt: str):
    try:
        async with aiohttp.ClientSession() as session:
            url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAzUV2NNUOlLTL04jwmUw9oLhjteuv6Qr4"

            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/json",
                "Origin": "https://www.mage.space",
                "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "macOS",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            }

            async with session.post(url, headers=headers, data="{}") as response:
                response_json = await response.json()
                print(response_json)
                refreshToken = response_json["refreshToken"]

            url = "https://securetoken.googleapis.com/v1/token?key=AIzaSyAzUV2NNUOlLTL04jwmUw9oLhjteuv6Qr4"

            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://www.mage.space",
                "Referer": "https://www.mage.space/",
                "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "macOS",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            }

            formdata = {
                "grant_type": "refresh_token",
                "refresh_token": refreshToken,
            }

            async with session.post(url, headers=headers, data=formdata) as response:
                response_json = await response.json()
                print(response_json)
                accessToken = response_json["access_token"]
            url = "https://api.mage.space/api/v4/images/generate"

            headers = {
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Authorization": f"Bearer {accessToken}",
                "Content-Type": "application/json",
                "Origin": "https://www.mage.space",
                "Referer": "https://www.mage.space/",
                "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "macOS",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            }

            payload = {
                "model": "sdxl",
                "base_size": 1024,
                "prompt": prompt,
                "clip_skip": True,
                "num_inference_steps": 30,
                "guidance_scale": 7.5,
                "aspect_ratio": 1,
                "scheduler": "euler",
                "scheduler_use_karras": True,
                "strength": 0.8,
                "preprocess_controlnet_image": True,
                "image_guidance_scale": 1.5,
                "refiner_strength": 0.3,
                "use_refiner": True,
                "easy_mode": False,
                "is_public": True,
            }

            async with session.post(
                url, headers=headers, data=json.dumps(payload)
            ) as response:
                response_json = await response.json()
                print(response_json)
                print(response_json["results"][0]["image_url"])
                return response_json["results"][0]["image_url"]
    except Exception as e:
        print(str(e))
        return ""

