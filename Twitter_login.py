from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time


def twitter_login(driver: WebDriver):

    driver.get("https://twitter.com")
    driver.delete_all_cookies()

    # print the cookies before login to Twitter
    time.sleep(30)
    print("----------------------------------------------------------------------------------------------------")
    cookies_before_login = driver.get_cookies()
    print(cookies_before_login)

    # get the Twitter login cookies through pre-login. Then we can achieve Twitter auto-login without manual login
    # by adding the login cookies to the web-driver.
    cookies_list = [{'value': 'side_no_out', 'secure': True, 'path': '/', 'domain': '.twitter.com', 'name': 'rweb_optin', 'expiry': 1617544471.573509, 'httpOnly': False},
                    {'value': 'zh-cn', 'secure': False, 'path': '/', 'domain': 'twitter.com', 'name': 'lang', 'httpOnly': False},
                    {'value': '1', 'secure': True, 'path': '/', 'sameSite': 'Lax', 'domain': '.twitter.com', 'name': 'csrf_same_site', 'expiry': 1617544471.57352, 'httpOnly': True},
                    {'value': '31e98272625787caebde42abf8673497', 'secure': True, 'path': '/', 'domain': '.twitter.com', 'name': 'ct0', 'expiry': 1586030052.046615, 'httpOnly': False},
                    {'value': '57d736bfb321267777f2bca617fca1a2ce90e56b', 'secure': True, 'path': '/', 'sameSite': 'None', 'domain': '.twitter.com', 'name': 'auth_token', 'expiry': 1743688471.388384, 'httpOnly': True},
                    {'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCILidUVxAToMY3NyZl9p%250AZCIlODY4YzRiZTJmY2VhMGU0YzZkY2FkMjliZjNiZWEyZDc6B2lkIiU4N2Ew%250AMDk5NTAzMDVjOGViZDcwMDBkOTFiOTQwNzQ5MzoJdXNlcmwrCQBA1WjQjF4N--58f3589ccb9816c0be040325f395a876702a1d0c', 'secure': True, 'path': '/', 'domain': '.twitter.com', 'name': '_twitter_sess', 'httpOnly': True},
                    {'value': 'u6mq1Ssxy5vbC7Y3vcrRpWT3mFU2qbejoAiba1Bw', 'secure': True, 'path': '/', 'domain': '.twitter.com', 'name': 'kdt', 'expiry': 1633269271.388329, 'httpOnly': True},
                    {'value': '"HBERAAA="', 'secure': True, 'path': '/', 'sameSite': 'None', 'domain': '.twitter.com', 'name': 'ads_prefs', 'expiry': 1743688471.388313, 'httpOnly': False},
                    {'value': '1', 'secure': True, 'path': '/', 'domain': '.twitter.com', 'name': 'csrf_same_site_set', 'expiry': 1617458071.57349, 'httpOnly': True},
                    {'value': '1', 'secure': True, 'path': '/', 'domain': '.twitter.com', 'name': 'remember_checked_on', 'expiry': 1743688471.388341, 'httpOnly': False},
                    {'value': 'GA1.2.861290180.1586008455', 'secure': False, 'path': '/', 'domain': '.twitter.com', 'name': '_ga', 'expiry': 1649080477, 'httpOnly': False},
                    {'value': 'u%3D963362197043757056', 'secure': True, 'path': '/', 'sameSite': 'None', 'domain': '.twitter.com', 'name': 'twid', 'expiry': 1743688472.755386, 'httpOnly': False},
                    {'value': 'v1%3A158600828128770440', 'secure': True, 'path': '/', 'sameSite': 'None', 'domain': '.twitter.com', 'name': 'guest_id', 'expiry': 1649080453.835578, 'httpOnly': False},
                    {'value': '1', 'secure': True, 'path': '/', 'domain': 'twitter.com', 'name': '_sl', 'expiry': 1586094854, 'httpOnly': False},
                    {'value': 'GA1.2.1726043265.1586008455', 'secure': False, 'path': '/', 'domain': '.twitter.com', 'name': '_gid', 'expiry': 1586094877, 'httpOnly': False},
                    {'value': '"v1_8oLkDLcXLS64joUkzp2/CA=="', 'secure': True, 'path': '/', 'sameSite': 'None', 'domain': '.twitter.com', 'name': 'personalization_id', 'expiry': 1649080453.835446, 'httpOnly': False}]
    for cookie in cookies_list:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)

    # refresh the page to load the cookies
    time.sleep(2)
    driver.refresh()
    # time.sleep(60)

    print("-----------------------------------------------------------------------------------------")
    login_cookies = driver.get_cookies()
    print(login_cookies)

    time.sleep(2)
    return(driver)


if __name__ == '__main__':
    twitter_login()

