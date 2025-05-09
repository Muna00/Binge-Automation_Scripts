from asyncio import timeout
import json
from playwright.sync_api import sync_playwright, expect
import re
from playwright.sync_api import Page
import conftest
from models.login import Login
from models.others import Player_Keys


def test_login_elementVisibility(page, load_config):
    login_page = Login(page, load_config)
    login_page.login_navigate()
    page.wait_for_timeout(1000)
    login_page.login_button.click()
    # login_page.login_visibility()

    expect(page.locator("div[class='BingeBox-root css-wgad3o']")).to_be_visible()
    expect(login_page.phone_number_field).to_be_visible()
    expect(login_page.generate_otp_button).to_be_visible()
    expect(login_page.fb_login_button).to_be_visible()
    expect(login_page.gmail_login_button).to_be_visible()
    expect(login_page.email_login_button).to_be_visible()
    expect(login_page.page.locator("u").filter(has_text="Privacy Notice")).to_be_visible()
    expect(login_page.page.locator("u").filter(has_text="Terms & Condition")).to_be_visible()
    page.wait_for_timeout(3000)





def test_OTP_valid_login(page, load_config):
    login_page = Login(page, load_config)
    login_page.login_navigate()
    login_page.otp_login()
    expect(page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")).to_be_visible()
    login_page.profile_img.click()
    page.wait_for_timeout(5000)
    expect(page.locator("div[class='BingeBox-root css-xkdv7i']")).to_be_visible()


def test_email_valid_login(page, load_config):
    login_page = Login(page, load_config)
    login_page.login_navigate()
    login_page.email_login()
    expect(page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")).to_be_visible()
    login_page.profile_img.click()
    page.wait_for_timeout(5000)
    expect(page.locator("div[class='BingeBox-root css-xkdv7i']")).to_be_visible()


def test_gmail_login(page, load_config):
    login_page = Login(page, load_config)
    login_page.login_navigate()
    login_page.gmail_login()
    page.wait_for_timeout(7000)
    expect(page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")).to_be_visible()
    login_page.profile_img.click(timeout=30000)
    page.wait_for_timeout(5000)
    expect(page.locator("div[class='BingeBox-root css-xkdv7i']")).to_be_visible()





