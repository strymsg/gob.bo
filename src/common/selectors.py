"""
This is part of gobbo-datos
Copyright Rodrigo Garcia 2025
"""
from src.common.custom_logger import CustomLogger

LOGGER = CustomLogger('selectors 🧰:')

def get_selector_value(selector, *args):
    """Helps checking the selector value.
    Parameters:
    selector (str or function): If it is a function, uses args* to pass the function arguments and return
      a result. Else returns the selector string
    args (list): if `selector' is a function this args are passed as arguments to that function
    Returns:
    str: Resulting selector
    """
    svalue = ''
    if isinstance(selector['value'], str) is False:
        svalue = selector['value'](*args)
    else:
        svalue = selector['value']
    return svalue


def get_locator(selector, *args):
    """Replaces the selector values and returns a valid string to be used in
    playright page.locator"""

    svalue = get_selector_value(selector, *args)
    if selector['stype'] == 'xpath':
        svalue = f'xpath={svalue}'
    if selector['stype'] == 'css':
        svalue = f'css={svalue}'
    LOGGER.debug(f'  locator: {svalue}')
    return svalue


async def is_element_located(page, selector, *args):
    """Tries to get the element from the given selector on the given page obeject.
    If element is not located or visible returns False
    """
    element = page.locator(get_locator(selector))
    if await element.count() > 0:
        return True
    return False
    

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


async def get_text_from_page_and_locator(p, locator: str, throw_exception=True):
    """Returns the `inner_text' from the element find with the given locator

    Parameters:
    p (Page Object playwrigth): Page object from browser context to search in
    locator: locator string
    throw_exception (bool): If true, raises an exception when no element for the given
      locator is found, otherwise will return an empty string
    """
    if not throw_exception:
        txt = await p.locator(get_locator(locator)).inner_text()
        return txt if txt is not None else ''

    try:
        return await p.locator(get_locator(locator)).inner_text()
    except Exception as e:
        LOGGER.error(f'Error getting element with locator {locator}')
        LOGGER.error(LOGGER.format_exception(e))
        raise e
