#!/bin/env python3
#-*-encoding:utf-8-*-

'''
爬取我爱我家信息
'''

from bs4 import BeautifulSoup
from r_basedao import BaseDao

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

urls = [
    {
        "url": "http://bj.5i5j.com/rent/n%d",
        "title": "我爱我家",
        "region": "北京",
        "descraption": "业主直租"
    }
]

config = {
    "user": "root",
    "password": "root",
    "database": "rcddup",
    "tableName": "rent_bj"
}
dao = BaseDao(**config)

try:
    driver = webdriver.Firefox(executable_path="D:/geckodriver/geckodriver.exe")
    driver.implicitly_wait(60)
    for i in range(1, 1000):
        url = urls[0]["url"]%(i)
        driver.get(url)
        if driver.find_element_by_xpath('//div[contains(@class, "rent-page")]/a[contains(@class, "current")]').text != str(i):
            break
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info_list = soup.find("div", {"id": "exchangeList"}).find("ul", {"class": "list-body"}).find_all("div", {"class": "list-info"})
        for info in info_list:
            title = info.find("h2").find("a").get_text()
            info_r = info.find("div", {"class": "list-info-r"})
            price = info_r.find("h3").text
            type = info_r.find("p").text
            image_src = info.find_parent().find_next().find("img").get("src")
            info =  {
                "id": None,
                "title": title,
                "image_src": image_src,
                "price": price,
                "type": type,
            }
            # print(info)
            dao.save("rent_bj", info)
except Exception as e:
    print(e)
finally:
    driver.quit()



