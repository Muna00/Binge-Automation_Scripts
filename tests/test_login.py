from asyncio import timeout

from playwright.sync_api import sync_playwright, expect
import re
from playwright.sync_api import Page
from models.login import Login
from models.others import Player_Keys


def test_login_elementVisibility(page:Page):
    login_page = Player_Keys(page)
    login_page.login_navigate()
    login_page.login_button.click()
    login_page.login_visibility()



def test_OTP_valid_login(page: Page):
    login_page=Player_Keys(page)
    login_page.login_navigate()

    login_page.otp_login("", ["","","",""])
    expect(page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")).to_be_visible()
    login_page.profile_img.click()

    expect(page.locator("div[class='BingeBox-root css-xkdv7i']")).to_be_visible()


def test_email_valid_login(page: Page):
    login_page = Player_Keys(page)
    login_page.login_navigate()

    login_page.email_login("","")
    expect(page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")).to_be_visible()
    login_page.profile_img.click()

    expect(page.locator("div[class='BingeBox-root css-xkdv7i']")).to_be_visible()


def test_gmail_login(page: Page): # ei script majhe moddhe run kore na, koyekbar run korle hoy( HOPEFULLY), jani na keno
    login_page = Player_Keys(page)
    login_page.login_navigate()

    login_page.gmail_login()
    #page.wait_for_timeout(100)
    expect(page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")).to_be_visible()
    login_page.profile_img.click(timeout=30000)
    expect(page.locator("div[class='BingeBox-root css-xkdv7i']")).to_be_visible()





