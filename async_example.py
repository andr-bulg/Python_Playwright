"""
Сохранение в файл формата pdf веб-страницы в асинхронном режиме
"""

from playwright.async_api import async_playwright
import asyncio
from datetime import datetime

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.championat.com/hockey/_superleague.html/")
        await page.pdf(path="pdf/async_page_{}.pdf".format(datetime.now().strftime('%d%m%Y%H%M%S')))

asyncio.run(main())

