import pytest
from selenium.webdriver import Chrome,Firefox,Ie
def get_driver_instance():
    browser_type = pytest.config.option.type.lower()
    env = pytest.config.option.env.lower()
    if env == 'local':
        if 
        driver = Firefox('./browser_servers\chromedriver.exe')
