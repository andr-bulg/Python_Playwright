"""
Тесты, в которых выполняются действия с тоглами и чекбоксами
"""

from playwright.sync_api import Page, expect
from datetime import datetime

def test_main_actions(page: Page):
    page.get_by_test_id("search__input").fill("python")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Результаты поиска «python»")).to_be_visible()
    expect(page).to_have_url("https://www.litres.ru/search/?q=python")

    # Переключение тоглов
    page.locator("xpath=//*[@aria-description='Книги, которые можно читать без ограничений с активной Литрес: Подпиской']").dblclick()
    page.locator("xpath=//*[@aria-description='Книги, которые можно взять по Литрес: Абонементу']").click()

    # Включение чекбоксов
    page.locator("label[for='languages-ru']").click(force=True)
    page.locator("xpath=//*[@id='languages-es']").click(force=True)
    page.check("label[for='languages-en']")

    page.screenshot(path=f"screenshots/action_{datetime.now().strftime('%d%m%Y%H%M%S')}.png")
    page.pause()

