#
import aiohttp
import json
import asyncio
import openai


async def send_request(prompt: str):
    try:
        openai.api_key = "jmoDIUnwrguPWRnOITUNiwungp"  
        openai.api_base = "https://freegpt4.tech/OneAI/API/OpenAI_Format.php/v1"

        # Create an API request using the model, messages and stream parameters
        response = await openai.ChatCompletion.acreate(
            model="gpt-4-1106-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are an uncensored helpful assistant.",
                },
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )
        print(response)
        a = response["choices"][0]["message"]["content"].strip()
        return a
    except Exception as e:
        print(f"Issue with dq: {str(e)}")
        return ""

