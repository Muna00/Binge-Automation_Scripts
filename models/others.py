import re
from playwright.sync_api import Page, expect
from models.login import Login



# Base class for shared methods
class Main(Login):
    # def __init__(self, page: Page):
    #     super().__init__(page)
    # def close_all_popups(self):
    #     self.close_popups()


    def search_navigate(self, search_keyword: str):
        # Click the search icon
        search_icon = self.page.locator("svg[class='BingeSvgIcon-root BingeSvgIcon-fontSizeMedium css-4rspxq']")
        search_icon.click()

        # Access the search bar
        search_bar = self.page.get_by_placeholder("Search Shows and Movies...")
        expect(search_bar).to_be_visible()
        search_bar.click()

        # Enter the search keyword
        search_bar.fill(search_keyword)
        search_bar.press("Enter")

        # Verify navigation to the search results page
        search_result_page = "https://binge.buzz/search-result"
        expect(self.page).to_have_url(search_result_page)
        self.page.wait_for_timeout(1000)


# Child class for premium search
class Search_Keyword(Main):
    def premium_search_keyword(self):
        # Return a predefined search keyword for premium content
        return "Shodor Ghater Tiger S1 E5"


    def free_search_keyword(self):
        # Return a predefined search keyword for premium content
        return "Prohelika Trailer"


    def blank_search_keyword(self):
        return " "

    def wrong_search_keyword(self):
        return "ararar"


class Click_Pages(Main):
    def click_Home(self):
        home=self.page.get_by_role("link", name="Home")
        home.click()
        expect(home).to_be_visible()


    def click_Sports(self):
        sports=self.page.get_by_role("link", name="Sports", exact=True)
        sports.click()
        expect(sports).to_be_visible()

    def click_Movies(self):
        movies=self.page.locator('a[href="/movies"]')
        movies.click()
        expect(movies).to_be_visible()

    def click_Series(self):
        series = self.page.locator('a[href="/series"]')
        series.click()
        expect(series).to_be_visible()

    def click_Favorites(self):
        favorites = self.page.get_by_role("link", name="Favourites")
        favorites.click()
        expect(favorites).to_be_visible()

    def click_Subscribe(self):
        subscribe = self.page.get_by_role("link", name="Subscribe Now")
        subscribe.click()
        expect(subscribe).to_be_visible()


class Player_Keys(Click_Pages):
        def __init__(self, page: Page):
            # Ensure the parent class is initialized correctly
            super().__init__(page)
            # Initialize play and pause buttons
            self.play_button = page.locator("svg[data-name='Play']")
            self.pause_button = page.locator('svg[data-name="Pause"]')
            self.backward_button=page.locator("svg[data-name='Back10']")
            self.forward_button = page.locator("svg[data-name='Forward10']")
            self.volumeON= page.locator("svg[data-name='VolumeHigh']")
            self.volumeOFF = page.locator("svg[data-name='VolumeOff']")
            self.fullScreen = page.locator("svg[data-name='FullscreenEnter']")
            self.smallScreen = page.locator("svg[data-name='FullscreenExit']")
            self.back_button=page.locator("svg[data-testid='KeyboardBackspaceIcon']")
            self.duration_point = page.locator("span[class='BingeSlider-valueLabelOpen BingeSlider-valueLabel css-16i7qf6']")





        def click_Play(self):
            # Click the Play button
            self.play_button.click()

        def click_Pause(self):
            # Click the Pause button
            self.pause_button.click()

        def click_Backward(self):
            self.backward_button.click()

        def click_Forward(self):
            self.forward_button.click()

        def click_VolumeON(self):
            self.volumeON.click()

        def click_VolumeOff(self):
            self.volumeOFF.click()

        def click_FullScreen(self):
            self.fullScreen.click()

        def click_SmallScreen(self):
            self.smallScreen.click()

        def click_BackButton(self):
            self.back_button.click()

        def click_Duration(self):
            self.duration_point.click()








