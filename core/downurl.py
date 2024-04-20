# import os
# import requests
# import shutil
# from bs4 import BeautifulSoup

# try:
#     shutil.rmtree('downloads')
# except:
#     pass
# def download_file(url, local_filename):
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 f.write(chunk)


# def download_webpage(url, folder="."):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # 创建目标文件夹，如果不存在的话
#     os.makedirs(folder, exist_ok=True)

#     for link in soup.find_all('link'):
#         if 'stylesheet' in link['rel']:
#             css_url = link['href']
#             if not css_url.startswith('http'):
#                 css_url = url + css_url
#             css_file = os.path.join(folder, os.path.basename(css_url).replace('?', '_'))

#             download_file(css_url, css_file)



#     for script in soup.find_all('script'):
#         js_url = script.get('src')
#         if js_url:  # 检查js_url是否为None
#             if not js_url.startswith('http'):
#                 js_url = url + js_url
#             js_file = os.path.join(folder, os.path.basename(js_url).replace('?', '_'))
#             download_file(js_url, js_file)

#     with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
#         f.write(response.text)

# if __name__=='__main__':
#     download_webpage('http://dongxiaoqu.zhengzhong.cn/', 'downloads')
import os
import requests
import shutil
from bs4 import BeautifulSoup

try:
    shutil.rmtree('downloads')
except:
    pass

def download_file(url, local_filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    with requests.get(url, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)

def download_webpage(url, folder="."):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 创建目标文件夹，如果不存在的话
    os.makedirs(folder, exist_ok=True)

    for link in soup.find_all('link'):
        if 'stylesheet' in link['rel']:
            css_url = link['href']
            if not css_url.startswith('http'):
                css_url = url + css_url
            css_file = os.path.join(folder, os.path.basename(css_url).replace('?', '_'))
            try:
                download_file(css_url, css_file)
            except:
                pass

    for script in soup.find_all('script'):
        js_url = script.get('src')
        if js_url:  # 检查js_url是否为None
            if not js_url.startswith('http'):
                js_url = url + js_url
            js_file = os.path.join(folder, os.path.basename(js_url).replace('?', '_'))
            try:
                download_file(js_url, js_file)
            except:
                pass

    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(response.text)

if __name__=='__main__':
    download_webpage('http://dongxiaoqu.zhengzhong.cn/', 'downloads')
