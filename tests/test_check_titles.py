"""
Тесты, проверяющие заголовки загружаемых страниц
"""

from playwright.sync_api import Page, expect

def test_main_page_title(page: Page):
    page.goto("https://www.championat.com/")
    expected_title = "Чемпионат.com: новости спорта - Чемпионат"
    assert page.title() == expected_title, \
        "Фактический заголовок страницы отличается от ожидаемого!"

def test_hockey_page_title(page: Page):
    page.goto("https://www.championat.com/")
    page.locator("xpath=/html/body/header/div[1]/div/nav/ul/li[2]/a").click()
    expected_title = "Хоккей России и мира: новости онлайн, фото, видео, онлайн трансляции — Весь хоккей России в 2024 году - Чемпионат"
    expect(page).to_have_title(expected_title)

