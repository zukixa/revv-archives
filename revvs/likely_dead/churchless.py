# gpt_free/churchless/churchless.py
import requests
import aiohttp
import json


class CompletionModel:
    @staticmethod
    def create(prompt):
        request_body = {"messages": [{"role": "user", "content": prompt}]}
        headers = {"Content-Type": "application/json"}
        data = {"Authorization": "Bearer ChatGPT-Hackers"}
        res = requests.post(
            "https://free.churchless.tech/v1/chat/completions",
            json=request_body,
            headers=headers,
            data=json.dumps(data),
        )
        return res.json()


class ChatCompletion:
    @staticmethod
    def create(prompt):
        completion = CompletionModel.create(prompt)
        print(completion)
        chat_bot_message = (
            completion.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "No response found")
        )
        return chat_bot_message


class CompletionModel2:
    @staticmethod
    async def create(prompt):
        request_body = {"messages": [{"role": "user", "content": prompt}]}
        headers = {"Content-Type": "application/json"}

        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://free.churchless.tech/v1/chat/completions",
                json=request_body,
                headers=headers,
            ) as res:
                return await res.json()


class ChatCompletion2:
    @staticmethod
    async def create(prompt):
        completion = await CompletionModel2.create(prompt)
        chat_bot_message = (
            completion.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "No response found")
        )
        return chat_bot_message


async def send_request(prompt):
    ans = await ChatCompletion2.create(prompt)
    return ans
