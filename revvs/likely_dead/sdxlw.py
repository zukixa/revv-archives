import asyncio
from playwright.async_api import async_playwright


valid_styles = [
    "shrink-0",
    "anime",
    "lineart",
    "pixelart",
    "shrink-0",
    "origami",
    "fantasyart",
    "neonpunk",
    "digitalart",
    "lowpoly",
    "photographic",
    "isometric",
    "cinematic",
    "dmodel",
    "analogfilm",
    "comicbook",
]


async def main(headless, style, prompt, output_dir, browser):
    browser_name = browser.lower()

    if browser_name not in ["chromium", "firefox"]:
        raise ValueError("Browser should be either chromium or firefox")

    if style not in valid_styles:
        raise ValueError(
            f"Invalid Style option, valid styles are:\n{', '.join(valid_styles)}"
        )

    async with async_playwright() as p:
        bytes = None
        if headless:
            browser = await p.chromium.launch(headless=True)
        else:
            browser = await p.chromium.launch()

        page = await browser.new_page()

        await page.goto("https://clipdrop.co/stable-diffusion")

        await page.click("button.termly-styles-module-root-f61419:nth-child(3)")
        await page.click('[name="prompt"]')
        await page.fill('input[name="prompt"]', prompt)
        await page.click("button.w-full:nth-child(1)")

        await page.click("." + style)

        await page.wait_for_selector(".hover\\3A bg-primary-400:nth-child(2)")
        await page.click(".hover\\3A bg-primary-400:nth-child(2)")
        await page.wait_for_timeout(3 * 1000)
        image_elements = []
        for i in range(1, 5):
            ie = await page.wait_for_selector(
                f"button.absolute:nth-child({i}) > img:nth-child(1)"
            )
            image_elements.append(ie)
        print(f"trolled: {image_elements} of {len(image_elements)}")

        for i, image_element in enumerate(image_elements):
            print("a")
            image_url = await image_element.get_attribute("src")
            bytes = await get_file_content_chrome(page, image_url)
        await browser.close()
    return bytes if bytes else None


async def get_file_content_chrome(page, url):
    encoded_content = await page.evaluate(
        """
    async (url) => {
        const response = await fetch(url);
        if (!response.ok) {
            return;
        }
        const buffer = await response.arrayBuffer();
        return Array.from(new Uint8Array(buffer));
    }
    """,
        url,
    )
    if encoded_content is None:
        raise Exception("Request failed")
    return bytes(encoded_content)
