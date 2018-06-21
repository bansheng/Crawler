# !/usr/bin/python
#  -*- coding: UTF-8 -*-
# auther: 丁亚东
# date  : 2018/5/7 23:58
import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()

url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()  # 队首元素出队
    visited |= {url}  # 标记为已访问，并集

    print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
    cnt += 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib.request.Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    urlop = urllib.request.urlopen(req)
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    # 避免程序异常中止, 用try..catch处理异常
    try:
        data = urlop.read().decode('utf-8')
    except:
        continue

    # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile(r'class="title".+?href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->  ' + x)