from urllib import request, parse
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = '12345'

# 匹配以数字结尾的字符串以继续搜索
search = re.compile("(\d*)$")
# 匹配最终的网页类型字符串以跳出循环
search_html = re.compile("\.html$")

for i in range(400):
    print("%s: " % nothing)

    line = request.urlopen("%s%s" % (url, nothing)).read().decode()
    print(line)

    # 如果找到最终的网页链接则终止查询
    if search_html.findall(line):
        break

    match = search.findall(line)
    if match:
        nothing = match[0]
    else:
        nothing = str(int(nothing) / 2)
