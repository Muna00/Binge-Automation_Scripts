
from playwright.sync_api import sync_playwright, expect
import re
from playwright.sync_api import Page
from models.login import Login
from models.others import Main, Search_Keyword, Click_Pages, Player_Keys


def test_player_keys_actions(page: Page):
    # Initialize Player_Keys object
    new_page = Player_Keys(page)

    # Perform login and navigation
    new_page.login_navigate()
    new_page.navigate_to_trailer_section()

    # Hover over the first content and verify preview window visibility
    page.locator("img[class='BingeBox-root css-1vqo5l9']").nth(0).hover(timeout=60000)
    expect(page.locator("div[class='BingeCardContent-root css-esr8dj']")).to_be_visible()
    page.wait_for_timeout(1000)

    # Click the play button
    page.locator("button[class='BingeBtnBase-root css-1lo0mph']").click()
    page.wait_for_timeout(1000)
    page.mouse.move(100, 100)



    # Wait for buttons to be available before checking visibility
    expect(new_page.pause_button).to_be_visible()
    expect(new_page.backward_button).to_be_visible()
    expect(new_page.forward_button).to_be_visible()
    expect(new_page.fullScreen).to_be_visible()

    # expect(new_page.volumeOFF).to_be_visible()
    expect(new_page.volumeON).to_be_visible()
    expect(new_page.back_button).to_be_visible()

    # Click the pause button

    page.mouse.move(100, 100)
    new_page.click_Pause()
    page.mouse.move(1001, 100)
    expect(new_page.play_button).to_be_visible()
    page.mouse.move(100,1001)
    new_page.click_Play()
    page.mouse.move(1004, 100)
    new_page.click_Forward()
    page.mouse.move(100, 1007)


    new_page.click_Backward()
    page.mouse.move(1004, 100)

    new_page.click_VolumeON()
    page.mouse.move(1009, 100)
    new_page.click_VolumeOff()
    page.mouse.move(100, 1004)



    new_page.click_FullScreen()
    expect(new_page.smallScreen).to_be_visible()
    new_page.click_SmallScreen()

    page.mouse.move(100, 100)
    new_page.click_Duration()
    new_page.click_BackButton()




 #def test_duration_key(page:Page):
     #< span

     #duration bar class ="BingeSlider-root BingeSlider-colorPrimary BingeSlider-sizeMedium css-1ud7vi0" > < span class ="BingeSlider-rail css-b04pc9" > < / span > < span class ="BingeSlider-track css-1t2bqnt" style="left: 0%; width: 34.4663%;" > < / span > < span data-index="0" data-focusvisible="false" class ="BingeSlider-thumb BingeSlider-thumbColorPrimary BingeSlider-thumbSizeMedium css-7drnjp" style="left: 34.4663%;" > < input data-index="0" aria-valuenow="58.660546" aria-orientation="horizontal" aria-valuemax="170.197" aria-valuemin="0" type="range" min="0" max="170.197" step="1" value="58.660546" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 100%; margin: -1px; overflow: hidden; padding: 0px; position: absolute; white-space: nowrap; width: 100%; direction: ltr;" > < span class ="BingeSlider-valueLabel css-16i7qf6" aria-hidden="true" > < span class ="BingeSlider-valueLabelCircle" > < span class ="BingeSlider-valueLabelLabel" > 00:58 <

     #BingeSlider-root BingeSlider-colorPrimary BingeSlider-sizeMedium css-1ud7vi0


     #class ="BingeSlider-valueLabelOpen BingeSlider-valueLabel css-16i7qf6" aria-hidden="true" > < span class ="BingeSlider-valueLabelCircle" > < span class ="BingeSlider-valueLabelLabel" > 00:41 <

