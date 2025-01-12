from asyncio import wait_for
from re import search

from playwright.sync_api import sync_playwright, expect
import re
from playwright.sync_api import Page
from models.login import Login
from models.others import Main, Search_Keyword, Click_Pages


def test_visible_clickable(page: Page):
    new_page = Login(page)
    new_page.navigate()
    new_page.close_popups()

    # Header part

    expect(page.get_by_role("link", name="Home")).to_be_visible()
    page.get_by_role("link", name="Home").click()
    expect(page).to_have_url("https://binge.buzz/")

    expect(page.get_by_role("link", name="Binge Logo")).to_be_visible()
    page.get_by_role("link", name="Binge Logo").click()
    expect(page).to_have_url("https://binge.buzz/")

    expect(page.get_by_role("link", name="Sports", exact=True)).to_be_visible()
    page.get_by_role("link", name="Sports", exact=True).click()
    expect(page).to_have_url("https://binge.buzz/sports")

    expect(page.get_by_role("link", name="Movies", exact=True)).to_be_visible()
    page.get_by_role("link", name="Movies", exact=True).click()
    expect(page).to_have_url("https://binge.buzz/movies")

    expect(page.get_by_role("link", name="Series")).to_be_visible()
    page.get_by_role("link", name="Series", exact=True).click()
    expect(page).to_have_url("https://binge.buzz/series")

    expect(page.get_by_role("link", name="Favourites")).to_be_visible()
    page.get_by_role("link", name="Favourites", exact=True).click()
    expect(page).to_have_url("https://binge.buzz/login")

    expect(page.get_by_role("button", name="Subscribe Now")).to_be_visible()
    page.get_by_role("button", name="Subscribe Now").click()
    expect(page).to_have_url("https://binge.buzz/subscription")
    expect(page.get_by_role("button", name="Login to view")).to_be_visible()
    expect(page.get_by_text("Already Subscribed?")).to_be_visible()



    expect(page.get_by_test_id("SearchIcon")).to_be_visible()
    page.get_by_test_id("SearchIcon").click()
    expect(page.get_by_placeholder("Search Shows and Movies...")).to_be_visible()

# Login page links

    expect(page.locator("button[class='BingeBtnBase-root css-8xcdnj']")).to_be_visible()
    page.locator("button[class='BingeBtnBase-root css-8xcdnj']").click()
    expect(page).to_have_url("https://binge.buzz/login")

    expect(page.locator("xpath=//*[@id='root']/div[1]/div[1]/div/div/div/p[2]/u[1]")).to_be_visible()
    page.locator("xpath=//*[@id='root']/div[1]/div[1]/div/div/div/p[2]/u[1]").click()
    expect(page).to_have_url("https://binge.buzz/privacy-policy")


    page.locator("button[class='BingeBtnBase-root css-8xcdnj']").click()
    expect(page.locator("xpath=//*[@id='root']/div[1]/div[1]/div/div/div/p[2]/u[2]")).to_be_visible()
    page.locator("xpath=//*[@id='root']/div[1]/div[1]/div/div/div/p[2]/u[2]").click()
    expect(page).to_have_url("https://binge.buzz/terms-conditions")

    footer_links = {
        "facebook": {
            "xpath": "//*[@id='root']/footer/div/div[1]/div[1]/a[1]",
            "expected_url": "https://www.facebook.com/binge.buzz"
        },
        "instagram": {
            "xpath": "//*[@id='root']/footer/div/div[1]/div[1]/a[2]",
            "expected_url": "https://www.instagram.com/binge.buzz/?hl=en"
        },
        "twitter": {
            "xpath": "//*[@id='root']/footer/div/div[1]/div[1]/a[3]",
            "expected_url": "https://x.com/"

        },
        "youtube": {
            "xpath": "//*[@id='root']/footer/div/div[1]/div[1]/a[4]",
            "expected_url": "https://www.youtube.com/c/BingeBangladesh"
        },
        "tiktok": {
            "xpath": "//*[@id='root']/footer/div/div[1]/div[1]/a[5]",
            "expected_url": "https://www.tiktok.com/@binge.buzz?_t=8iAbH9xNbv7&_r=1"
        },

        "terms": {
            "xpath": "//*[@id='root']/footer/div/ul/li[1]/a",
            "expected_url": "https://binge.buzz/terms-conditions"
        },
        "privacy": {
            "xpath": "//*[@id='root']/footer/div/ul/li[2]/a",
            "expected_url": "https://binge.buzz/privacy-policy"
        },
        "FAQ": {
            "xpath": "//*[@id='root']/footer/div/ul/li[3]/a",
            "expected_url": "https://binge.buzz/faq-content"
        },
        "redeem": {
            "xpath": "//*[@id='root']/footer/div/ul/li[4]/a",
            "expected_url": "https://binge.buzz/login"
        },
        "playstore": {
            "xpath": "//*[@id='root']/footer/div/div[1]/div[2]/img[1]",
            "expected_url": "https://play.google.com/store/apps/details?id=buzz.binge.mobile"
        },
        "appstore": {
            "xpath": "//*[@id='root']/footer/div/div[1]/div[2]/img[2]",
            "expected_url": "https://apps.apple.com/us/app/binge-bd/id1529394367"
        }
    }

    # Iterate through each social media link
    for platform, details in footer_links.items():
        locator = page.locator(f"xpath={details['xpath']}")
        expect(locator).to_be_visible()
        locator.click()


        if platform == "playstore" or platform == "appstore":
            with page.expect_popup() as popup_info:
                locator.click()
            new_page = popup_info.value

            # Verify the redirection URL
            expect(new_page).to_have_url(details['expected_url'])
            print(f"Verified URL for {platform}: {details['expected_url']}")

            # Close the new tab after verification
            new_page.close()
        elif platform == "twitter":
            # Wait briefly to capture the URL before redirection
            page.wait_for_timeout(1000)

        else:
            # For other platforms, wait for the full navigation to the expected URL
            page.wait_for_url(details['expected_url'])
            expect(page).to_have_url(details['expected_url'])

        # Navigate back to the original page
        page.go_back()



def test_banner_visible(page:Page):
    new_page=Click_Pages(page)
    page.wait_for_timeout(10000)
    new_page.login_navigate()
    page.wait_for_timeout(10000)


    pages_to_click = [
        new_page.click_Home,
        new_page.click_Sports,
        new_page.click_Movies,
        new_page.click_Series,
    ]

    # Locator to expect on each page
    expected_locator = "div[class='slick-slider slick-initialized']"

    # Loop through each page method
    for page_method in pages_to_click:
        page_method()  # Call the page method
        expect(page.locator(expected_locator)).to_be_visible()

#if slider button available then it is clickable or not


def test_free_content_play(page: Page):
    new_page = Login(page)
    new_page.navigate()
    new_page.close_popups()
    page.wait_for_timeout(1000)
    new_page.navigate_to_trailer_section()

    expect(page).to_have_url(re.compile(r"https://binge.buzz/categories/498/vod/1"), timeout=10000)
    page.locator("img[class='BingeBox-root css-1vqo5l9']").nth(1).hover(timeout=60000) # hover over the 2nd content
    expect(page.locator("div[class='BingeCardContent-root css-esr8dj']")).to_be_visible() #Preview window visible
    expect(page.locator("button[class='BingeBtnBase-root css-1lo0mph']")).to_be_visible() #play button visible
    expect(page.locator("button[class='BingeBtnBase-root css-1qw26fx']")).to_be_visible() #more info button visible
    page.wait_for_timeout(1000)
    page.locator("button[class='BingeBtnBase-root css-1qw26fx']").click() #more info button click
    expect(page.locator("div[class='BingeDialogContent-root css-1yh5k5c']")).to_be_visible() #content playing preview page
    expect(page.locator("button[class='BingeBtnBase-root css-2j7f05']")).to_be_visible()#play button
    expect(page.locator("button[class='BingeBtnBase-root css-z1ehuj']")).to_be_visible()# favorite button

    page.locator("button[class='BingeBtnBase-root css-2j7f05']").click() #play button click
    expect(page).to_have_url(re.compile("https://binge.buzz/playing-vod/")) #content playing page redirect
    page.go_back()

    expect(page).to_have_url(re.compile(r"https://binge.buzz/categories/498/vod/1"), timeout=10000)
    page.wait_for_timeout(2000)

    page.locator("img[class='BingeBox-root css-1vqo5l9']").nth(3).hover(timeout=60000)  # hover over the 2nd content
    expect(page.locator("div[class='BingeCardContent-root css-esr8dj']")).to_be_visible() #Preview window visible
    page.wait_for_timeout(1000)

    page.locator("button[class='BingeBtnBase-root css-1lo0mph']").click()
    page.go_back()



def test_premium_content_play(page: Page):
    new_page = Login(page)
    new_page.navigate()
    new_page.close_popups()
    new_page.navigate_to_trailer_section()

    expect(page).to_have_url(re.compile("https://binge.buzz/categories/498/vod/1"), timeout=10000)
    page.locator("img[class='BingeBox-root css-1vqo5l9']").nth(0).hover(timeout=60000)  # hover over the 2nd content
    expect(page.locator("div[class='BingeCardContent-root css-esr8dj']")).to_be_visible()  # Preview window visible

    expect(page.locator("button[class='BingeBtnBase-root css-1lo0mph']")).to_be_visible()  # play button visible
    expect(page.locator("button[class='BingeBtnBase-root css-1qw26fx']")).to_be_visible()  # more info button visible
    page.wait_for_timeout(1000)

    page.locator("button[class='BingeBtnBase-root css-1qw26fx']").click()  # more info button click
    expect(page.locator("div[class='BingeDialogContent-root css-1yh5k5c']")).to_be_visible()  # content playing preview page
    expect(page.locator("button[class='BingeBtnBase-root css-2j7f05']")).to_be_visible()  # play button
    expect(page.locator("button[class='BingeBtnBase-root css-z1ehuj']")).to_be_visible()  # favorite button

    page.locator("button[class='BingeBtnBase-root css-2j7f05']").click()  # play button click
    expect(page).to_have_url(re.compile(r"https://binge.buzz/subscription\?contentID=\d+&contentType=vod"), timeout=10000)



def test_add_to_favorites(page:Page):
    new_page = Login(page)
    new_page.navigate()
    new_page.close_popups()
    new_page.navigate_to_trailer_section()

    expect(page).to_have_url(re.compile("https://binge.buzz/categories/498/vod/1"), timeout=10000)
    page.locator("img[class='BingeBox-root css-1vqo5l9']").nth(0).hover(timeout=60000)  # hover over the 2nd content
    expect(page.locator("div[class='BingeCardContent-root css-esr8dj']")).to_be_visible()  # Preview window visible

    expect(page.locator("button[class='BingeBtnBase-root css-1lo0mph']")).to_be_visible()  # play button visible
    expect(page.locator("button[class='BingeBtnBase-root css-1qw26fx']")).to_be_visible()  # more info button visible
    page.wait_for_timeout(1000)
    page.locator("button[class='BingeBtnBase-root css-1qw26fx']").click()
    page.locator("button[class='BingeBtnBase-root css-z1ehuj']").click()# favourite
    expect(page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()#login prompt
    expect(page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()#login button
    expect(page.get_by_role("button", name= "Cancel")).to_be_visible()
    page.get_by_role("button", name="Cancel").click()
    page.locator("button[class='BingeBtnBase-root css-z1ehuj']").click()
    page.locator("button[class='BingeBtnBase-root css-4x9eju']").click()#login button
    expect(page).to_have_url(re.compile("https://binge.buzz/login"))#login redirection




# to check if anon user can get the login prompt upon clicking the payment options and then click Cancel button
#this is to check if an anon user is getting the login prompt, and to cancel the prompt to carry on with the login prompt  appearance
def test_subscription_to_loginPrompt_cancel(page:Page):
    page.get_by_role("region").get_by_text("Select payment methodbKashPay")
    page.get_by_role("region").locator("div").filter(has_text="Pay using bKash").nth(2).click()
    expect(page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
    expect(page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
    expect(page.get_by_role("button", name="Cancel")).to_be_visible()
    page.get_by_role("button", name="Cancel").click()

    page.get_by_role("region").locator("div").filter(has_text="Pay using Robi/").nth(2).click()
    expect(page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
    expect(page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
    expect(page.get_by_role("button", name="Cancel")).to_be_visible()
    page.get_by_role("button", name="Cancel").click()

    page.get_by_role("region").locator("div").filter(has_text="Pay using Nagad").nth(2).click()
    expect(page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
    expect(page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
    expect(page.get_by_role("button", name="Cancel")).to_be_visible()
    page.get_by_role("button", name="Cancel").click()

    page.get_by_role("region").locator("div").filter(has_text="Card/MFS PaymentPay using").nth(2).click()
    expect(page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()  # login prompt
    expect(page.locator("button[class='BingeBtnBase-root css-4x9eju']")).to_be_visible()  # login button
    expect(page.get_by_role("button", name="Cancel")).to_be_visible()
    page.get_by_role("button", name="Cancel").click()


# to check if anon user can get the login prompt upon clicking the payment options and then click Cancel button
#this is to check if an anon user is redirecting to login page from every subscription packs
def test_subscription_to_loginPage_Redirection(page:Page):

    new_page = Login(page)
    new_page.navigate()
    new_page.close_popups()
    page.locator("button[class='BingeBtnBase-root css-1fjopj8']").click()

    page.get_by_role("button", name="Daily Pack 3 Devices Login").get_by_role("button").click()
    new_page.bkash_to_Login_redirection()
    page.get_by_role("button", name="Daily Pack 3 Devices Login").get_by_role("button").click()
    new_page.dob_to_Login_redirection()
    page.get_by_role("button", name="Daily Pack 3 Devices Login").get_by_role("button").click()
    new_page.nagad_to_Login_redirection()
    page.get_by_role("button", name="Daily Pack 3 Devices Login").get_by_role("button").click()
    new_page.card_to_Login_redirection()

    page.get_by_role("button", name="Weekly Pack 3 Devices Login").get_by_role("button").click()
    new_page.bkash_to_Login_redirection()
    page.get_by_role("button", name="Weekly Pack 3 Devices Login").get_by_role("button").click()
    new_page.dob_to_Login_redirection()
    page.get_by_role("button", name="Weekly Pack 3 Devices Login").get_by_role("button").click()
    new_page.nagad_to_Login_redirection()
    page.get_by_role("button", name="Weekly Pack 3 Devices Login").get_by_role("button").click()
    new_page.card_to_Login_redirection()

    page.get_by_role("button", name="Monthly Pack 3 Devices Login").get_by_role("button").click()
    new_page.bkash_to_Login_redirection()
    page.get_by_role("button", name="Monthly Pack 3 Devices Login").get_by_role("button").click()
    new_page.dob_to_Login_redirection()
    page.get_by_role("button", name="Monthly Pack 3 Devices Login").get_by_role("button").click()
    new_page.nagad_to_Login_redirection()
    page.get_by_role("button", name="Monthly Pack 3 Devices Login").get_by_role("button").click()
    new_page.card_to_Login_redirection()

    page.get_by_role("button", name="6-Month Pack 3 Devices Login").get_by_role("button").click()
    new_page.bkash_to_Login_redirection()
    page.get_by_role("button", name="6-Month Pack 3 Devices Login").get_by_role("button").click()
    new_page.dob_to_Login_redirection()
    page.get_by_role("button", name="6-Month Pack 3 Devices Login").get_by_role("button").click()
    new_page.nagad_to_Login_redirection()
    page.get_by_role("button", name="6-Month Pack 3 Devices Login").get_by_role("button").click()
    new_page.card_to_Login_redirection()




def test_anon_subscription(page:Page):
    #This tests the visibility and login prompt appearance of subscription packs and voucher redeem

    new_page = Login(page)
    new_page.navigate()
    new_page.close_popups()

    #anon user subscription assertions
    page.locator("button[class='BingeBtnBase-root css-1fjopj8']").click()
    expect(page).to_have_url(re.compile("https://binge.buzz/subscription"))
    expect(page.get_by_text("Already Subscribed?")).to_be_visible()
    expect(page.get_by_role("button",name="Login to view")).to_be_visible()

    expect(page.locator(".BingeBox-root > .BingePaper-root").first).to_be_visible()
    expect(page.get_by_role("button", name="Daily Pack 3 Devices Login").get_by_role("button")).to_be_visible()
    page.get_by_role("button", name="Daily Pack 3 Devices Login").get_by_role("button").click()
    new_page.check_payment_option_visibility()
    test_subscription_to_loginPrompt_cancel(page)

    expect(page.locator(".BingeBox-root > div:nth-child(2) > .BingePaper-root")).to_be_visible()
    expect(page.get_by_role("button", name="Weekly Pack 3 Devices Login").get_by_role("button")).to_be_visible()
    page.get_by_role("button", name="Weekly Pack 3 Devices Login").get_by_role("button").click()
    new_page.check_payment_option_visibility()
    test_subscription_to_loginPrompt_cancel(page)

    expect(page.locator("div:nth-child(3) > .BingePaper-root")).to_be_visible()
    expect(page.get_by_role("button", name="Monthly Pack 3 Devices Login").get_by_role("button")).to_be_visible()
    page.get_by_role("button", name="Monthly Pack 3 Devices Login").get_by_role("button").click()
    new_page.check_payment_option_visibility()
    test_subscription_to_loginPrompt_cancel(page)
    new_page.check_payment_option_visibility()


    expect(page.locator("div:nth-child(4) > .BingePaper-root")).to_be_visible()
    expect(page.get_by_role("button", name="6-Month Pack 3 Devices Login").get_by_role("button")).to_be_visible()
    page.get_by_role("button", name="6-Month Pack 3 Devices Login").get_by_role("button").click()
    expect(page.get_by_role("button", name="Redeem")).to_be_visible()
    new_page.check_payment_option_visibility()
    test_subscription_to_loginPrompt_cancel(page)


    expect(page.get_by_placeholder("Enter Your Coupon here")).to_be_visible()
    expect(page.locator("button[class='BingeBtnBase-root css-hnz8d1']")).to_be_visible()
    page.locator("button[class='BingeBtnBase-root css-hnz8d1']").click()
    expect(page.locator("div[class='BingeBox-root css-1bw55l2']")).to_be_visible()



#this test checks, of the search icon is clickable,after searching, redirecting to search results page, and displays all the matched content
def test_search_option(page:Page):
    pre=Login(page)
    pre.login_navigate()

    main=Main(page)
    main.search_navigate()


    search_result_cards = page.locator(".BingeBox-root.css-1vqo5l9")
    result_count = search_result_cards.count()

    assert result_count > 0, "No search results found."


    for i in range(result_count):
        card = search_result_cards.nth(i)
        card.hover(timeout=5000)
        page.wait_for_timeout(5000)

        expect(page.locator("#root")).to_contain_text(re.compile("prohelika", re.IGNORECASE))



#should fail as for now this
def test_blank_search(page:Page):
    bl=Login(page)
    bl.login_navigate()
    blank=Search_Keyword(page)
    search_keyword=blank.blank_search_keyword()
    blank.search_navigate(search_keyword)


def test_wrong_search(page:Page):
    wro=Login(page)
    wro.login_navigate()
    wrong=Search_Keyword(page)
    search_keyword=wrong.wrong_search_keyword()
    wrong.search_navigate(search_keyword)

    search_result_cards = page.locator(".BingeBox-root.css-1vqo5l9")
    result_count = search_result_cards.count()
    assert result_count==0
    expect(page.get_by_role("heading", name="NO RECORDS FOUND")).to_be_visible()

def test_anon_PremiumContentPlayFromSearch(page:Page):
    pre=Login(page)
    pre.login_navigate()
    premium = Search_Keyword(page)
    search_keyword = premium.premium_search_keyword()
    premium.search_navigate(search_keyword)
    search_result_cards = page.locator(".BingeBox-root.css-1vqo5l9")  # Ensure this matches the actual card locator
    result_count = search_result_cards.count()
    assert result_count > 0, "No search results found."

    for i in range(result_count):
        card = search_result_cards.nth(i)
        card.hover(timeout=5000)
        page.wait_for_timeout(5000)

        title_locator = page.locator("div[class='BingeBox-root css-qsm21h']")
        if title_locator.text_content().strip() == search_keyword:

            play_button =page.locator("button[class='BingeBtnBase-root css-1lo0mph']")
            expect(play_button).to_be_visible()
            play_button.click()
            expect(page).to_have_url(re.compile(r"https://binge.buzz/subscription\?contentID=\d+&contentType=vod"),
                                     timeout=10000)
            break
    else:
        raise AssertionError(f"No content title matched the keyword '{search_keyword}'")




def test_anon_FreeContentPlayFromSearch(page:Page):
    pre = Login(page)
    pre.login_navigate()
    free = Search_Keyword(page)
    search_keyword = free.free_search_keyword()
    free.search_navigate(search_keyword)

    search_result_cards = page.locator(".BingeBox-root.css-1vqo5l9")  # Ensure this matches the actual card locator
    result_count = search_result_cards.count()
    assert result_count > 0, "No search results found."

    for i in range(result_count):
        card = search_result_cards.nth(i)
        card.hover(timeout=5000)
        page.wait_for_timeout(5000)

        title_locator = page.locator("div[class='BingeBox-root css-qsm21h']")
        if title_locator.text_content().strip() == search_keyword:

            play_button =page.locator("button[class='BingeBtnBase-root css-1lo0mph']")
            expect(play_button).to_be_visible()
            play_button.click()
            expect(page).to_have_url(re.compile(r"https://binge.buzz/playing-vod/6087"),
                                     timeout=10000)
            break
    else:
        raise AssertionError(f"No content title matched the keyword '{search_keyword}'")









