# KuGou
A small downloader for KuGou 本程序只应用于学习交流，不要应用于商业目的、侵犯其他公司利益

Version : 0.1  默认下载
Version : 0.2  选择下载

## Step 1：获取搜索结果的url
  
  1.在博客（[博客原文](http://www.cnblogs.com/tangwanzun/p/6582039.html)）中了解了酷狗搜索结果的url结构
    
    由'http://songsearch.kugou.com/song_search_v2?callback=' + callback + 'keyword=' + keyword + '&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=' + timeStap  构成
    
    
    其中 callback 为回调函数（我也不知道是干什么的[呲牙]），keyword 为搜索关键词的url格式，  timeStap为时间戳
    
  2.用浏览器的开发工具审查搜索结果的Network中的All，在搜索框中输入歌曲名字后会出现song_search的一个链接，在右侧Preview中有解析好的json
    
    其中[data][lists]便是歌曲列表。（以后有时间可以实现选择下载和批量下载）
    本程序实现下载默认歌曲，便采用了[data][lists][0]中歌曲的信息，其中FileHash是歌曲的Hash信息，程序中的getFileHash()函数的功能便是返回filehash
   
## Step 2：获取歌曲文件的url

  1.每一首歌曲都有特有的url
  
    'http://www.kugou.com/yy/index.php?r=play/getdata&hash=' + filehash
    解析此网页后发现，在data里面有歌曲的各种信息，包括timelenth、filesize、audio_name、lyrics...  其中最重要的，也是我一直寻找的就是播放地址：play_url
    
## Step 3：下载歌曲

    1.怎么把MP3格式的网页保存呢？
      强大的Python库为我们提供了方法：urllib.request.urlretrieve(url,path) 把音乐或者图片格式的网页保存在path路径里面
      

## 感谢
1.感谢表哥写的一个程序（[程序地址](https://github.com/fooyou/cmus-lrc)）很多思路从中得出  
   
2.感谢博客（[博客原文](http://www.cnblogs.com/tangwanzun/p/6582039.html)）  
    
## Change The World By Program
