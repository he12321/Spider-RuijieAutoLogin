# 提取html的信息

from lxml import etree

tree = etree.parse("a.html", etree.HTMLParser())
# result = tree.xpath("/html/body/ul/li/a/text()")  # ['百度', 'b站', '搜狐']
# result = tree.xpath("/html/body/ul/li[1]/a/text()")  # li[1]拿到第一个 ['百度']
# xpath的顺序从1开始 []表示索引

# 1.a[@属性="值"] 对属性的筛选，@表示属性  2.@属性获取属性值 a@href

# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")  # ['大炮']
# print(result)

ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    # 从每一个li中提取文字信息
    # 从li中继续寻找，相对查找（./表示li）
    result_1 = li.xpath("./a/text()")
    result_2 = li.xpath("./a/@href")  # 获取标签属性值
    result_3 = li.xpath("./a/@href='feiji'")
    print(result_1, result_2, result_3)

print(tree.xpath("/html/body/ol/li/a/@href"))
print(tree.xpath("/html/body/ol/li/a/text()"))