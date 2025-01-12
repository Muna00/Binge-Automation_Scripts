from asyncio import timeout

from playwright.sync_api import sync_playwright, expect
import re
from playwright.sync_api import Page
from models.login import Login

def test_OTP_valid_login(page: Page):
    login_page = Login(page)
    login_page.navigate()
    login_page.close_popups()
    login_page.login_button.click()
    
    login_page.otp_login("01833-183992", ["2","3","2","3"])
    expect(page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")).to_be_visible()
    login_page.profile_img.click()

    expect(page.locator("div[class='BingeBox-root css-xkdv7i']")).to_be_visible()


def test_email_valid_login(page: Page):
    login_page = Login(page)
    login_page.navigate()
    login_page.close_popups()
    login_page.login_button.click()
    login_page.email_login("testtmuna@gmail.com","TestMuna@123")
    expect(page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")).to_be_visible()
    login_page.profile_img.click()

    expect(page.locator("div[class='BingeBox-root css-xkdv7i']")).to_be_visible()


def test_gmail_login(page: Page): # ei script majhe moddhe run kore na, koyekbar run korle hoy( HOPEFULLY), jani na keno
    login_page = Login(page)
    login_page.navigate()
    login_page.close_popups()
    login_page.login_button.click()
    login_page.gmail_login()
    #page.wait_for_timeout(100)
    expect(page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")).to_be_visible()
    login_page.profile_img.click(timeout=30000)
    expect(page.locator("div[class='BingeBox-root css-xkdv7i']")).to_be_visible()





