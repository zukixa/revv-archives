import base64
from playwright.async_api import async_playwright


async def send_request(prompt, model_id, scales):
    #
    #
    #
    scale = str(scales)
    modelarray = [
        "AnyLora",
        "AbsoluteReality 1.6 (realistic)",
        "Anything 3.0 (anime)",
        "Anything 4.0 (anime)",
        "Anything 5.0 (anime)",
        "Deliberate 2 (general)",
        "DreamShaper 5 (general)",
        "DreamShaper 6 (general)",
        "DreamShaper 7 (general)",
        "Epîc Diffusion 1.1 (general)",
        "NightmareShaper (general)",
        "Stable Diffusion 1.4 (general)",
        "Stable Diffusion 1.5 (general)",
        "Stable Diffusion 2.1 (512px) (general)",
        "Vintedois Diffusion (simple, general)",
        "Waifu Diffusion 1.3 (anime)",
        "Waifu Diffusion 1.4 (anime)",
    ]
    model = modelarray[model_id]
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        # Go to the BIGJPG website
        print("a")
        await page.goto("https://dezgo.com/")
        # Click on the "Log in / Sign Up" button
        # Fill in the email and password
        print("b")
        await page.wait_for_timeout(3 * 1000)
        print("c")
        await page.type(
            "textarea.mud-input-slot.mud-input-root.mud-input-root-outlined.mud-input-root-margin-dense",
            prompt,
        )
        print("d")
        await page.wait_for_timeout(3 * 1000)
        # if model is not dreamscaper 6
        if model != "DreamShaper 7 (general)":
            await page.wait_for_selector(".mud-select")
            await page.click(".mud-select")
            await page.wait_for_timeout(3 * 1000)
            await page.click(f"text={model}")
        # 0 is portrait, 3 is square, 6 is landscape
        if scale != "3":
            element = await page.query_selector(
                ".mud-expand-panel.mud-elevation-1.mud-expand-panel-border"
            )
            await element.click()
            await page.wait_for_timeout(3 * 1000)
            # 0 portrait 3 central 6 landscape
            await (await page.query_selector_all(".mud-slider-input"))[1].fill(scale)
        await page.wait_for_timeout(3 * 1000)
        print("e")
        await page.click("text=Run")
        # Click on the checkbox
        # Wait for the image to be present
        print("f")
        image_element = await page.wait_for_selector("#image-output")

        print("g")
        # Get the 'src' attribute of the image
        src_value = await image_element.get_attribute("src")
        # Step 1: Parse the base64 string
        header, base64_str = src_value.split(",")

        # Step 2: Base64 decode the data
        image_data = base64.b64decode(base64_str)

        # Close the browser
        await browser.close()
        print(image_data)
        return image_data


