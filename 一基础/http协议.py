print("http协议")
'''
# http协议
请求：
    1.请求行->请求url、请求方式get/post、协议
    2.请求头->放一些服务器使用的附加信息
    3.请求体->一般放一些请求参数
响应：
    1.状态行->协议、状态码
    2.响应头->放一些客户端使用的附加信息
    3.响应体->服务端返回的真正客户端要使用的内容（html,json）

请求头中一些重要的内容
1.User-agent:请求载体的设备标识（使用什么设备发送的请求）
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.6
2.Referer:防盗链（这个请求是从哪个页面发送过来，反爬会用到）
3.cookies：本地字符串数据信息（用户登录信息，反爬的taken）
响应头中
1.cookies：本地字符串数据信息（用户登录信息，反爬的taken）
2.各种莫名其妙的字符串（一般都是taken字样）
请求方式
1.GET:显示提交，查询东西的时候
2.POST：隐式提交，提交上传修改服务器的数据的时候

---------------------------------------------------------------------------------------------
请求 URL: https://cm.bilibili.com/cm/api/receive/content/pc
请求方法: POST                  # 请求方法get/post
状态代码: 200                   # 状态码 404网页打不开  200 ok网页响应正常
远程地址: 223.111.250.57:443
引用者策略: no-referrer-when-downgrade

# 响应头：respons-headers
access-control-allow-credentials: true
access-control-allow-headers: Origin,No-Cache,X-Requested-With,If-Modified-Since,Pragma,Last-Modified,Cache-Control,Expires,Content-Type,Access-Control-Allow-Credentials,DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Cache-Webcdn,x-bilibili-key-real-ip,x-backend-bili-real-ip,x-risk-header
access-control-allow-origin: https://www.bilibili.comcache-control: no-cache
content-encoding: gzipcontent-type: application/json;charset=UTF-8
cross-origin-resource-policy: cross-origindate: Sun, 22 Jan 2023 11:41:16 GMT
expires: Sun, 22 Jan 2023 11:41:15 GMTserver: Apache-Coyote/1.1
x-application-context: cpm-receive:8088x-cache-webcdn: BYPASS from blzone05

# 请求头：requests-headers
:authority: cm.bilibili.com
:method: POST
:path: /cm/api/receive/content/pc
:scheme: https
accept: application/json
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
content-length: 299
content-type: application/json
cookie: buvid3=99ED0C2E-4271-B40C-C936-E255FF630F0E16729infoc; b_nut=1674119016; i-wanna-go-back=-1; _uuid=F37778B5-FEA5-5E110-8B8E-AF9C25E76FF417833infoc; nostalgia_conf=-1; buvid_fp_plain=undefined; rpdid=|(um~R|~RYul0J'uY~RuumRmk; DedeUserID=1845709939; DedeUserID__ckMd5=48e46ba8c3222779; b_ut=5; i-wanna-go-feeds=-1; LIVE_BUVID=AUTO5316741332137340; CURRENT_QUALITY=80; buvid4=2EA8E1BE-E09B-9CC6-ED56-622CF09DEFC218005-023011917-%2BsOKQ0jzzm7nFUDeXXkVDA%3D%3D; fingerprint=0c01b851020e4b7c21c5a5ed12251ea2; buvid_fp=677cf0c0dc25a41f268335dd53dad530; is-2022-channel=1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; bp_video_offset_1845709939=753858466796273700; SESSDATA=66f682ae%2C1689939033%2C83ea6%2A11; bili_jct=2f93ba85d71b951293d10fc0f0b7edb1; sid=fitm84ny; _dfcaptcha=491bd03100c2416210437767805b21d1; innersign=0; b_lsid=AB958771_185D942DACF; PVID=5
origin: https://www.bilibili.com
referer: https://www.bilibili.com/
sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-site
# 请求设备的信息参数
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61

'''