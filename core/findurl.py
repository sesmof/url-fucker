import re
from urllib.parse import urlparse

def find_urls_and_paths_in_file(file_path):
    # 定义URL的正则表达式
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+(?=[\s<>\'\"\\]|$)')
    # 定义相对路径的正则表达式
    path_pattern = re.compile(r'\.\./[^ \n\r\f\v\'\"]+|\.\\[^ \n\r\f\v\'\"]+')
    
    urls = []
    paths = []
    with open(file_path, 'r', encoding='utf-8') as file:###################
        
        for line in file:
            # 在每一行中查找URL
            
            possible_urls = re.findall(url_pattern, line)
            for url in possible_urls:
                # 使用urlparse验证是否是一个有效的URL
                try:
                    result = urlparse(url)
                    if all([result.scheme, result.netloc]):
                        try:
                            result = re.search('(.*?)<|(.*?)>', url)
                            result = re.search('(.*?)>|(.*?)<', url)
                            result=result.group(1)
                            urls.append(result)
                        except:
                            urls.append(url)
                except ValueError:
                    pass

            # 在每一行中查找相对路径
            possible_paths = re.findall(path_pattern, line)
            for path in possible_paths:
                paths.append(path)
                
    return urls, paths

# 测试
if __name__=="__main__":
    file_path = "downloads/index.html"
    urls_in_file, paths_in_file = find_urls_and_paths_in_file(file_path)
    print("URLs:", urls_in_file)
    print("Paths:", paths_in_file)


