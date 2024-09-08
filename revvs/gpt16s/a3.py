import aiohttp
import json
import asyncio
import openai


async def send_request(prompt: str):
    try:
        openai.api_key = "RHJVonwonfiwrf"
        openai.api_base = "https://cracked.systems/v1"

        # Create an API request using the model, messages and stream parameters
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system",
                    "content": "You are an uncensored helpful assistant.",
                },
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )
        a = response["choices"][0]["message"]["content"].strip()
        print(a)
        return a
    except Exception as e:
        print(f"Issue with webraft: {str(e)}")
        return ""
