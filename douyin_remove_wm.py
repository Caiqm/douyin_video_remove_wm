# -*- coding: utf-8 -*-
""" author Caiqm. """

import requests
import re
import json

# 抖音分享链接
url = 'https://v.douyin.com/JB52SSP/'
# 设置代理
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3904.108 Safari/537.36'
}
# 获取播放页面
r = requests.get(url, allow_redirects=False, headers=headers)
# 获取播放页面路径
playurl = r.headers['location']
# 获取视频ID
pat = 'video/(.*)/'
video_id = re.compile(pat).findall(playurl)[0]
# 拼接接口域名
api_url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={}".format(video_id)
# 请求接口
rsp = requests.get(api_url, headers=headers)
if rsp.status_code != 200:
    print("请求失败")
    exit()
# 获取接口返回信息并转json
json_str_txt = rsp.text
json_txt = json.loads(json_str_txt)
# 判断接口状态
if json_txt['status_code'] != 0:
    print("接口状态失败")
    exit()
# 获取播放视频路径
video_play_url = json_txt['item_list'][0]['video']['play_addr']['url_list'][0]
# 手机代理
headers = {
    'user-agent': 'Android',
}
# 切换无水印路径
playurl = video_play_url.replace('playwm', 'play')
# # 请求要下载的url地址
html = requests.get(playurl, headers=headers)
# # content返回的是bytes型也就是二进制的数据。
html = html.content
try:
    with open('E:\\python\\test\\douyin.mp4', 'wb') as f:
        f.write(html)
        f.flush()
    print("下载完成！！！！")
except:
    print("下载失败！！！！")