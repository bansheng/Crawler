# encoding:UTF-8
import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
# 重点部分是返回值, 这个函数返回一个 http.client.HTTPResponse 对象,
# 这个对象又有各种方法, 比如我们用到的read()方法, 这些方法都可以根据官方文档的链接链过去.
# 根据官方文档所写, 我用控制台运行完毕上面这个程序后, 又继续运行如下代码, 以更熟悉这些乱七八糟的方法是干什么的.
data = data.decode('UTF-8')
print(data)
