# tests/test_yandex_search_selenium.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def driver():
    # Настройка браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Автоматическая установка драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    # Закрытие браузера
    driver.quit()


def test_yandex_search(driver):
    print("Открываем сайт ya.ru")
    driver.get("https://ya.ru")

    print("Ищем поле ввода")
    search_input = driver.find_element(By.NAME, "text")
    assert search_input.get_attribute("value") == ""

    print("Вводим запрос и нажимаем Enter")
    search_input.send_keys("yashaka/selene")
    search_input.send_keys(Keys.ENTER)

    print("Ждём появления результатов")
    time.sleep(2)  # можно заменить на WebDriverWait

    print("Проверяем, что текст 'selene' есть на странице")
    assert "selene" in driver.page_source.lower()
