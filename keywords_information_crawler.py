from selenium.webdriver.chrome.webdriver import WebDriver
import time
import pandas as pd


def keywords_information_collector(driver: WebDriver, keyword: str='hotel', start_date='2020-01-05',
                                   end_date='2020-04-06', iter_num: int=10, rolling_factor: int=1):

    # 设置查询关键字和查询日期对应的twitter查询页面
    # url中的&f=live表示最近的推文
    # 当keyword=(%40westin)时, 表示搜索提到@westin的结果
    # 当keyword="at%20westin"时, 表示搜索包括固定短语at westin的结果
    url = 'https://twitter.com/search?q=' + keyword + '%20until%3A' + end_date + '%20since%3A' + start_date + \
          '&src=typed_query&f=live'
    driver.get(url)
    time.sleep(15)

    # 创建用于存储数据的DataFrame
    info_df = pd.DataFrame(columns=('user_name', 'twitter_time', 'text'))

    # 多次滚动页面来刷新获得新内容
    for i in range(iter_num):
        # 获取每个用户发文的Twitter消息内容块(div)
        twitters_div = driver.find_elements_by_css_selector(".css-1dbjc4n.r-18u37iz.r-thb0q2")

        for twitter_div in twitters_div:
            # 可能存在不符合条件的div块
            try:
                text_twitter_div = twitter_div.find_elements_by_css_selector(
                    '.css-901oao.r-jwli3a.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0')
            except:
                continue
            # 属于该class的部分div块(1/2)为空div
            if twitter_div.text != '' and text_twitter_div != []:
                # 获取Twitter内容文本
                try:
                    text_twitter = text_twitter_div[0].text
                except:
                    continue

                # 获取发文时间
                time_twitter_class_label = "css-4rbku5 css-18t94o4 css-901oao r-111h2gw r-1loqt21 r-1q142lx r-1qd0xha" \
                                           " r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0"
                time_twitter_css_selector = "." + time_twitter_class_label.replace(' ', '.')
                try:
                    time_twitter = twitter_div.find_elements_by_css_selector(time_twitter_css_selector)[0]\
                        .get_attribute("title")
                except:
                    continue

                # 获取发文用户昵称
                user_twitter_class_label = "css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l"
                user_twitter_css_selector = "." + user_twitter_class_label.replace(' ', '.')
                try:
                    user_name = twitter_div.find_elements_by_css_selector(user_twitter_css_selector)[0]\
                        .get_attribute('href')
                except:
                    continue

                # 将数据插入DataFrame(info_df)中
                print("------------------------------------------------")
                print([time_twitter, user_name, text_twitter])
                single_twitter = pd.DataFrame({'user_name': [user_name], 'twitter_time': [time_twitter],
                                               'text': [text_twitter]})
                info_df = info_df.append(single_twitter, ignore_index=True)

        # 向下滚动页面
        js = "window.scrollTo(0, %d * document.body.scrollHeight)" % rolling_factor
        driver.execute_script(js)
        time.sleep(5)

    info_df.drop_duplicates(subset=['text'], inplace=True)
    # info_df.to_csv('twitter_hotel.csv')
    return info_df









