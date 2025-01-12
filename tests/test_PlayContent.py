import re
from asyncio import timeout

from playwright.sync_api import Page, expect,sync_playwright
from playwright.sync_api import sync_playwright


def test_trailer_playback():
    with sync_playwright() as p:

        browser = p.chromium.launch(channel="chrome",headless=False)
        page = browser.new_page()


        page.goto("https://binge.buzz/")


        expect(page.locator("img[class='BingeBox-root css-16pcgwn']")).to_be_visible()
        page.get_by_label("close").click()
        page.get_by_label("Accept cookies").click()

        # Scroll to find the "Trailer" section

        page.evaluate("window.scrollBy(0, 1000)")
        page.locator("text='Trailer'").scroll_into_view_if_needed()
        page.get_by_text("Trailer ").highlight()

        #expect(page.get_by_text("Trailer ")).to_be_visible()
        page.get_by_text("Trailer ").click(timeout=1000000)

        expect(page).to_have_url(re.compile(r"https://binge.buzz/categories/498/vod/1"), timeout=10000)
        page.wait_for_timeout(2000)

        expect(page.get_by_role("heading", name="Trailer")).to_be_visible(timeout=10000)
        page.wait_for_timeout(2000)
        #page.mouse.move(1000, 100)
        page.locator("img[class='BingeBox-root css-1vqo5l9']").nth(2).hover(timeout=10000)
        #page.locator("img[class='BingeBox-root css-1vqo5l9']").nth(2).click()
        page.locator("button[class='BingeBtnBase-root css-1lo0mph']").click(timeout=5000)


        #expect(page.locator("#video_vdrm_html5_api")).to_be_visible(timeout=10000)
        page.locator("//div/div[2]/div[1]/button[1]/svg").click(timeout=5000)
        page.wait_for_timeout(50000)
        #page.locator("button[class='BingeBtnBase-root BingeIconBtn-root BingeIconBtn-sizeMedium css-tge1vt'][data-name='Play']").click(timeout=5000)
        page.wait_for_timeout(50000)




