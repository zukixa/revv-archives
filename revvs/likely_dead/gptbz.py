from json import dumps, loads
import base64
import io
import numpy as np
from PIL import Image
import textract
import websockets
import asyncio
import cv2
import pytesseract
import re
import requests


# Define the asynchronous function to test the WebSocket connection
async def test():
    balls = ""
    # Establish a WebSocket connection with the specified URL
    async with websockets.connect(
        'wss://chatgpt.func.icu/conversation+ws') as wss:

        # Prepare the message payload as a JSON object
        payload = {
            'content_type': 'text',
            'engine': 'chat-gpt',
            'parts': ['write a story without the letter a'],
            'options': {}
        }

        # Send the payload to the WebSocket server
        await wss.send(dumps(obj=payload, separators=(',', ':')))

        # Initialize a variable to track the end of the conversation
        ended = None
        response = await wss.recv()
        json_response = loads(response)
        balls = ""
        if 'challenge' in json_response:
            # Extract the captcha image from the challenge
            captcha_base64 = json_response['challenge']['question'][22:]
            b64_string = captcha_base64
            img_bytes = base64.b64decode(b64_string)
            np_data = np.frombuffer(img_bytes, np.uint8)
            img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)
            cv2.imwrite('image.jpg', img)
            # Load image from file
            img = cv2.imread('image.jpg')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            median = cv2.medianBlur(gray, 5)
            alpha = 3.0  # Contrast control (1.0-3.0)
            adjusted = cv2.convertScaleAbs(median, alpha=alpha)
            # Convert the base64 string to bytes and save the image to disk
            with open('captcha.png', 'wb') as f:
                f.write(adjusted)

            # Convert the image to a base64 string
            with open('captcha.png', 'rb') as f:
                base64_str = base64.b64encode(f.read()).decode('utf-8')

            # Set the API URL and parameters
            api_url = 'https://ocr.holey.cc/ncku'
            params = {'base64_str': captcha_base64}

            # Send a GET request to the API
            response = requests.get(api_url, params=params)

            # Parse the response JSON
            result = response.json()
            print(result)
            challenge_answer = result['data']
            payload2 = {"options": {"challenge_answer": f"{challenge_answer}"}}
            print(challenge_answer)
            await wss.send(dumps(obj=payload2, separators=(',', ':')))
        # Continuously receive and process messages until the conversation ends
        while not ended:
            try:
                # Receive and parse the JSON response from the server
                response = await wss.recv()
                json_response = loads(response)
                print(json_response)
                # work of absolute chaos: -- repeat this until one passes through
                if 'challenge' in json_response:
                    # Extract the captcha image from the challenge
                    captcha_base64 = json_response['challenge']['question'][
                        22:]

                    # Convert the base64 string to bytes and save the image to disk
                    with open('captcha.png', 'wb') as f:
                        f.write(base64.b64decode(captcha_base64))

                    # Convert the image to a base64 string
                    with open('captcha.png', 'rb') as f:
                        base64_str = base64.b64encode(f.read()).decode('utf-8')

                    # Set the API URL and parameters
                    api_url = 'https://ocr.holey.cc/ncku'
                    params = {'base64_str': base64_str}

                    # Send a GET request to the API
                    response = requests.get(api_url, params=params)

                    # Parse the response JSON
                    result = response.json()
                    challenge_answer = result['data']
                    payload2 = {
                        "options": {
                            "challenge_answer": f"{challenge_answer}"
                        }
                    }
                    await wss.send(dumps(obj=payload2, separators=(',', ':')))
                    continue

                ended = json_response.get('eof')

                # If the conversation has not ended, print the received message
                if not ended:
                    print(json_response['content']['parts'][0])
                    balls += json_response['content']['parts'][0]

            # Handle cases when the connection is closed by the server
            except websockets.ConnectionClosed:
                break
        return balls
