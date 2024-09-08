import aiohttp
import asyncio
import json


async def send_request(question):
    try:
        url = "https://www.pizzagpt.it/api/chatx-completion"

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            #  "Content-Type": "text/plain;charset=UTF-8",
            "Cookie": "n-req=0; dntd=false;",  # cf_clearance=Rf4fVBYQ4X9Z5GF.w3j8vRQRR1_wAG3ctiAqvmjB6M8-1699300720-0-1-90a9a8a3.544194f1.75769dfb-0.2.1699300720; __gads=ID=c8f0da9801041a3c-222815a1e3e7009a:T=1699300720:RT=1699300720:S=ALNI_MYIeKdNKDvJv23_wM_iIokKVUkyoQ; __gpi=UID=00000a410161e7d3:T=1699300720:RT=1699300720:S=ALNI_MZRSjx-sPtM6jk9JZz7l079XOJGjg; _ga=GA1.1.1580539292.1699300720; FCNEC=%5B%5B%22AKsRol_op0kQwQihXZI_g4kEAcYhu-p6YTFGIRKFi8XvKIYyfYuLI8pYx1PnixbUC9UyWGTpZquffrbRGDvbHaLyoH6O9RZu_1iDfA6ijvVsoOUoruu5Y1lOtHDxaVs-erhE-EynfY0FEPnu6dRLiVj5DpBAWC3_sQ%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; _ga_LZKWDTM58H=GS1.1.1699300720.1.0.1699300723.0.0.0",
            "Origin": "https://pizzagpt.it",
            "Referer": "https://pizzagpt.it/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "X-Secret": "Marinara",
        }

        data = {"question": "Answer in English:\n" + question}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                response_json = await response.json()
        return response_json["answer"]["content"]
    except Exception as e:
        print(f"Issue with pizza: {str(e)}")
        return ""
