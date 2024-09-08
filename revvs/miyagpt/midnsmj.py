import aiohttp
import asyncio
import json
import time, random
import uuid

tokens = [
    "e8b3fa60-464c-4844-8e77-33ebe010838e",
    "3e9b0336-851b-45f3-887e-474caf09e2f6",
    "039bc7d9-ff2b-4fc9-a53a-d0ccf5e927a3",
    "3af3b9be-6562-442c-9dda-60685964ed6c",
    "68ba08ec-02fa-485a-b416-6166a16aa96c",
    "3c47a3b1-990c-46f1-a574-60526187f842",
    "9cb8f0fb-8e2d-4eeb-be66-936c4745b354",
    "50c8bdeb-01c7-486f-b5db-2a97dc350e56",
    "1703a7e6-2d43-43dd-bbef-1f1602efda04",
    "e9d35f93-5f79-47e0-9b8b-5a9da752937a",
    "7c0539d6-359a-4355-9b4b-ebeb45a43564",
    "06fc9953-4163-43ff-a9c5-9ebef78aa1de",
    "f4d9a54b-cfdd-455b-b2b8-e9f3c5d6bbee",
    "89a54ec8-8776-458b-b06f-13d8f79287d8",
    "657fa2c0-f282-45ef-a60c-41121ebb25a7",
    "551a1457-8824-40fa-be66-430bb8ae5d9f",
    "582317c0-8143-4acd-9213-cc7daf3ac201",
    "3fe4da68-ad4c-47e0-9bf6-4feca8d7dbae",
    "e9195a2a-83a1-4008-87cd-9b10bcc8161a",
    "713a55e1-6d2c-45a9-91f3-416c6ad530b4",
    "6295d425-915c-4249-8660-d666ce31d2c7",
    "dbe76d72-c16c-41e3-9259-e8e9da40efbb",
    "b9e1f969-5320-488e-9834-b342544aa1b0",
    "b7bebfda-0f01-472c-89bc-703d75c83611",
    "89c11634-671d-4e8d-af65-9397aef52649",
    "05d8716b-c0b9-4d31-b29b-caed34427dba",
    "3028096e-97c9-4dfa-bc6a-80544f4db07f",
    "dffb474b-7677-4e3e-8061-912c0bdf8774",
    "5d848ec7-accc-412d-8ad2-73d6ee44438b",
    "5b2ec191-aa6a-4f93-9263-0c5a1d133790",
    "3158f3d3-1488-42df-bc61-4453c66e9173",
    "f1b20bfe-635a-4d0e-a980-f5c9a96c06b3",
    "5d20672c-2b58-43d1-8122-d98c0363f7ea",
    "f6435126-e3ab-46aa-a63d-14364a1904c1",
    "521f4fe8-068d-4467-b7a2-ba2c58ca7cb4",
    "6168de61-0524-4c2e-8c2a-c2ef95d48075",
    "e9e53b74-4c72-482b-8246-a24b76967df7",
    "9ad49768-957e-451d-a121-e17e288af5f9",
    "787a70aa-6d4f-43a6-98db-a6a1884847a1",
    "2187c11f-b352-4296-ad65-db26e4116eb2",
    "bca0f77e-16e4-449b-9bd4-08e0ea13424c",
    "d3fd2fee-6866-4de1-b5a8-2ae159a91f4a",
    "b2f8d684-4ce0-47b5-9f7e-adbc075f6855",
    "a0806e26-86cf-4d4c-9f07-b47836f5ad1a",
    "cc45324c-72de-472b-9bf7-960a4b7b24c6",
    "33cb0aaf-bb8b-410a-91b6-c16ba58ee9b7",
    "0751ed4c-6d59-4953-8224-263ad7f257d8",
    "f76dcb3a-0244-4f74-823f-851856aa3a4d",
    "b83727b2-7113-457d-84d3-b5a791c32f61",
    "cd1d1a8f-4dd2-4ad7-97c1-8d67c686a663",
    "2297cec9-3d41-4bf9-b0df-0aef2a5cd0e8",
    "d180d025-d775-42d8-a76c-6b9ff6c41dd7",
    "3a70e46a-39aa-4110-8b10-2c833d9a6b96",
    "c43a8afe-8762-4965-a12b-d6ac17d5a84c",
    "a8f4f4ca-161e-4049-b939-639abfc82571",
    "4ffd1178-ac83-4698-abb3-d658ccafcb3b",
    "481ecd65-182d-4fd2-9688-ca1616de75a8",
    "ff94bc54-9279-4fd6-b18f-664c889e0041",
    "a6470cf8-30b9-410c-9b70-f46299c17b0c",
    "7f0d0f09-bb6c-48f9-87a9-17954df06306",
    "6cd3e9ac-a6b7-4c59-aca7-c91d83b16e80",
    "0b42c8fe-5ab7-4a55-9fe8-2ef051f4df6f",
    "26c6bcb3-4d3e-45ac-a21c-1275d326b2a3",
    "b0be4eed-78fe-43d9-bc6f-cb541a185963",
    "31d8b2c5-dd32-414a-95e0-3ef48f688fd7",
    "41105766-c33d-45df-bc63-aaf112483dad",
    "670f4276-e2f1-4886-83da-984872bf6a3b",
    "82f09e2b-a565-485a-97bc-70131719286d",
    "ce326e21-9541-497a-9f24-838765131f93",
    "6e5b964f-c5cb-4a4f-964e-fa94ca9d7d6e",
    "d4edb390-b098-4497-9037-bc2b4775f83d",
    "fe2777a4-9c60-4796-9c42-4369540c98a3",
    "4f37d64f-8d32-4324-b3b9-e6e7185b09d1",
    "5a31bd5b-24c8-421c-a4ff-0f2546596b27",
    "d027e7d0-3622-486f-9c94-098962376a01",
    "a968577d-0de5-4b91-9a4a-6a7d9f6c3166",
    "ab08113b-2f1c-403f-ab24-d6e9ad7e72a0",
    "e0ff1bda-d4a6-4cc2-a093-f73eee5ef777",
    "f2d1cead-f924-4f8d-b4e3-b1068621f2aa",
    "16f776ef-f7fa-4c92-9178-b12afba2068d",
    "03f42d8f-9555-4b74-8025-f29713ded3f7",
    "5483a0b6-eb18-4ae8-9253-c57607588fb9",
    "b2967940-bdd7-4df6-a699-c3b2d7efb9e8",
    "7a45f1e9-1c42-480d-a6c2-70c2d4a1d3f7",
    "4ae7b67e-b3d3-4292-b7f9-b365731fe5ab",
    "22fd7ecb-acd3-4689-b198-66196ad167d8",
    "e1fe88b0-a000-449e-9b44-31441394a1fc",
    "a562f526-99fd-45f2-a01e-79b0f85ef666",
    "f96b98a8-808d-4caf-ab82-8e1abcc23d7f",
    "cc86575e-913b-4d33-be9b-c5c34904e8f1",
    "63120c2a-a93e-4a6d-8f1b-f646d9422ce7",
    "fa0a42d0-5131-4880-abd6-a24c392b0bbd",
    "1a72daf6-56a7-47f8-9534-bffde8f99c77",
    "0255d836-31a5-4fe7-ba71-f6720010abc1",
    "f224d714-9514-4993-aa78-e8506871fb8b",
    "ba8cd965-ec37-44cc-bb47-aae0e9d09a8e",
    "dbb43218-775f-442f-9f83-7d4f2ed1c866",
    "abc68ac0-6552-4cfd-a02e-71af6b8d56e3",
    "e9c75f85-e53d-4670-91c9-dcc750b1fac3",
]

tokens = [
    "1331d31c-cf9e-4240-ac15-6520c008876d",
    "2e30dca3-c774-4274-909d-ac1332adfda8",
    "0a913d8d-3a76-49b1-bfb6-4351121d1538",
    "122a0735-fe0d-4f49-b70a-d2144f98a975",
    "42b53cb8-f02b-4791-9b87-fff1c26e8f5f",
    "9e285995-c257-4e9a-9950-de73c85fccd1",
    "a8e2089d-8389-47ba-af48-9a67a74ea97d",
    "287c8089-6226-4754-b8c8-14981d72ec47",
    "3035908f-4e9a-43a5-bfd4-1ee6ce0ed2d8",
    "871cbc7b-92ca-4889-817f-c3a13e8f3524",
    "9e7caab5-4437-4673-96c2-7676c503cdb7",
    "74526d78-b847-42ff-b28c-293575ac8da9",
    "b9da0955-f13d-434e-8424-8e4b44714428",
    "fa74b674-1863-4b2c-a7f8-76aefbb0d9a4",
    "ead8b79c-e73d-4bc7-ae33-8ddf96c65c2a",
    "8c040b6e-f3ba-4f52-9265-6bc23050c30d",
    "d307f9eb-c222-4c0f-aaea-ad36d0ab9a0f",
    "d5ddbaff-5d43-45cb-97a8-628f87e6b428",
    "4a91d202-ddb2-458d-b9c2-7db03156148c",
    "64254567-0336-4d20-aa2e-aeef45a05d99",
    "c2f4b905-501f-4ac0-a135-ed150187887f",
    "883624bc-e8e3-4766-af8f-68a3619fa818",
    "fb6d5355-4ac9-4d41-915c-37f9f7991b6c",
    "118ac2fd-2968-4e32-9521-fa6ac735cdb2",
    "44d99d42-4ec7-4beb-b47e-5f723f860189",
    "34065045-6306-40a3-9432-6fec6f323534",
    "bf54b4ee-e4fb-4eb5-96bc-6f11ae21dce3",
    "be6c053a-37d9-43ab-b5ed-8931ebad7b21",
    "d139d2d8-bf13-4a1b-b2a4-f28ef12e6891",
    "c9c5b53c-00a3-4bd3-9977-f22778e46209",
    "2f121059-3fbd-450d-bccd-4e935fc3b640",
    "b3a81f26-e00b-43e8-ad0b-1ae9ffce336a",
    "a37e1dc2-8cf7-4a98-aa2c-46cf2b1b4ca7",
    "8fd6f125-3527-4f7e-b992-314fefec8285",
    "1f25acca-c3b9-4bac-bbdd-dbce6c748cfc",
    "b6b17d6a-9b7d-4d5f-882e-80079d5e2cce",
    "996500f1-9e5d-455c-bc4b-6cac1a8e5498",
    "64d9a2e8-b5b0-4f69-8275-b55440e1693c",
    "2583ea42-0178-4cf3-89be-b75afd423687",
    "985ab3a8-932e-438a-9941-7c3a2147c408",
    "3e7f9db8-9d3f-454e-9fcd-dc931d3c4d36",
    "16eb385a-c14d-4431-b7ca-bcd68250b1ec",
    "2f3977ff-93c8-4798-af41-82044059da19",
    "c1052b05-08d4-43f8-820c-af56a078382f",
    "b9880fe2-4a23-4abf-8e15-8e825bc7fde0",
    "4fbbbdc3-99cc-4e6a-a1ed-6298e708e2bb",
    "d8fd9014-9e4a-4875-9580-cb567aac705b",
    "fdb5b642-a06e-4ca1-9df3-b64e15c97e70",
    "89855427-3f37-41e5-8875-dc438a30822d",
    "df24f0e1-8c2a-4dde-8806-d9322fd99de5",
    "88a4c721-3a89-4fe6-a7f8-7bf6349417e4",
    "6bc504d0-241d-4458-ae79-8eca69b017c2",
    "ef360a68-5deb-4773-908a-3e3e254c4e35",
    "8f278a37-444f-44fc-9b91-9a2467e0e26f",
    "985effd7-78ed-4673-a3e3-71034da487d0",
    "d3407273-d003-4834-8127-45126e19eaa1",
    "7895ec61-38ef-49ee-befc-d23fa88dd2ca",
    "54867e80-35c8-42b9-82e8-70db908e4c41",
    "3c704893-5e98-4483-9448-f91bd3234dae",
    "d53af9e5-9899-4a47-8ae2-7d9069dca221",
    "4161eaa3-4710-4d8d-be84-cf9f6ad0a211",
    "2e3084f8-2e11-4885-870f-c5027494e5e7",
    "18b55b62-156a-4653-969d-8a39b876186a",
    "88af4912-98fb-4628-a020-802272447a09",
    "aa2c2df0-e612-4037-9333-56bf1e190bdc",
    "7e874358-3e8c-467c-9eac-3410343fc2a7",
    "6ac0282f-5046-4bcf-a572-e5df8e5ed89f",
    "9e467bf9-7e14-411d-8d83-8b9571914082",
    "ba7e39b4-a9cc-496f-a70b-d939d46b6725",
    "be13ea60-6117-44e1-bda8-c9e60ae58c71",
    "db82a04f-98a2-4861-9d86-480ccc66b06d",
    "bf1d7496-9835-42ed-a3b0-4898f640a227",
]


async def send_request(prompt: str):
    tries = 0
    while tries < 10:
        try:
            TOKEN = random.choice(tokens)
            headers = {
                "Connection": "keep-alive",
                "sec-ch-ua": '"Chromium";v="116", " Not A;Brand";v="24", "Google Chrome";v="116"',
                "Content-Type": "application/json",
                "X-Token": TOKEN,  # "387e6503-524e-4417-8936-199e0dcada79",
                "sec-ch-ua-mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "sec-ch-ua-platform": '"macOS"',
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://miyadns.com",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://miyadns.com/",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
            }
            async with aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(ssl=False)
            ) as session:
                # First Post Request
                post_url = "https://miyadns.com/api/Chat/Image"
                post_data = {
                    "prompt": prompt,
                    "sessionId": str(uuid.uuid4()),
                    "type": "2",
                }

                async with session.post(
                    post_url, headers=headers, data=json.dumps(post_data)
                ) as resp:
                    post_json = await resp.json()
                    print(post_json)
                # Extract the result from the JSON response
                result_id = post_json["result"]

                # Second GET Request
                get_url_template = (
                    "https://miyadns.com/anonymousapi/Anonymous/ImgStatus?imgId={}"
                )

                # Loop until 'IN_PROGRESS' is not the status
                while True:
                    async with session.get(
                        get_url_template.format(result_id), headers=headers
                    ) as resp:
                        get_json = await resp.json()
                        print(get_json)

                    if get_json["result"] not in ["IN_PROGRESS", "SUBMITTED"]:
                        # Exit the loop if the result is not 'IN_PROGRESS'
                        break

                    # Sleep for a bit before polling again to avoid flooding the server with requests
                    await asyncio.sleep(1)

                image_get_url = (
                    "https://miyadns.com/anonymousapi/Anonymous/ImgShow?imgId={}"
                )
                async with session.get(
                    image_get_url.format(result_id), headers=headers
                ) as resp:
                    n = await resp.read()
                    if n is None:
                        tries += 1
                        continue
                    else:
                        return n
        except:
            tries += 1
