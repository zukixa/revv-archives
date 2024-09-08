import httpx
import asyncio
from urllib.parse import quote_plus


async def send_request(question: str):
    try:
        # Convert spaces and special characters in the question to be URL-friendly
        formatted_question = quote_plus(question)

        # Append the question to the URL
        request_url = (
            "https://hercai.onrender.com/v2/hercai?question=" + formatted_question
        )

        # Perform the GET request
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.get(request_url)

        # Return server's response
        return response.json()["reply"]
    except Exception as e:
        print(f"Issue with turkiye: {str(e)}")
        return ""

