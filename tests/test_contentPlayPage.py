
from playwright.sync_api import sync_playwright, expect
import re
from playwright.sync_api import Page
from models.login import Login
from models.others import Main, Search_Keyword, Click_Pages, Player_Keys



def test_player_keys_actions(page: Page):
    new_page = Player_Keys(page)
    new_page.set_prerequisites()

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
    expect(new_page.play_button).to_be_visible()
    new_page.click_Play()
    new_page.click_Forward()
    new_page.click_Backward()
    new_page.click_VolumeON()
    new_page.click_VolumeOff()

    new_page.click_FullScreen()
    expect(new_page.smallScreen).to_be_visible()
    new_page.click_SmallScreen()

    new_page.click_Duration()
    new_page.click_BackButton()
    expect(page).to_have_url(re.compile(r"https://binge.buzz/categories/498/vod/1"))




 #def test_duration_key(page:Page):
     #< span

     #duration bar class ="BingeSlider-root BingeSlider-colorPrimary BingeSlider-sizeMedium css-1ud7vi0" > < span class ="BingeSlider-rail css-b04pc9" > < / span > < span class ="BingeSlider-track css-1t2bqnt" style="left: 0%; width: 34.4663%;" > < / span > < span data-index="0" data-focusvisible="false" class ="BingeSlider-thumb BingeSlider-thumbColorPrimary BingeSlider-thumbSizeMedium css-7drnjp" style="left: 34.4663%;" > < input data-index="0" aria-valuenow="58.660546" aria-orientation="horizontal" aria-valuemax="170.197" aria-valuemin="0" type="range" min="0" max="170.197" step="1" value="58.660546" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 100%; margin: -1px; overflow: hidden; padding: 0px; position: absolute; white-space: nowrap; width: 100%; direction: ltr;" > < span class ="BingeSlider-valueLabel css-16i7qf6" aria-hidden="true" > < span class ="BingeSlider-valueLabelCircle" > < span class ="BingeSlider-valueLabelLabel" > 00:58 <

     #BingeSlider-root BingeSlider-colorPrimary BingeSlider-sizeMedium css-1ud7vi0


     #class ="BingeSlider-valueLabelOpen BingeSlider-valueLabel css-16i7qf6" aria-hidden="true" > < span class ="BingeSlider-valueLabelCircle" > < span class ="BingeSlider-valueLabelLabel" > 00:41 <


#these test verifies if the forward,backward, and duration bar action reflects the time change
def test_forward_verification(page:Page):
    new_page = Player_Keys(page)
    new_page.set_prerequisites()

    # first e pause kore nibo jeno timestamp neya jay
    new_page.click_Pause()
    initial_time = new_page.get_timestamp()
    new_page.click_Forward()
    page.wait_for_timeout(1000)
    new_time = new_page.get_timestamp()
    assert initial_time - new_time == 10



def test_backward_verification(page:Page):
    new_page = Player_Keys(page)
    new_page.set_prerequisites()
    new_page.click_Duration()
    # first e pause kore nibo jeno timestamp neya jay
    new_page.click_Pause()
    initial_time = new_page.get_timestamp()
    new_page.click_Backward()
    page.wait_for_timeout(1000)
    new_time = new_page.get_timestamp()
    assert new_time - initial_time == 10


def test_drag_difference(page:Page):
    new_page = Player_Keys(page)
    new_page.set_prerequisites()

    # first e pause kore nibo jeno timestamp neya jay
    new_page.click_Pause()
    ini_timestamp = new_page.get_timestamp()
    new_page.click_Duration()
    page.wait_for_timeout(1000)
    new_timestamp = new_page.get_timestamp()

    assert new_timestamp != ini_timestamp





def test_drag_verification(page:Page):
    new_page = Player_Keys(page)
    new_page.set_prerequisites()
    page.wait_for_timeout(5000)


    new_page.click_Pause()
    new_page.click_Duration()
    new_page.hoverOverCircle()
    page.wait_for_timeout(1000)
    ini_timestamp = new_page.get_timestamp()
    ini_cursor_time=new_page.get_cursorTimeStamp()
    new_page.click_Duration()
    new_page.hoverOverCircle()
    page.wait_for_timeout(1000)
    new_cursor_time = new_page.get_cursorTimeStamp()
    new_timestamp = new_page.get_timestamp()
    assert ini_cursor_time + ini_timestamp == new_cursor_time + new_timestamp

