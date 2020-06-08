# -*- coding: utf-8 -*-
import requests  # 啟動網路 url 取得網頁內容
from bs4 import BeautifulSoup  #解析HTML網頁語法
import datetime
import time
from lxml import etree  #建立HTML/XML 樹狀圖 支援Xpath
import sys

strUrl = "https://tw.stock.yahoo.com/q/q?s=2892"

startTime = datetime.datetime(int(sys.argv[1]), int(sys.argv[2]),
                              int(sys.argv[3]), 9, 0, 0)
endTime = datetime.datetime(int(sys.argv[1]), int(sys.argv[2]),
                            int(sys.argv[3]), 19, 30, 0)
nowTime = datetime.datetime.now()

while(nowTime >= startTime and nowTime <= endTime):
  nowTime = datetime.datetime.now()
  print(str(nowTime.month) + "/" + str(nowTime.day) + " -> " + str(nowTime.hour) + ":" +  ("0" + str(nowTime.minute) if (nowTime.minute<10) else str(nowTime.minute)))
  response = requests.get(strUrl)
  tree = etree.HTML(response.text)
  stockName, dealPrice, upDown = "//tr[2]/td[1]/a[1]/text()","//tr[2]/td[3]/b/text()","//tr[2]/td[6]/font/text()"
  print("".join(tree.xpath(stockName)), "".join(tree.xpath(dealPrice)), "".join(tree.xpath(upDown)))
  time.sleep(5)
