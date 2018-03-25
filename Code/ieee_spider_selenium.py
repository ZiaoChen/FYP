from selenium import webdriver
import time
import os
import csv
import signal
import traceback
path = os.path.dirname(os.path.realpath(__file__))
from selenium.webdriver import ChromeOptions

def get_paper_details(url, driver):

    driver.get(url)
    paper = {}
    paper["Title"] = driver.find_element_by_tag_name("h1").text.encode('utf-8')
    try:
        paper["Abstract"] = driver.find_element_by_xpath("//div[contains(@class,'abstract-text') and contains(@class, 'ng-binding')]").text.encode('utf-8')
    except:
        paper["Abstract"] = None
    try:
        driver.find_element_by_xpath('//*[contains(text(),"Keywords")]').click()
        paper["Keywords"] = driver.find_element_by_xpath("//ul[contains(@class,'u-mt-1')]").text.encode('utf-8')
    except:
        paper["Keywords"] = None
    print paper["Title"]
    return paper
    driver.quit()
options = ChromeOptions()
options.add_argument('--disable-popup-blocking')
options.add_experimental_option("prefs", {'profile.managed_default_content_settings.images': 2})
driver = webdriver.Chrome("chromedriver", chrome_options=options)
# driver = webdriver.PhantomJS()
# paper_driver = webdriver.PhantomJS()
paper_driver = webdriver.Chrome("chromedriver")

# base_url = "http://ieeexplore.ieee.org/search/searchresult.jsp?queryText=machine%20learning"
base_url = "http://ieeexplore.ieee.org/search/searchresult.jsp?queryText=(Computer%20Science)&ranges=2000_2000_Year&sortType=desc_p_Citation_Count"
base_url2 = "&pageNumber=%s&rowsPerPage=%s"
total_page = 25
paper_per_page = 100
headers = ["Title", "Abstract", "Keywords"]
writer = csv.DictWriter(open('IEEE-Computer-Science-2000.csv', 'wb'), fieldnames=headers)
writer.writeheader()
count = 0
for page in range(total_page):
    driver.get(base_url + base_url2 % (str(page + 1), paper_per_page))
    for _ in range(int(paper_per_page / 4)):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
    paper_url_list = driver.find_elements_by_xpath("//div[contains(@class,'List-results-items') and contains(@class, 'ng-scope')]")
    while not paper_url_list:
        time.sleep(1)
        print "Page not loaded, trying again..."
        paper_url_list = driver.find_elements_by_xpath(
            "//div[contains(@class,'List-results-items') and contains(@class, 'ng-scope')]")
    for paper_element in paper_url_list:
        paper_url = paper_element.find_element_by_tag_name("a").get_attribute("href")
        print paper_url
        try:
            writer.writerow(get_paper_details(paper_url, paper_driver))
            count += 1
            print count
        except:
            print traceback.print_exc()
            pass

driver.service.process.send_signal(signal.SIGTERM)
driver.quit()
paper_driver.quit()

