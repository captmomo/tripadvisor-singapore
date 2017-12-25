import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import DesiredCapabilities
import re

def set_headers():
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
                                                                  'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                                                  'Chrome/39.0.2171.95 Safari/537.36'
    driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities)
    return driver

def scrape_with_headers(url):
    driver = set_headers()
    driver.get(url)
    time.sleep(5)
    element1 = driver.find_element_by_css_selector('span[class*="taLnk ulBlueLinks"]')
    element1.click()
    time.sleep(5)
    html = (driver.page_source).encode('utf-8')
    extract_reviews(html, driver)

def extract_reviews(html, driver):
    soup = BeautifulSoup(html, 'lxml')
    for review in soup.find_all("div", {"class": "prw_rup prw_reviews_basic_review_hsx"}):
        review_text = review.find("p",{"class": "partial_entry"}).text
        print(review_text)
        playFile.write(review_text+'\n')
    navigation = soup.find("div", {"class" : "unified pagination north_star "})
    if navigation.find("span", {"class" : "nav next disabled"}) == None:
        next_button = driver.find_element_by_xpath("//div[@class='ui_button primary ' and text()='Next']")
        next_button.click()
        time.sleep(5)
        element1 = driver.find_element_by_css_selector('span[class*="taLnk ulBlueLinks"]')
        element1.click()
        time.sleep(5)
        html = (driver.page_source).encode('utf-8')
        extract_reviews(html, driver)
    else:
        print("last page")
        driver.quit()
        playFile.close()

playFile = open('zooreviews.txt', 'w', encoding='utf-8')
url = 'https://www.tripadvisor.com.sg/Attraction_Review-g294265-d324542-Reviews-or9640-Singapore_Zoo-Singapore.html'
scrape_with_headers(url)

#<span class="taLnk ulBlueLinks" onclick="widgetEvCall('handlers.clickExpand',event,this);">More</span>