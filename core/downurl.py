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
# import os
# import requests
# import shutil
# from bs4 import BeautifulSoup

# try:
#     shutil.rmtree('downloads')
# except:
#     pass

# def download_file(url, local_filename):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     with requests.get(url, stream=True, headers=headers) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 f.write(chunk)

# def download_webpage(url, folder="."):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # 创建目标文件夹，如果不存在的话
#     os.makedirs(folder, exist_ok=True)

#     for link in soup.find_all('link'):
#         if 'stylesheet' in link['rel']:
#             css_url = link['href']
#             if not css_url.startswith('http'):
#                 css_url = url + css_url
#             css_file = os.path.join(folder, os.path.basename(css_url).replace('?', '_'))
#             try:
#                 download_file(css_url, css_file)
#             except:
#                 pass

#     for script in soup.find_all('script'):
#         js_url = script.get('src')
#         if js_url:  # 检查js_url是否为None
#             if not js_url.startswith('http'):
#                 js_url = url + js_url
#             js_file = os.path.join(folder, os.path.basename(js_url).replace('?', '_'))
#             try:
#                 download_file(js_url, js_file)
#             except:
#                 pass

#     with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
#         f.write(response.text)

# if __name__=='__main__':
#     download_webpage('http://dongxiaoqu.zhengzhong.cn/', 'downloads')

# import os
# import requests
# import shutil
# from bs4 import BeautifulSoup

# try:
#     shutil.rmtree('downloads')
# except:
#     pass

# def download_file(url, local_filename):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     with requests.get(url, stream=True, headers=headers) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 f.write(chunk)

# def download_webpage(url, folder="."):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # 创建目标文件夹，如果不存在的话
#     os.makedirs(folder, exist_ok=True)

#     for link in soup.find_all('link'):
#         if 'stylesheet' in link['rel']:
#             css_url = link['href']
#             if not css_url.startswith('http'):
#                 css_url = url + css_url
#             css_file = os.path.join(folder, os.path.basename(css_url).replace('?', '_'))
#             try:
#                 download_file(css_url, css_file)
#             except:
#                 pass

#     for script in soup.find_all('script'):
#         js_url = script.get('src')
#         if js_url:  # 检查js_url是否为None
#             if not js_url.startswith('http'):
#                 js_url = url + js_url
#             js_file = os.path.join(folder, os.path.basename(js_url).replace('?', '_'))
#             try:
#                 download_file(js_url, js_file)
#             except:
#                 pass

#     with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
#         f.write(response.text)

# if __name__=='__main__':
#     download_webpage('http://dongxiaoqu.zhengzhong.cn/', 'downloads')

#######################

# import os
# import requests
# import shutil
# import hashlib
# from bs4 import BeautifulSoup

# # 获取当前脚本的路径
# script_path = os.path.dirname(os.path.realpath(__file__))
# downloads_folder = os.path.join(script_path, 'downloads')

# try:
#     shutil.rmtree(downloads_folder)
# except:
#     pass

# def download_file(url, local_filename):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     with requests.get(url, stream=True, headers=headers) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 f.write(chunk)

# def download_webpage(url, folder="."):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # 创建目标文件夹，如果不存在的话
#     os.makedirs(folder, exist_ok=True)

#     for link in soup.find_all('link'):
#         if 'stylesheet' in link['rel']:
#             css_url = link['href']
#             if not css_url.startswith('http'):
#                 css_url = url + css_url
#             css_file = os.path.join(folder, os.path.basename(css_url).replace('?', '_'))
#             try:
#                 download_file(css_url, css_file)
#             except:
#                 pass

#     for script in soup.find_all('script'):
#         js_url = script.get('src')
#         if js_url:  # 检查js_url是否为None
#             if not js_url.startswith('http'):
#                 js_url = url + js_url
#             js_file = os.path.join(folder, os.path.basename(js_url).replace('?', '_'))
#             try:
#                 download_file(js_url, js_file)
#             except:
#                 pass
#         else:  # 如果没有src属性，那么这是一个内联脚本
#             inline_js = script.string
#             if inline_js:  # 检查内联脚本是否为空
#                 # 使用脚本内容的哈希值作为文件名
#                 js_file = os.path.join(folder, hashlib.md5(inline_js.encode()).hexdigest() + '.js')
#                 with open(js_file, 'w', encoding='utf-8') as f:
#                     f.write(inline_js)

#     with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
#         f.write(response.text)

# if __name__=='__main__':
#     download_webpage('http://dongxiaoqu.zhengzhong.cn/', 'downloads')
# ###########################
# import os
# import requests
# import shutil
# from bs4 import BeautifulSoup
# from urllib.parse import urlparse

# # 获取当前脚本的路径
# # script_path = os.path.dirname(os.path.realpath(__file__))
# # downloads_folder = os.path.join(script_path, 'downloads')

# try:
#    shutil.rmtree('downloads')
# except:
#     print('-')

# def download_file(url, local_filename):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     with requests.get(url, stream=True, headers=headers) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 f.write(chunk)

# def download_webpage(url, folder="."):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # 创建目标文件夹，如果不存在的话
#     os.makedirs(folder, exist_ok=True)

#     for link in soup.find_all('link'):
#         if 'stylesheet' in link['rel']:
#             css_url = link['href']
#             if not css_url.startswith('http'):
#                 css_url = url + css_url
#             css_file = os.path.join(folder, os.path.basename(urlparse(css_url).path))
#             try:
#                 download_file(css_url, css_file)
#             except:
#                 pass

#     for script in soup.find_all('script'):
#         js_url = script.get('src')
#         if js_url:  # 检查js_url是否为None
#             if not js_url.startswith('http'):
#                 js_url = url + js_url
#             js_file = os.path.join(folder, os.path.basename(urlparse(js_url).path))
#             try:
#                 download_file(js_url, js_file)
#             except:
#                 pass

#     with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
#         f.write(response.text)

# if __name__=='__main__':
#     download_webpage('http://www.hdzxy.com', 'downloads')
########
import os
import requests
import shutil
from bs4 import BeautifulSoup
from urllib.parse import urljoin

try:
    shutil.rmtree('downloads')
except:
    pass

def download_file(url, local_filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    if url is not None and url != 'None':
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
                css_url = urljoin(url, css_url)
            css_file = os.path.join(folder, os.path.basename(css_url).replace('?', '_'))
            try:
                download_file(css_url, css_file)
            except:
                pass

    # 合并嵌入在<script>标签中的JavaScript代码
    combined_js_code = ""
    for script in soup.find_all('script'):
        js_url = script.get('src')
        if js_url and js_url != 'None':
            if not js_url.startswith('http'):
                js_url = urljoin(url, js_url)
            js_file = os.path.join(folder, os.path.basename(js_url).replace('?', '_'))
            try:
                download_file(js_url, js_file)
            except:
                pass
        else:
            js_code = script.string
            if js_code:
                combined_js_code += js_code + "\n"

    # 将合并后的JavaScript代码写入文件
    combined_js_file = os.path.join(folder, 'combined.js')
    with open(combined_js_file, 'w', encoding='utf-8') as f:
        f.write(combined_js_code)

    # 删除其他的script_xx.js类型的文件
    

    # 保存整个页面
    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(response.text)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 创建目标文件夹，如果不存在的话
    os.makedirs(folder, exist_ok=True)

    for link in soup.find_all('link'):
        if 'stylesheet' in link['rel']:
            css_url = link['href']
            if not css_url.startswith('http'):
                css_url = urljoin(url, css_url)
            css_file = os.path.join(folder, os.path.basename(css_url).replace('?', '_'))
            try:
                download_file(css_url, css_file)
            except:
                pass

    # 合并嵌入在<script>标签中的JavaScript代码
    combined_js_code = ""
    for script in soup.find_all('script'):
        js_url = script.get('src')
        if js_url and js_url != 'None':
            if not js_url.startswith('http'):
                js_url = urljoin(url, js_url)
            js_file = os.path.join(folder, os.path.basename(js_url).replace('?', '_'))
            try:
                download_file(js_url, js_file)
            except:
                pass
        else:
            js_code = script.string
            if js_code:
                combined_js_code += js_code + "\n"

    # 将合并后的JavaScript代码写入文件
    combined_js_file = os.path.join(folder, 'combined.js')
    with open(combined_js_file, 'w', encoding='utf-8') as f:
        f.write(combined_js_code)

    # 保存整个页面
    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(response.text)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 创建目标文件夹，如果不存在的话
    os.makedirs(folder, exist_ok=True)

    for link in soup.find_all('link'):
        if 'stylesheet' in link['rel']:
            css_url = link['href']
            if not css_url.startswith('http'):
                css_url = urljoin(url, css_url)
            css_file = os.path.join(folder, os.path.basename(css_url).replace('?', '_'))
            try:
                download_file(css_url, css_file)
            except:
                pass

    script_count = 1
    for script in soup.find_all('script'):
        js_url = script.get('src')
        if js_url and js_url != 'None':  # 检查js_url是否为None
            if not js_url.startswith('http'):
                js_url = urljoin(url, js_url)
            js_file = os.path.join(folder, os.path.basename(js_url).replace('?', '_'))
            try:
                download_file(js_url, js_file)
            except:
                pass
        else:
            # 处理嵌入在<script>标签中的JavaScript代码
            js_code = script.string
            if js_code:
                js_file = os.path.join(folder, f'script_{script_count}.js')
                with open(js_file, 'w', encoding='utf-8') as f:
                    f.write(js_code)
                script_count += 1

    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(response.text)


    for script in soup.find_all('script'):
        js_url = script.get('src')
        if js_url and js_url != 'None':  # 检查js_url是否为None
            if not js_url.startswith('http'):
                js_url = urljoin(url, js_url)
            js_file = os.path.join(folder, os.path.basename(js_url).replace('?', '_'))
            try:
                download_file(js_url, js_file)
            except:
                pass
    for filename in os.listdir(folder):
        if filename.startswith('script_') and filename.endswith('.js') and filename != 'combined.js':
            os.remove(os.path.join(folder, filename))
    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(response.text)

if __name__=='__main__':
    download_webpage('http://dongxiaoqu.zhengzhong.cn/', 'downloads')
