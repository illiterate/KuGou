#!/usr/bin/env python3
# Author: Victor He
# Email: victor-he@qq.com

import urllib.request
import urllib.parse
import json
import time

def getFileHash(keyword_cn):
    callback = 'jQuery112403505339159124259_1507896482672&'
    keyword = urllib.parse.quote(keyword_cn)
    timeStap = str(int(time.time()*1000))
    url = 'http://songsearch.kugou.com/song_search_v2?callback=' + callback + 'keyword=' + keyword + '&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=' + timeStap

    res = urllib.request.urlopen(url)
    html = res.read().decode()
    html = html[len(callback) : len(html)-2]
    html = json.loads(html)
    filehash = str(html['data']['lists'][0]['FileHash'])
    return filehash

def downloadFile(filehash):
    hashurl = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash=' + filehash
    res = urllib.request.urlopen(hashurl)
    html = res.read().decode()
    html = json.loads(html)
    songurl = html['data']['play_url']
    path = keyword_cn + '.mp3'
    urllib.request.urlretrieve(songurl,path)
    print(keyword_cn + '.mp3 下载成功')

if __name__ == '__main__':
    keyword_cn = input('请输入歌曲名字：')
    downloadFile(getFileHash(keyword_cn))
