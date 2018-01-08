import csv
import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


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
    time.sleep(2)
    element1 = driver.find_elements_by_css_selector(
        'span[class*="taLnk ulBlueLinks"]')
    if len(element1) != 0:
        element1[0].click()
        time.sleep(2)
    html = (driver.page_source).encode('utf-8')
    extract_reviews(html, driver)


def extract_reviews(html, driver):
    soup = BeautifulSoup(html, 'lxml')
    for review in soup.find_all("div", {"class": "prw_rup prw_reviews_basic_review_hsx"}):
        review_text = review.find("p", {"class": "partial_entry"}).text
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow([review_text])

    navigation = soup.find("div", {"class": "unified pagination north_star "})
    if navigation.find("span", {"class": "nav next disabled"}) == None:
        next_button = driver.find_element_by_xpath(
            "//div[@class='ui_button primary ' and text()='Next']")
        next_button.click()
        time.sleep(2)
        element1 = driver.find_elements_by_css_selector(
            'span[class*="taLnk ulBlueLinks"]')
        if len(element1) != 0:
            element1[0].click()
            time.sleep(2)
        html = (driver.page_source).encode('utf-8')
        extract_reviews(html, driver)
    else:
        print("last page")
        driver.quit()
        csvfile.close()


sys.setrecursionlimit(1500)
csvfile = open('zooreviews2.csv', 'w+', encoding='utf-8', newline='')
website = 'https://www.tripadvisor.com.sg/Attraction_Review-g294265-d324542-Reviews-Singapore_Zoo-Singapore.html'
scrape_with_headers(website)
            for item in self.negatives:
                if token in item:
                    score = score - 1
        #print(score)
        # TODO
        return score

    def vader_analyze(self, text):
        vader = SentimentIntensityAnalyzer()
        score = vader.polarity_scores(text)
        return score['compound']

    def frequency(self, text):
        fdist1 = FreqDist(text)
        print(fdist1)
        top_50 = fdist1.most_common(50)
        return top_50

    def animal_frequency(self, input_list, raw_text):
        animals = input_list
        animals = [word.lower() for word in animals]
        #http://www.nltk.org/howto/stem.html
        stemmer = nltk.PorterStemmer()
        raw_text = raw_text
        singles = [stemmer.stem(word) for word in raw_text]
        animal_text = []
        for word in singles:
            if word in animals:
                animal_text.append(word)
            else:
                continue
        fdist1 = FreqDist(animal_text)
        top_50 = fdist1.most_common(50)
        return top_50

        # TODO
        return score
    
    def vader_analyze(self, text):
        vader = SentimentIntensityAnalyzer()
        score = vader.polarity_scores(text)
        return score['compound']

    def frequency(self, text):
        fdist1 = FreqDist(text)
        print(fdist1)
        top_50 = fdist1.most_common(50)
        return top_50
    
    def animal_frequency(self, input_list, raw_text):
        animals = input_list
        animals = [word.lower() for word in animals]
        #http://www.nltk.org/howto/stem.html
        stemmer = nltk.PorterStemmer()
        raw_text = raw_text
        singles = [stemmer.stem(word) for word in raw_text]
        animal_text = []
        for word in singles:
            if word in animals:
                animal_text.append(word)
            else:
                continue
        fdist1 = FreqDist(animal_text)
        top_50 = fdist1.most_common(50)
        return top_50

