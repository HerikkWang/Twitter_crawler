from Twitter_login import twitter_login
from keywords_information_crawler import keywords_information_collector
from selenium import webdriver
from user_location_crawler import user_location_collector


if __name__ == '__main__':
    driver = webdriver.Chrome()

    # driver = twitter_login(driver)

    data = keywords_information_collector(driver=driver, keyword='(in%20Westin)', iter_num=100, rolling_factor=1)

    for i in range(len(data)):
        user_url = data.iloc[i]['user_name']
        user_location = user_location_collector(user_url=user_url, webdriver=driver)
        data.loc[i, 'location'] = user_location

    data.to_csv('twitter_in_westin_.csv', encoding='utf-8')
    print(data)
    driver.quit()
