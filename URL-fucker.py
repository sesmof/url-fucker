'''
萌新的处女作
a inferior and terrible program for mining URLs, wrote by sesmof and a terrible AI.
Thank you for using ;)
'''
import time
time1=time.time()
import argparse
from core import downurl
from core.color import *
from datetime import datetime
import re
from urllib.parse import urlparse
import os
from concurrent.futures import ThreadPoolExecutor
path='downloads'
astar='[*]'
logo=TOmiku(r'''
 _     ____  _           _____ _     ____  _  __ _____ ____ 
/ \ /\/  __\/ \         /    // \ /\/   _\/ |/ //  __//  __\
| | |||  \/|| |   _____ |  __\| | |||  /  |   / |  \  |  \/|
| \_/||    /| |_/\\____\| |   | \_/||  \_ |   \ |  /_ |    /
\____/\_/\_\\____/      \_/   \____/\____/\_|\_\\____\\_/\_\
''')+TOgreen('*** v1.11 *********************************')+TObulue('''*** ---by sesmof ***''')
#Command line parsing解析命令行 
parser=argparse.ArgumentParser(description=TOmiku('URL-fucker v0.1'))
parser.add_argument('-u', type=str, default=None, help='input the url')
parser.add_argument('-t', action='store_true', help='if you want to use multithreading')
parser.add_argument('-s', action='store_true', help='find subdomain')
args=parser.parse_args()
#---
#加脑袋
def add_http_header(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    return url
#当前时间
def now():
    return astar+'|@'+datetime.now().strftime("%H:%M:%S")+'|'
#遍历文件夹下的所有文件
def traverse_file(path):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            yield 'downloads/'+file

        elif os.path.isdir(file_path):
            traverse_file(file_path)
#识别出文件中的url
from core import findurl
#获取网页摘要
from core import getxxx
#扫子域名
from core.findsudomain import find_subdomain
def find_subdomain2(path):
    subdomains=[]
    for file in traverse_file(path):
        
        urls_in_file, paths_in_file=findurl.find_urls_and_paths_in_file(file)
        #print(urls_in_file)
        # print('===========================')
        # print(find_subdomain(urls_in_file,args.u))
        subdomains.append(find_subdomain(urls_in_file,args.u))
    return subdomains
#find_subdomain2(path)#test

import threading
#多线程函数
def worker(file, url, lock):
    try:
        status_code, title = getxxx.getxxx(url)
    except:
        status_code = 'Unknown'
        title = 'Unknown'
        with lock:
            print('|--', TOred(now()+'An error occurred while parsing the URL: ')+url, TOred(status_code), title)
    else:
        with lock:
            if status_code == 200:
                print('|--', TOgreen(now())+url, TOgreen(str(status_code)), title)
            else:
                print('|--', TOyellow(now())+url, TOyellow(str(status_code)), title)
#下载页面,还有一些初始化功能:
def downpage():
    if args.u==None:
        print(logo)
        print('\n'+TOmiku('[*]')+'-h for help\n'+TOmiku('[*]')+'-u input url\n'+TOmiku('[*]')+'-t use multithreading\n'
              +TOmiku('[*]')+'-s to find subdomains\n')
        exit()
    else:
        print(logo)
        url=add_http_header(str(args.u))

        downurl.download_webpage(url,path)
        print(TOgreen(now()+'success:')+' main-page is downloaded')
downpage()

#普通启动
def normal_main(path):
    for file in traverse_file(path):
        print ('\n'+TOmiku(file))
        urls_in_file, paths_in_file=findurl.find_urls_and_paths_in_file(file)
        for url in urls_in_file:
            #print(TOmiku(url))
            try:
                
                statuse_code,tittle=getxxx.getxxx(url)

                if statuse_code ==200:
                    print('|--',TOgreen(now())+url,TOgreen(str(statuse_code)),tittle)
                else:
                    print('|--',TOyellow(now())+url,TOyellow(str(statuse_code)),tittle)
            except:
                print('|--',TOred(now()+'An error occurred while parsing the URL: ')+url,TOred(str('5xx')),tittle)
#多线程启动
def thread_main(path):
    lock = threading.Lock()
    for file in traverse_file(path):
        print('\n' + TOmiku(file))
        urls_in_file, paths_in_file = findurl.find_urls_and_paths_in_file(file)
        threads = []
        for url in urls_in_file:
            t = threading.Thread(target=worker, args=(file, url, lock))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
ifsubdomain=0
if args.s ==True:
    ifsubdomain=1
    # subdomain_worker=threading.Thread(target=find_subdomain2,args=(path,))
    # subdomain_worker.start()
    #find_subdomain2(path)
    future = ThreadPoolExecutor().submit(find_subdomain2, path)
    
if args.t ==False:
    normal_main(path)
elif args.t==True:
    thread_main(path)
if ifsubdomain==1:
    whattime=time.time()-time1
    print('\n'+TOmiku('[*]urls finding is DOWN,It took: ')+TOgreen(f'{whattime}')+TOmiku('s'))
    print(TOmiku("[*]subdomain's finding is WAITING to work out"))

    subdomains = future.result()
    if len(subdomains)!=0:
        print(TOmiku('subdomains:')+'\n')
        for i in subdomains:
            if len(i)!=0:
                for j in i:
                    print(j)
    else:
        print(TOyellow('Sorry no subdomains found')+'\n')


    #print(subdomains)

whattime=time.time()-time1
print('\n'+TOmiku('[*]ALL DOWN,It took: ')+TOgreen(f'{whattime}')+TOmiku('s')+'\n')
