import time
from selenium.webdriver.chrome.webdriver import WebDriver


def user_location_collector(driver: WebDriver, user_url: str):
    driver.get(user_url)
    time.sleep(4.5)
    # 用户所在位置对应页面元素的css class存在两种，所以需要对两种都进行尝试获取
    location_class_1 = 'css-901oao css-16my406 r-111h2gw r-4qtqp9 r-1qd0xha r-ad9z0x r-19einr3 r-bcqeeo r-qvutc0'
    location_css_selector_1 = '.' + location_class_1.replace(' ', '.')
    location_class_2 = 'css-901oao css-16my406 r-111h2gw r-4qtqp9 r-1qd0xha r-ad9z0x r-zso239 r-bcqeeo r-qvutc0'
    location_css_selector_2 = '.' + location_class_2.replace(' ', '.')
    try:
        location_span = driver.find_elements_by_css_selector(location_css_selector_1)
        # 当用户的地理位置为设置时，采集到的数据就会是用户加入twitter的时间，需要排除
        try:
            if '加入' in location_span[0].text:
                location = 'unknown'
            else:
                location = location_span[0].text
        except:
            location = 'unknown'
    except:
        location = 'unknown'

    if location == 'unknown':
        try:
            location_span = driver.find_elements_by_css_selector(location_css_selector_2)
            try:
                if '加入' in location_span[0].text:
                    location = 'unknown'
                else:
                    location = location_span[0].text
            except:
                location = 'unknown'
        except:
            location = 'unknown'

    return location
