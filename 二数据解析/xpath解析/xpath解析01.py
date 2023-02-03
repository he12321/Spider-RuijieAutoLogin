# xpath解析：既高效而且简单，在xml文档中搜索内容的一门语言
# html是xml的一门子集
'''
<book>
    <id>1</id>
    <name>周杰伦</name>
    <nick>hello</nick>
</bbok>
每一个标签是一个节点
book是id，name， nick的父节点
id，name是同胞、兄弟节点
找name(靠节点关系或属性)=> book/name
'''

# 使用xpath需要安装lxml模块
# pip install lxml-i (国内源/清华)https://pypi.tuna.tsinghua.edu.cn/simple

# xpath解析
from lxml import etree  # etree.XML().xpath
xml = """
<ul class="site-footer-ul">
    <li>这是儿子</li>
    <li>
        <div>this is python</div>
    </li>
    <span>
        <div>this is a span</div>
    </span>
    <div>子代div</div>
    <li>
        <a>this is 添加测速节点</a>
    </li>
</ul>
"""
tree = etree.XML(xml)  # 加载为etree的对象
# result = tree.xpath("/ul")  # /表示层级关系，第一个/是跟节点
# [<Element ul at 0x1dbf0b594c0>]    Element:存在节点
# result = tree.xpath("/ul/li/a/text()")  # text() 拿文本
# ['添加测速节点']
# result = tree.xpath("/ul/li/a/text()")  # ['添加测速节点']
# result = tree.xpath("/ul/*/div/text()")  # li/span的div值   * 表示任意的节点，通配符
# ['this is python', 'this is a span']
result = tree.xpath("/ul//div/text()")  # //子孙 所有的div
# ['this is python', 'this is a span', '子代div']
print(result)

