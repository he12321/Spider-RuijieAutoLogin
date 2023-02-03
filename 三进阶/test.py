import base64
import json
from base64 import b64encode
from Crypto.Cipher import AES

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

g = '0CoJUm6Qyw8W8jud'


def get_params(data):  # data: win是utf-8的字符串
    i = "34EPsTSawK4yYPPr"  # 随机16位值

    g = '0CoJUm6Qyw8W8jud'
    first_enc = aes_encrypt(data, g)
    second_enc = aes_encrypt(first_enc, i)
    return second_enc


def tobe_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):  # 加密算法
    iv = "0102030405060708"  # 偏移量

    # 加密,编码成字节 key(bytes、iv(bytes/ mode:cbc
    aes = AES.new(key=key.encode("utf-8"), mode=AES.MODE_CBC, iv=iv.encode("utf-8"))  # 创造加密工具

    # 加密的长度必须是16的倍数
    u_data = tobe_16(data)
    byte_s = aes.encrypt(u_data.encode("utf-8").strip())  # 要加密的数据也必须是字节

    # 将字节字符串编码成16进制字符串
    return str(b64encode(byte_s), "utf-8")


def aes_encrypt(msg, key):
    # 如果不是16的倍数则进行填充
    padding = 16 - len(msg) % 16
    # 这里使用padding对应的单字符进行填充
    msg += padding * chr(padding)
    # 用来加密或者解密的初始向量(必须是16位)
    iv = '0102030405060708'
    # AES加密
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 加密后得到的是bytes类型的数据
    encrypt_bytes = cipher.encrypt(msg)
    # 使用Base64进行编码,返回byte字符串
    encode_string = base64.b64encode(encrypt_bytes)
    # 对byte字符串按utf-8进行解码
    encrypt_text = encode_string.decode('utf-8')
    # 返回结果
    return encrypt_text


print("params:", get_params(json.dumps(data)))
'''
"hXIHzJTHloMCaCpK"
"i7wvj8/cCucRRvz8Gr5sRjiL4g0aycupNZK2c+mgWVglvqZ3lx6r52FTKWxewciUXklsbxZybh8pTahxfODa8A76CszjaygV3EdFo9gvWnWyzAW" \
"OBzPV+qJxDu20AHJ2KqbaOHU/Ix/u2BGHwhy6WcfcEnA1Fq5ErpEOcD857ocN2FdDh8wiKuNm/LxUn/fkyRVpfwgI+tYK6/Z1saIhyQ=="

params: PCsq7ade0wP5zt5acBgETajqKi5CX+nXy17uEs0mxL+avQxvK6UmPNdClsK10FCFM4XHX30hCysNnjraCcffwwIfnDLrifIBcB8TdtO
d3qN/C5K4tlxZv9trT95XcybAuIZd91Tg3CPMRShAv38hfczNeUoi4ern0BOa6dw8G4jdhQQe6u3I1DLzdSJoetzz0Ui4IWN6U5Z5/9dKvfK
a3ylkEpkuIBLJW8XLeq5sHVmndH/qqbPJzjGaxalxLyN5XCCIX2z7H+cjxAxoEKbw7n
+cpASQJdwseNNoZJ9bWAWsboVhIsdcfylaugbtM5ec
enc_encSecKey: 0f7ef420c46448b70d70824bcb9eedc06e3a6d615442e7c80d886
575c1cb64f627da23a3693d63a0cf4bab0158f9217583f1232c7380c2fdd8d9c0d70
406bd55f547449e1b68e36198612e4710552ab7d068d44078ae7d9eb9a465fbb226d2fcc9a8b72fb
76f21debf671dc149796f3deb2091e71f49efdda9b76d8ddb35efa2

'''

