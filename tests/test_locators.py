"""
Работа с локаторами
"""

from playwright.sync_api import Page, expect


def test_locator_role(page: Page):
    page.get_by_role("link", name="Читают сейчас").click()
    expect(page).to_have_title("Рекомендации для вас- ищите на Литрес")
    page.get_by_role("button", name="Найти").click()
    expect(page.get_by_text("вебтун")).to_be_visible()

def test_locator_placeholder(page: Page):
    page.get_by_placeholder("Искать на Литрес").fill("Программирование на Python")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Результаты поиска «Программирование на Python»")).to_be_visible()

def test_locator_data_testid(page: Page):
    page.get_by_test_id("tab-login").click()
    expect(page.get_by_text("Введите почту или логин")).to_be_visible()

def test_locator_alttext(page: Page):
    page.goto("https://www.litres.ru/popular/")
    page.get_by_alt_text("Логотип Литрес").click()
    expect(page).to_have_url("https://www.litres.ru/")
    expect(page.get_by_role("link", name="Читают сейчас")).to_be_visible()

def test_locator_title(page: Page):
    page.get_by_title("Телеграмм").click()

def test_locator_xpath(page: Page):
    expect(page.locator("xpath=//a[@title='YouTube']")).to_be_visible()
    page.locator("xpath=//a[@href='https://www.youtube.com/@MyBookbyLitres']").click()

