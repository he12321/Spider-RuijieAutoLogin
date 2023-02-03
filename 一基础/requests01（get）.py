'''
爬虫：模拟浏览器来访问互联网上的资源
requests模块安装：pip install requests（需要环境变量配置好）
# 如果pip现在选择国内源  百度pip清华源
临时使用：pip install -i 清华源 requests
pip list：查看Python已安装好的模块
'''

# https://www.sogou.com/sogou?query=周杰伦（搜索地址栏里面的请求get）
import requests
who = input("请输入一个喜欢的明星：")
url = f'https://www.sogou.com/sogou?query={who}'  # f'{}'把括号变量加到字符里面
# resp = requests.get(url)  # 没有处理会调用一个自动化程序的User-agent处理
# print(resp)
# print(resp.text)  # 获取html的源码代码
# <p class="p2">用户您好，我们的系统检测到您网络中存在异常访问请求。
# <br>此验证码用于确认这些请求是您的正常行为而不是自动程序发出的，需要您协助验证。</p>
# 在请求头里面有user-ageent描述当前请求是哪个设备发出
dic = {
    # 里面是一个字典
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
resp = requests.get(url, dic)
print(resp.text)
resp.close()


