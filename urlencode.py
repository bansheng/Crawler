#__auther__: "丁亚东"
#__date__  : 2018/5/7
import urllib
import urllib.request

data={}
data['word']='dingyadong'

url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values

data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)