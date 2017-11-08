#!/bin/env python3
#-*-encoding:utf-8-*-

import time

from urllib import request
from bs4 import BeautifulSoup

urls = [
    {
        "url": "http://www.360kan.com/ct/PUPmb87mMYWwET.html",
        "description": "秦时明月5：君临天下",
    }, {
        "url": "http://www.360kan.com/ct/PEDsa57jNICzDj.html",
        "description": "秦时明月之天行九歌"
    }, {
        "url": "http://www.360kan.com/ct/QE4maZ7jM4OuDT.html",
        "description": "武庚纪"
    }
]

if __name__ == "__main__":
    for url_dict in urls:
        url = url_dict["url"]
        desc = url_dict["description"]
        resp = request.urlopen(url)
        soup = BeautifulSoup(resp, "html.parser")
        # a_list = soup.find("div", {"class": "s-top-list-ji"}).find("div", {"class": "num-tab-main"}).find_all("a")
        # max = 1
        # for a in a_list:
        #     # print(a)
        #     num = a.get("data-num")
        #     if num:
        #         if int(num) > max:
        #             max = int(num)
        new = soup.find("div", {"class": "s-top-list-ji"}).find("i", {"class": "ico-new"})
        if new:
            max = new.findParent().get("data-num")
            href = new.findParent().get("href")
            print(desc, ">>> 最新集数：%s 【%s】"%(max, href))
        else:
            print(desc, ">>> 无更新")