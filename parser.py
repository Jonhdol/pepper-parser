from playwright.sync_api import sync_playwright
from pathlib import Path

Path("output").mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        viewport={"width": 1600, "height": 3000}
    )

    page.goto(
        "https://www.pepper.ru/hot?page=350",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(5000)

    Path("output/page.html").write_text(
        page.content(),
        encoding="utf-8"
    )

    page.screenshot(
        path="output/page.png",
        full_page=True
    )

    print(page.title())

    browser.close()
