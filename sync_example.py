"""
Создание скриншота веб-страницы в синхронном режиме
"""

from playwright.sync_api import sync_playwright
from datetime import datetime

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.championat.com/hockey/_superleague.html")
    page.screenshot(path=f"screenshots/page_{datetime.now().strftime('%d%m%Y%H%M%S')}.png")

