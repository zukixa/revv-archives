import aiohttp
import asyncio
import uuid
import json
import time

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://zoo.replicate.dev",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}


async def fetch_prediction(model, prompt):
    data = {
        "prompt": prompt,
        "version": "98d6bab2dd21e4ffc4cc626420ab4f24b99ec60728c5d835ff9c3439396aca45",
        "source": "replicate",
        "model": model,
        "anon_id": str(uuid.uuid4()),
        "submission_id": str(uuid.uuid4()),
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://zoo.replicate.dev/api/predictions",
            headers=headers,
            data=json.dumps(data),
        ) as post_response:
            text = await post_response.text()
            post_response_json = json.loads(text)
        print("passed")
        print(post_response_json)
        tries = 0
        while True:
            tries += 1
            async with session.get(
                f"https://zoo.replicate.dev/api/predictions/{post_response_json['id']}",
                headers=headers,
            ) as get_response:
                tx = await get_response.text()
                js = json.loads(tx)
                if js["status"] == "succeeded":
                    return f"https://ennwjiitmiqwdrgxkevm.supabase.co/storage/v1/object/public/images/public/{post_response_json['id']}.png"
                #   if "output" in get_response_json:
                #      print(get_response_json["output"])
                #     if model == "deepfloyd-if":
                #        return get_response_json["output"]
                #   return get_response_json["output"][0]
                if tries > 45:
                    return ""
            await asyncio.sleep(2)
