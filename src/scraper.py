"""
This is part of gobbo-datos
Copyright Rodrigo Garcia 2025
"""

import traceback
from playwright.async_api import async_playwright

from src.locators import locators
from src.common.custom_logger import CustomLogger
from src.common.selectors import get_selector_value, get_locator, is_element_located
from src.common.time import random_sleep, today_yyyymmdd
from src.common.csv import csv_write_headers, append_to_csv, csv_columnnames_exist
from typing import List, Dict

LOGGER = CustomLogger('gob.bo scraper ')


class GobboScrapper:
    """Class that helps scraping gob.bo"""

    def __init__(
        self,
            width=1280,
            height=800,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            home_page='https://www.gob.bo/'
            
    ):
        self.width = width
        self.height = height
        self.user_agent = user_agent
        self.home_page = home_page
        self.page = None


    async def init(self, p):
        browser = await p.chromium.launch(headless=False)

        context = await browser.new_context(
            viewport={'width': self.width, 'height': self.height},
            user_agent=self.user_agent,
        )
        self.page = await context.new_page()


    async def goto_home(self):
        try:
            await self.page.goto(self.home_page, wait_until="networkidle", timeout=120000)
        except Exception as e:
            LOGGER.error(LOGGER.format_exception(e))
            raise e


    async def enter_category(self, category: str):
        """Goes to the main page and loads the give category
        """
        await self.goto_home()
        await random_sleep(2, 5.5)
        await self.page.locator(get_locator(locators['categorias']['linkPorNombre'], category)).click()
        await random_sleep(1, 2.2)


    async def get_procedure_elements(self) -> List:
        """Gets the list of procedure elements
        """
        try:
            elements = await self.page.locator(get_locator(locators['listaTramites']['linkPorTramite'])).all()
            return elements
        except Exception as e:
            LOGGER.error("Can't get procedures links.")
            LOGGER.error(LOGGER.format_exception(e))

        
    async def get_procedures_links(self) -> List[str]:
        """Get all links of procedures"""
        links = []
        try:
            elements = await self.page.locator(get_locator(locators['listaTramites']['linkPorTramite'])).all()
            for element in elements:
                link_procedure = element.get_attribute("href")
                links.append(f'{self.home_page}/{link_procedure}')
        except Exception as e:
            LOGGER.error("Can't get procedures links.")
            LOGGER.error(LOGGER.format_exception(e))

        return link
    

    async def get_text_from_all_elements(self, locator):
        """Gets the text from all elements that matches the locator.
        When there are multiple elements the text is concat with ,
        If no element is found returns an empty string
        """
        text = ''
        if await is_element_located(self.page, locator):
            web_elements =  await self.page.locator(get_locator(locator)).all()
            if len(web_elements) == 1:
                return await web_elements[0].inner_text()

            for web_element in web_elements:
                text += await web_element.inner_text() + ','
        return text


    async def scrape_procedure_by_url(self, url) -> Dict:
        """Examines the current page that should be a procedure and gets
        the data by scraping it.

        #TODO: Agregar duracion (en mas informacion)

        Returns:
        Dictionary with procedure data
        """
        LOGGER.debug(f'Scraping Procedure {url}')
        try:
            await self.page.goto(url, wait_until="networkidle", timeout=120000)
        except Exception as e:
            LOGGER.error(LOGGER.format_exception(e))
            raise e

        procedure = {}
        procedure['titulo'] = await self.get_text_from_all_elements(locators['tramites']['titulo'])
        LOGGER.debug(f' Title: {procedure["titulo"]}.')
        procedure['institucion'] = await self.get_text_from_all_elements(
            locators['tramites']['institucion']
        )

        procedure['descripcion'] = await self.get_text_from_all_elements(
            locators['tramites']['descripcion']
        )

        procedure['institucion'] = await self.get_text_from_all_elements(
            locators['tramites']['institucion'])

        procedure['contacto'] = await self.get_text_from_all_elements(
            locators['tramites']['contacto'])

        procedure['web'] = await self.get_text_from_all_elements(
            locators['tramites']['web'])

        procedure['institucion'] = await self.get_text_from_all_elements(
            locators['tramites']['institucion']
        )

        procedure['es_presencial'] = 0
        procedure['es_en_linea'] = 0
        
        tipoTramite1 = await self.get_text_from_all_elements(
            locators['tramites']['tipoTramite1'])
        if tipoTramite1.endswith('Presencial') is True:
            procedure['es_presencial'] = 1
        if tipoTramite1.endswith('Línea') is True:
            procedure['es_en_linea'] = 1
        else:
            tipoTramite2 = await self.get_text_from_all_elements(
                locators['tramites']['tipoTramite2'])
            if tipoTramite2.endswith('Presencial') is True:
                procedure['es_presencial'] = 1
            if tipoTramite2.endswith('Línea') is True:
                procedure['es_en_linea'] = 1

            
        procedure['requisitos'] = await self.get_text_from_all_elements(
            locators['tramites']['queNecesitoText'])

        procedure['procedimiento'] = await self.get_text_from_all_elements(
            locators['tramites']['comoYDondeTexto'])

        procedure['num_ubicaciones'] = 0
        procedure['ubicaciones'] = await self.get_text_from_all_elements(
        locators['tramites']['direccionesTramite'])
        ubicaciones_elements = await self.page.locator(
            get_locator(locators['tramites']['direccionesTramite'])
        ).all()
        procedure['num_ubicaciones'] = len(ubicaciones_elements)
        
        procedure['info_adicional'] = await self.get_text_from_all_elements(
            locators['tramites']['masInfo'])

        procedure['ultima_actualizacion'] = await self.get_text_from_all_elements(
            locators['tramites']['ultimaActualizacion'])

        procedure['observaciones'] = await self.get_text_from_all_elements(
            locators['tramites']['observaciones'])

        procedure['costo_descripcion'] = await self.get_text_from_all_elements(
            locators['tramites']['costoTexto'])

        procedure['costo_montos'] = await self.get_text_from_all_elements(
            locators['tramites']['costoMontos'])

        procedure['costo_formas'] = await self.get_text_from_all_elements(
            locators['tramites']['costoFormas'])

        procedure['costo_conceptos'] = await self.get_text_from_all_elements(
            locators['tramites']['costoConceptos'])

        procedure['costo_ctas_bancarias'] = await self.get_text_from_all_elements(
            locators['tramites']['costoCtasBancarias'])

        r_green_elements = await self.page.locator(
            get_locator(locators['tramites']['rateGreen'])).count()
        r_yellow_elements = await self.page.locator(
            get_locator(locators['tramites']['rateYellow'])).count()        
        r_red_elements = await self.page.locator(
            get_locator(locators['tramites']['rateRed'])).count()        
        procedure['calificacion'] = r_green_elements + r_yellow_elements + r_red_elements

        return procedure


    async def scrape_entire_category(self, category: str, save_to_file=None) -> List[Dict]:
        """Gets all procedures data of the given category.
        Enters to each of procedures by click to them and returning to the
        original page.

        Parameters:
        category (str): Name of the category from the main page

        Returns:
        Dictionary with Procedures data
        """
        # 1. Enters to the category
        await self.enter_category(category)

        procedures = []

        pages = 0
        LOGGER.info(f'Starting category {category}----------------------------------------------')
        procedure_urls = []
        while True:
            LOGGER.info(f'----------- {category} - Page: {pages}')

            # Get procedures of the current page
            elements = await self.get_procedure_elements()
            # Scraping every procedure element
            
            for i, procedure_element in enumerate(elements):
                await elements[i].scroll_into_view_if_needed()
                procedure_urls.append(await elements[i].get_attribute('href'))

            # Next page
            if await is_element_located(self.page, locators['listaTramites']['pagSiguienteBtn']):
                LOGGER.info(f'Forwarding page {pages} \n\n')
                next_btn = self.page.locator(
                    get_locator(locators['listaTramites']['pagSiguienteBtn'])
                )
                await next_btn.scroll_into_view_if_needed()
                await random_sleep(2, 4)
                await next_btn.click()
                pages += 1
                await random_sleep(0.4, 2)
            else:
                LOGGER.debug('Next page button not found. --------------------------------------')
                LOGGER.info(f'Total of {len(procedures)} - Category: {category} ({pages} pages)')
                break

        LOGGER.info('Getting procedures data.')

        for url in procedure_urls:
            # scrape procedure page
            #procedure = await self.scrape_current_procedure_page()
            procedure = await self.scrape_procedure_by_url(self.home_page + url)
            procedure['url'] = self.home_page + url
            procedure['categoria'] = category
            await random_sleep(0.5, 1.5)
            procedures.append(procedure)
            if save_to_file is not None:
                LOGGER.debug(f'Saving procedure to file {save_to_file}')
                csv_headers = list(procedure.keys())
                if csv_columnnames_exist(save_to_file, csv_headers) is False:
                    csv_write_headers(save_to_file, csv_headers)
                append_to_csv(procedure, csv_headers, save_to_file)
                LOGGER.debug('Added to csv.')
            LOGGER.debug(f'Saved procedures up to now: {len(procedures)}')
            
        return procedures
