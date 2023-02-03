# 抓取网易云评论(寂寞烟火 烟嗓)

# 1.找到未加密的的参数
# 2.想办法进行类似的加密（必须参考网易的逻辑，params、encSecKey）
# 3.请求到网易，获取评论信息

# 安装pycryptodeme，进行ACE加密
# pip install pycryptodome
import codecs
from math import floor
from random import random

from Crypto.Cipher import AES
import requests
from base64 import b64encode
import json


# 产生随机字符
def generate_random_str(lenth):
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    new_string = ""
    for i in range(lenth):
        new_string += string[floor(random() * len(string))]  # floor取整

    return new_string


def get_encSeckey():  # i:随机16位值 e:010001 f:长字符串
    result = enc_enSecKey(i, e, f)
    return result


# 实现RSA加密：function c(a, b, c) {a：随机16字符串，b：010001，c：长字符串
def enc_enSecKey(random_string, key, f):
    # def rsa_encrypt(random_string, key, f):
    # 随机字符串逆序排列
    string = random_string[::-1]
    # 将随机字符串转换成byte类型数据
    text = bytes(string, 'utf-8')
    # RSA加密
    sec_key = int(codecs.encode(text, encoding='hex'), 16) ** int(key, 16) % int(f, 16)
    # 返回结果
    return format(sec_key, 'x').zfill(256)


def get_params(data):  # data: win是utf-8的字符串
    g = '0CoJUm6Qyw8W8jud'  # 秘钥

    first_enc = enc_params(data, g)
    second_enc = enc_params(first_enc, i)
    return second_enc


def tobe_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


# 实现AES加密 function b(a, b) a=data, b=随机产生的16字符串
def enc_params(data, key):  # 加密算法

    iv = "0102030405060708"  # 偏移量为定值

    # 加密,编码成字节 key(bytes、iv(bytes/ mode:cbc
    aes = AES.new(key=key.encode("utf-8"), iv=iv.encode("utf-8"), mode=AES.MODE_CBC)  # 创造加密工具

    # 加密的长度必须是16的倍数，并且转化成字节
    data_16 = tobe_16(data).encode("utf-8")
    byte_s = aes.encrypt(data_16)  # 要加密的数据也必须是byte, .encode("utf-8")

    # 将字节字符串编码成16进制字符串
    return str(b64encode(byte_s), "utf-8")


# 处理加密过程
'''
 var bMr1x = window.asrsea(JSON.stringify(i3x), bsg7Z(["流泪", "强"]), bsg7Z(TH8z.md), bsg7Z(["爱心", "女孩", "惊恐", "大笑"]));
            e3x.data = j3x.cr4v({
                params: bMr1x.encText,
                encSecKey: bMr1x.encSecKey
JSON.stringify(i3x)= data = {"rid":"R_SO_4_512358200","threadId":"R_SO_4_512358200","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}       
bsg7Z(["流泪", "强"] = '010001'     
bsg7Z(TH8z.md) = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
bsg7Z(["爱心", "女孩", "惊恐", "大笑"]) = '0CoJUm6Qyw8W8jud'

window.asrsea = d,所以调用window.asrsea() = d()函数
window.ecnonasr = e

function a(a=16) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,  # b长度里面产生随机数 
            e = Math.floor(e),  # 取整数
            c += b.charAt(e);  # 选取字符
        return c
    }                           # 通过循环产生一个16位的随机字符串
    function b(a, b) {  # a=data, b=随机产生的16字符串
        var c = CryptoJS.enc.Utf8.parse(b)  # b是秘钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {  # c：加密的秘钥
            iv: d,  # 偏移量
            mode: CryptoJS.mode.CBC  # 模式：cbc加密
        });
        return f.toString()
    }
    function c(a, b, c) {a：随机16字符串，b：010001，c：长字符串
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),  # b,c字符串传进来
        e = encryptedString(d, a)   # 结果与a（随机）
    }
    function d(d, e, f, g) { d:data  e:'010001'  f:'也是固定的长字符串'  g:'0CoJUm6Qyw8W8jud'
        var h = {}
          , i = a(16);  # i：16随机字符串，把i设置为定值
        return h.encText = b(d, g),   # data, g
        h.encText = b(h.encText, i),  # 返回的是params
        h.encSecKey = c(i, e, f), # 返回的是encSeckey，i固定之后得到的key也固定，e、f是定值
        h    
        encSockey："df82cdb0005842860ae10b2d4e403b732b6696ea95d0f5c0fd0adcb5dc427998e06
        076bcae89c56fc7b8a9948b644194a0d62a2fa66bd2bb555017329c6378a38656865a7b40e94cea67
        31fb47e17acc2419cac7d6a805e1912e9aba6b66a48c6c83e273bdc76ea75c1a4c2fb39456cedef0d83e16803e5ad92a2079778f6fb7"
    }
    
    params两次加密：
    数据data+g -> b =>第一次加密+i -> 第二次加密 => b = params
    
'''

# 请求方式是post
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5a' \
      'a76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46' \
      'bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'  # 第四个参数，秘钥

i = generate_random_str(16)  # 随机产生的16字符串

# https://music.163.com/#/song?id=2013805632
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_2013805632",
    "threadId": "R_SO_4_2013805632"
}

# 请求方式是post
resp = requests.post(url, data={
    # 把字典转换成字符串，导入json：import json
    # 这下面大坑，必须转换成utf-8的字符串
    "params": get_params(json.dumps(data)),  # data是字典，转换成字符串
    "encSecKey": get_encSeckey()
})

print(resp.json())
