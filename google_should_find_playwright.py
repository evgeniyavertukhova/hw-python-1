from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://ya.ru')

    search_input = page.locator('[name="text"]')
    expect(search_input).to_be_empty()
    search_input.fill('yashaka/selene')
    search_input.press('Enter')

    # Ждём, пока появится результат
    expect(page.locator('body')).to_contain_text('selene')

    browser.close()