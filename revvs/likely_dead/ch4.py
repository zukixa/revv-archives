import asyncio
from playwright.async_api import async_playwright

try:
    from . import gp as gp
except:
    import gp as gp


async def send_request(prompt: str):
    async with async_playwright() as p:
        attemps_made = 0
        max_attempts = 20
        while attemps_made < max_attempts:
            # Get new proxy
            px = await gp.get_proxy()
            # Launch browser with the new proxy
            browser = await p.chromium.launch(headless=True, proxy={"server": px})
            page = await browser.new_page()

            try:
                # Try to navigate to the URL
                await page.goto("https://ch4.onrender.com/")
                await page.wait_for_timeout(2000)

                # If success, return page after successful navigation
                break

            except Exception as e:
                print(f"Attempt {attemps_made + 1} failed: {e}")

                # Close browser if exception caught
                await browser.close()

                # Increase the number of attempts made
                attemps_made += 1
        # Click the 'New Chat' button
        new_chat_button = await page.query_selector(".el-button--primary")
        if new_chat_button is not None:
            await new_chat_button.click()

        # Wait for the textarea to be present and visible
        await page.wait_for_selector(".el-textarea__inner", state="attached")
        # Input 'hi' into the textarea
        await page.fill(".el-textarea__inner", prompt)

        # Press the 'Send' button
        send_button = await page.query_selector(".el-button--primary.el-button--large")
        if send_button is not None:
            await send_button.click()

        while True:
            output_message = await page.query_selector(".Message.A.p-4")
            message_text = await output_message.inner_text()
            if "Thinking" not in message_text:
                break
            await asyncio.sleep(0.1)  # Wait 10

        # Extract the output message
        output_message = await page.query_selector(".Message.A.p-4")
        message_text = await output_message.inner_text()
        message_texts = message_text.split("\n")

        # The dialogue part of the message text is all but the last line.
        dialogue_text = "\n".join(message_texts[:-1])
        print("Output Message: ", dialogue_text)

        # Close the browser
        await browser.close()
        return dialogue_text

