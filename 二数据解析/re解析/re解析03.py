# re模块的使用

import re
# findall：匹配字符串所有符合正则的内容
# def findall(pattern, string, flags=0):
# lst = re.findall(r"\d+", "我的电话号码是10086或者110，我是爱敲代码的小贺！")
# print(lst)
#
# # finditer：匹配符合正则的字符串，返回的是迭代器
# it = re.finditer(r"\d+", "我的电话号码是10086或者110，我是爱敲代码的小贺！")
# for i in it:
#     print(i.group())

# search返回的结果是match对象,找到一个对象就返回
# def search(pattern, string, flags=0):
# Scan through string looking for a match to the pattern, returning a Match object, or None if no match was found.
# return _compile(pattern, flags).search(string)
# s = re.search(r"\d+", "我的电话号码是10086或者110，我是爱敲代码的小贺！")
# print(s.group())
# print(s.group())

# 预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("我的电话号码是10010，我的名字叫小贺,中国移动的电话号码是10086")
# for i in ret:
#     print(i.group())
#
# ret = obj.findall("有什么问题请拨打110电话！")
# for i in ret:
#     print(i)

# 从正则里面提取内容
s = """
    <div class="jay" id="1">第一名</div>
    <div class="jllj" id="2">这是一个测试的div块</div>
    <div class="lisi" id="3">计算机与大数据</div>
    <div class="zhangsan" id="4">物联网工程</div>
"""
# 准备正则 def compile(pattern, flags=0)
# (?P<分组名字>正则) 从正则匹配的内容中提取到分组名字的内容

obj = re.compile(r'<div class=".*?" id="(?P<id>.*?)">(?P<get>.*?)</div>', re.S)
# re.S: 让.匹配换行符
# 单引号和双引号不能同事存在，会冲突，前面使用单引号，里面使用双引号

result = obj.finditer(s)
for it in result:
    print("id:"+it.group("id"), it.group("get"))

