import pytest
import json
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def load_config():
    with open('config.json') as f:
        config = json.load(f)
    return config


import pytest
import json
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def load_config():
    with open('config.json') as f:
        config = json.load(f)
    return config


import pytest
import json
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def load_config():
    with open('config.json') as f:
        config = json.load(f)
    return config


@pytest.fixture(scope="function")
def page(load_config):
    with sync_playwright() as p:
        # Launch Google Chrome instead of Chromium
        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


