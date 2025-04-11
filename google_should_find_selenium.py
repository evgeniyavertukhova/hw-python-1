from selene import browser, be, have


browser.open('https://ya.ru')
browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('body').should(have.text('selene'))

# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
test test