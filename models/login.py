import json
import re
from asyncio import timeout

from playwright.sync_api import Page, expect


class Login:
    def __init__(self, page, load_config):
        self.page = page
        self.page_url = load_config['url']

        # Store credentials from the loaded config
        self.credentials = load_config['credentials']

        # Element locators
        self.login_button = page.get_by_role("button", name="Login")
        self.phone_number_field = page.locator("input.PhoneInputInput")
        self.generate_otp_button = page.get_by_role("button", name="Generate OTP")
        self.first_otp = page.get_by_label("Please enter OTP character 1")
        self.second_otp = page.get_by_label("Please enter OTP character 2")
        self.third_otp = page.get_by_label("Please enter OTP character 3")
        self.fourth_otp = page.get_by_label("Please enter OTP character 4")

        self.fb_login_button = page.get_by_label("Login with Facebook")
        self.gmail_login_button = page.get_by_label("Login with Google")

        self.verify_button = page.locator("button.BingeBtnBase-root.css-mhiio4")
        self.profile_img = page.locator(
            "button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-fnsiv']")

        self.email_login_button = page.get_by_label("Login with Email")
        self.email_field = page.get_by_placeholder("Enter Email to Sign-in")
        self.pass_field = page.get_by_placeholder("Enter password")
        self.submit = page.get_by_role("button", name="Submit")

    def navigate(self):
        self.page.goto(self.page_url)

    def close_popups(self):
        close_popup_button = self.page.get_by_label("close")
        accept_cookies_button = self.page.locator('#rcc-confirm-button')

        if close_popup_button.is_visible():
            close_popup_button.click()

        if accept_cookies_button.is_visible():
            accept_cookies_button.click(timeout=1000)

    def login_navigate(self):
        self.navigate()
        self.page.wait_for_timeout(3000)
        self.close_popups()
        self.page.wait_for_timeout(1000)

    def login_visibility(self):
        self.login_button.click()
        expect(self.page.locator("div[class='BingeBox-root css-wgad3o']")).to_be_visible()
        expect(self.phone_number_field).to_be_visible()
        expect(self.generate_otp_button).to_be_visible()
        expect(self.fb_login_button).to_be_visible()
        expect(self.gmail_login_button).to_be_visible()
        expect(self.email_login_button).to_be_visible()
        expect(self.page.locator("u").filter(has_text="Privacy Notice")).to_be_visible()
        expect(self.page.locator("u").filter(has_text="Terms & Condition")).to_be_visible()
        self.page.wait_for_timeout(3000)

    def otp_login(self):
        # Fetch phone number and OTP from credentials
        phone_number = self.credentials['phone_number']
        otp = self.credentials['otp']

        self.login_button.click()
        self.phone_number_field.fill(phone_number)
        self.generate_otp_button.click()
        self.first_otp.fill(otp[0])
        self.second_otp.fill(otp[1])
        self.third_otp.fill(otp[2])
        self.fourth_otp.fill(otp[3])
        self.page.wait_for_timeout(2000)
        self.verify_button.click()
        self.page.wait_for_timeout(5000)

    def email_login(self):
        # Fetch email and password from credentials
        email = self.credentials['email']
        password = self.credentials['password']

        self.login_button.click()
        self.email_login_button.click()
        self.page.wait_for_timeout(5000)
        self.email_field.fill(email)
        self.page.wait_for_timeout(5000)
        self.pass_field.fill(password)
        self.submit.click()
        self.page.wait_for_timeout(5000)

    def gmail_login(self):
        self.login_button.click()
        self.gmail_login_button.click()


        with self.page.context.expect_page(timeout=60000) as new_page_info:
            self.page.wait_for_timeout(2000)  # Allow popup to load
            new_page = new_page_info.value
        new_page.locator("input[type='email']").fill(self.credentials['gmail_email'])
        new_page.locator("button:has-text('Next')").click()
        new_page.wait_for_timeout(5000)
        new_page.locator("input[type='password']").fill(self.credentials['gmail_password'])
        new_page.locator("button:has-text('Next')").click()



    def navigate_to_trailer_section(self):
        self.page.evaluate("window.scrollBy(0, 1000)")
        self.page.locator("text='Trailer'").scroll_into_view_if_needed()
        self.page.get_by_text("Trailer ").highlight()
        self.page.get_by_text("Trailer ").click(timeout=1000000)
        self.page.wait_for_timeout(2000)

    def check_payment_option_visibility(self):
        # Verifying the payment options' visibility
        #expect(self.page.get_by_role("region").get_by_text("Select payment methodbKashPay")).to_be_visible()
        expect(self.page.get_by_role("region").locator("div").filter(has_text="Pay using bKash").nth(2)).to_be_visible()
        expect(self.page.get_by_role("region").locator("div").filter(has_text="Pay using Robi/").nth(2)).to_be_visible()
        expect(self.page.get_by_role("region").locator("div").filter(has_text="Pay using Nagad").nth(2)).to_be_visible()
        expect(self.page.get_by_role("region").locator("div").filter(has_text="Card/MFS PaymentPay using").nth(
            2)).to_be_visible()

    def bkash_to_Login_redirection(self):
        self.page.get_by_role("region").locator("div").filter(has_text="Pay using bKash").nth(2).click()
        expect(self.page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
        expect(self.page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
        self.page.locator("button[class='BingeBtnBase-root css-4x9eju']").click()
        self.page.wait_for_timeout(1000)
        expect(self.page).to_have_url(re.compile("https://binge.buzz/login"))  # login redirection
        self.page.go_back()

    def dob_to_Login_redirection(self):
        self.page.get_by_role("region").locator("div").filter(has_text="Pay using Robi/").nth(2).click()
        expect(self.page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
        expect(self.page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
        self.page.locator("button[class='BingeBtnBase-root css-4x9eju']").click()
        self.page.wait_for_timeout(1000)

        expect(self.page).to_have_url(re.compile("https://binge.buzz/login"))  # login redirection
        self.page.go_back()

    def nagad_to_Login_redirection(self):
        self.page.get_by_role("region").locator("div").filter(has_text="Pay using Nagad").nth(2).click()
        expect(self.page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
        expect(self.page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
        self.page.locator("button[class='BingeBtnBase-root css-4x9eju']").click()
        self.page.wait_for_timeout(1000)
        expect(self.page).to_have_url(re.compile("https://binge.buzz/login"))  # login redirection
        self.page.go_back()

    def card_to_Login_redirection(self):
        self.page.get_by_role("region").locator("div").filter(has_text="Card/MFS PaymentPay using").nth(2).click()
        expect(self.page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
        expect(self.page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
        self.page.locator("button[class='BingeBtnBase-root css-4x9eju']").click()
        self.page.wait_for_timeout(1000)
        expect(self.page).to_have_url(re.compile("https://binge.buzz/login"))  # login redirection
        self.page.go_back()

    def subscription_to_loginPrompt_cancel(self):  # DO NOT RUN THIS TEST

        self.page.get_by_role("region").locator("div").filter(has_text="Pay using bKash").nth(2).click()
        expect(self.page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
        expect(self.page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
        expect(self.page.get_by_role("button", name="Cancel")).to_be_visible()
        self.page.get_by_role("button", name="Cancel").click()

        self.page.get_by_role("region").locator("div").filter(has_text="Pay using Robi/").nth(2).click()
        expect(self.page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
        expect(self.page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
        expect(self.page.get_by_role("button", name="Cancel")).to_be_visible()
        self.page.get_by_role("button", name="Cancel").click()

        self.page.get_by_role("region").locator("div").filter(has_text="Pay using Nagad").nth(2).click()
        expect(self.page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
        expect(self.page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
        expect(self.page.get_by_role("button", name="Cancel")).to_be_visible()
        self.page.get_by_role("button", name="Cancel").click()

        self.page.get_by_role("region").locator("div").filter(has_text="Card/MFS PaymentPay using").nth(2).click()
        expect(self.page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
        expect(self.page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
        expect(self.page.get_by_role("button", name="Cancel")).to_be_visible()
        self.page.get_by_role("button", name="Cancel").click()


