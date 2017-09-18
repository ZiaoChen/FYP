from selenium import webdriver
import time
import os
import csv
import signal
path = os.path.dirname(os.path.realpath(__file__))


def get_paper_details(url):
    driver = webdriver.Chrome("chromedriver")
    driver.get(url)
    paper = {}
    paper["Title"] = driver.find_element_by_tag_name("h1").text
    paper["Abstract"] = driver.find_element_by_xpath("//div[contains(@class,'abstract-text') and contains(@class, 'ng-binding')]").text.encode('utf-8')
    driver.find_element_by_xpath('//*[contains(text(),"Keywords")]').click()
    paper["Keywords"] = driver.find_element_by_xpath("//ul[contains(@class,'u-mt-1')]").text
    print paper["Title"]
    return paper
    driver.quit()

driver = webdriver.PhantomJS()
base_url = "http://ieeexplore.ieee.org/search/searchresult.jsp?queryText=machine%20"
base_url2 = "learning&pageNumber=%s&rowsPerPage=%s"
total_page = 10
paper_per_page = 100
headers = ["Title","Abstract","Keywords"]
writer = csv.DictWriter(open('Data/IEEE-machine-learning.csv', 'wb'), fieldnames=headers)
writer.writeheader()

for page in range(total_page):
    driver.get(base_url + base_url2 % (str(page + 1), paper_per_page))
    for _ in range(int(paper_per_page / 10)):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.1)
    paper_url_list = driver.find_elements_by_xpath("//div[contains(@class,'List-results-items') and contains(@class, 'ng-scope')]")
    for paper_element in paper_url_list:
        paper_url = paper_element.find_element_by_tag_name("a").get_attribute("href")
        print paper_url
        writer.writerow(get_paper_details(paper_url))

driver.service.process.send_signal(signal.SIGTERM)
driver.quit()

