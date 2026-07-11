from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")

    print("Подключились!")

    contexts = browser.contexts

    print("Контекстов:", len(contexts))

    if contexts:
        page = contexts[0].pages[0]
        print(page.title())
        print(page.url)

    browser.close()
