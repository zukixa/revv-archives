import asyncio
from playwright.async_api import async_playwright


async def send_request(prompt: str):
    browser = None
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto("https://vello.ai/app")
            await asyncio.sleep(3)
            # Press the first button
            #     await page.click("button.absolute.right-4.top-4")
            #     await asyncio.sleep(1)
            # Press the second button
            await page.click('text="GPT 4"')
            await asyncio.sleep(1)
            # Fill in the textarea
            await page.fill("textarea.resize-none", prompt)
            await page.wait_for_selector(
                ".cursor-pointer.text-center.text-slate-300.grid.place-items-center.w-8.h-8.rounded-full.shrink-0.hover\\:bg-slate-50.-ml-10.text-slate-300"
            )
            await page.click(
                ".cursor-pointer.text-center.text-slate-300.grid.place-items-center.w-8.h-8.rounded-full.shrink-0.hover\\:bg-slate-50.-ml-10.text-slate-300"
            )
            # cursor-pointer text-center text-slate-300 grid place-items-center w-8 h-8 rounded-full shrink-0 hover:bg-slate-50 -ml-10 text-slate-300
            # wait for a while
            await asyncio.sleep(5)

            # Set the selector for the xpath of the articles
            # ... previous code ...

            # Set the CSS selector for the article containing the message
            # CSS selector for the container
            chat_thread_selector = "#chat_thread"
            # CSS selector for messages. Adjust this to the correct class for GPT4 vs user messages.
            gpt4_message_selector = f"{chat_thread_selector} .group.bg-white"

            # Variable to hold the message seen in the last iteration
            last_message = ""
            # Counter to break the loop after seeing the same message multiple times
            recheck_counter = 0

            while True:
                # Query all GPT4 message groups
                gpt4_message_elements = await page.query_selector_all(
                    gpt4_message_selector
                )
                print(gpt4_message_elements)
                if gpt4_message_elements:
                    # Take the last GPT4 message group since we want the most recent
                    last_gpt4_message_element = gpt4_message_elements[-1]
                    # Extract the text content from the message
                    new_message = await last_gpt4_message_element.text_content()
                    if new_message != last_message:
                        # If the message has changed, update the last_message variable
                        last_message = new_message
                        recheck_counter = 0
                    else:
                        # If the message is the same as last time, increment the recheck counter
                        recheck_counter += 1
                        if recheck_counter >= 3:
                            # If the same message is seen 3 times, break out of the loop
                            break
                else:
                    recheck_counter += 1
                    if recheck_counter >= 3:
                        break
                # Sleep before next check
                await asyncio.sleep(1)

            await browser.close()
            print(last_message)
            if "4" in last_message[:10]:
                return last_message.split("4")[1]
            else:
                return last_message
    except Exception as e:
        print(f"Issue with vello: {str(e)}")
        return ""
    finally:
        # Ensure browser is always closed even if there are exceptions
        if browser:
            await browser.close()

print(asyncio.run(send_request("good allah morning")))