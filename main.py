"""
This is part of gobbo-datos
Copyright Rodrigo Garcia 2025
"""

import asyncclick as click

from playwright.async_api import async_playwright
from src.common.custom_logger import CustomLogger
from src.common.time import today_yyyymmdd
from src.scraper import GobboScrapper


LOGGER = CustomLogger('gob.bo scraper ')


@click.command()
async def scrape_tramites():
    categories = ['Impuestos', 'Bienes Inmuebles', 'Cultura y Turismo',
                  'Económico-Productivo',
                  'Educación', 'Gobierno', 'Identificación', 'Justicia',
                  'Medio Ambiente', 'Salud', 'Transporte']

    gobbo_scraper = GobboScrapper()

    filename = f'{today_yyyymmdd()}_tramites_gobbo.csv'
    
    async with async_playwright() as p:
        await gobbo_scraper.init(p)

        for category in categories:
            await gobbo_scraper.scrape_entire_category(category, filename)
            await gobbo_scraper.goto_home()

    
if __name__ == '__main__':
    scrape_tramites(_anyio_backend='asyncio')
