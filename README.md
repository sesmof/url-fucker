# url-fucker
# url-fucker

一款信息收集工具
先把url源码(包括css/js)下载下来,然后再在源码中识别出url,对识别出来的url进行访问,获得相应码与网页tittle

使用方法:

#安装模块

pip install requests

pip install beautifulsoup4

---------------------------------------------------

python3 url-fucker -u example.com  #启动

python3 url-fucker -u example.com -t #以多线程模式启动#2024.4.21 添加了多线程功能

python3 url-fucker -u example.com -t -s #以多线程模式启动并收集子域名#2024.4.22 添加了搜集子域名功能#目前的最佳语法

作者博客园:https://www.cnblogs.com/sesmof
