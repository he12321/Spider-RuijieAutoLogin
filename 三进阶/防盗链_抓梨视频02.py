# 抓取梨视频视频

'''
源：
https://www.pearvideo.com/video_1046026

fetch/XHR
https://video.pearvideo.com/mp4/short/20170310/1675074941229-10267680-hd.mp4

下载url
https://video.pearvideo.com/mp4/short/20170310/cont-1046026-10267680-hd.mp4
'''

import requests
from lxml import etree

# 1.拿到contid
# 2.拿到videoStatus返回的json -> srcURL
# 3.把srcURL里面的内容进行修正
# 4.下载视频保存到文件

url = 'https://www.pearvideo.com/video_1046026'
contId = url.split("_")[1]  # 把第一个_后面的内容切片

# 获取视频名称
html = etree.HTML(requests.get(url).text)
video_name = html.xpath('//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1/text()')[0]  # 取出元组字符串
print(video_name)
# print('contId =', contId)
videoStatusURL = 'https://www.pearvideo.com/videoStatus.jsp?contId='+contId+'&mrd=0.9876586107811862'
# mrd=0.9876586107811862 就是一个随机数
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70",
    # 防盗链：溯源，既请求的上一级是谁
    "Referer": url
}

'''
请求头里面的Referer就是防盗链，一步一步地执行链接
https://www.pearvideo.com/videoStatus.jsp?contId=1046026&mrd=0.9876586107811862
上面url的上一级必须是下面的防盗链（请求的上一级）
Referer: https://www.pearvideo.com/video_1046026
'''

resp = requests.get(videoStatusURL, headers=header)
# print(resp.text)
dic = resp.json()  # 返回的json到字典里面
# print(dic)

# 目标下载网站：https://video.pearvideo.com/mp4/short/20170310/cont-1046026-10267680-hd.mp4

srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f'cont-'+contId)
resp.close()

# 保存到文件

import os

resp = requests.get(srcUrl)
content = resp.content  # 拿到字节文件
os.listdir('梨视频')  # 创建文件夹
with open('梨视频/'+video_name+'.mp4', mode="wb") as f:
    f.write(content)

print(video_name+".mp4视频下载成功！")
f.close()
resp.close()
