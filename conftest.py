from playwright.sync_api import Page
import pytest


# Создание фикстуры, которая будет общей для всех тестов
@pytest.fixture(autouse=True)
def open_page(page: Page):
    page.goto("https://www.litres.ru/")

