# auther: "丁亚东"
# date  : 2018/5/7

import urllib.request
import re

data = {}
data['word'] = 'ppp'

url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
# print(data)

line = "Cats are smarter than dogs"
# ？是非贪婪模式
matchObj = re.match(r'(C.*) are (.*?) (.*)', line, re.M | re.I)
print(matchObj.groups())
print(type(matchObj.span()))
