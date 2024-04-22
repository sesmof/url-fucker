# Regular expression comes from https://github.com/GerbenJavado/LinkFinder
#👆↑这行注释来自于jsfinder: https://github.com/Threezh1/JSFinder
import re
from urllib.parse import urlparse

def find_urls_and_paths_in_file(file_path):
    # 定义URL的正则表达式
    # url_pattern = re.compile(r"""
	#   (?:"|')                               # Start newline delimiter
	#   (
	#     ((?:[a-zA-Z]{1,10}://|//)           # Match a scheme [a-Z]*1-10 or //
	#     [^"'/]{1,}\.                        # Match a domainname (any character + dot)
	#     [a-zA-Z]{2,}[^"']{0,})              # The domainextension and/or path
	#     |
	#     ((?:/|\.\./|\./)                    # Start with /,../,./
	#     [^"'><,;| *()(%%$^/\\\[\]]          # Next character can't be...
	#     [^"'><,;|()]{1,})                   # Rest of the characters can't be
	#     |
	#     ([a-zA-Z0-9_\-/]{1,}/               # Relative endpoint with /
	#     [a-zA-Z0-9_\-/]{1,}                 # Resource name
	#     \.(?:[a-zA-Z]{1,4}|action)          # Rest + extension (length 1-4 or action)
	#     (?:[\?|/][^"|']{0,}|))              # ? mark with parameters
	#     |
	#     ([a-zA-Z0-9_\-]{1,}                 # filename
	#     \.(?:php|asp|aspx|jsp|json|
	#          action|html|js|txt|xml)             # . + extension
	#     (?:\?[^"|']{0,}|))                  # ? mark with parameters
	#   )
	#   (?:"|')                               # End newline delimiter
	# """,re.VERBOSE)
    url_pattern = re.compile(r"""
    (?:"|')                               # Start newline delimiter
    (
        (?:(?:[a-zA-Z]{1,10}://|//)       # Match a scheme [a-Z]*1-10 or //
        [^"'/]{1,}\.                      # Match a domainname (any character + dot)
        [a-zA-Z]{2,}[^"']{0,})            # The domainextension and/or path
        |
        (?:(?:/|\.\./|\./)                # Start with /,../,./
        [^"'><,;| *()(%%$^/\\\[\]]        # Next character can't be...
        [^"'><,;|()]{1,})                 # Rest of the characters can't be
        |
        (?:(?:[a-zA-Z0-9_\-/]{1,}/        # Relative endpoint with /
        [a-zA-Z0-9_\-/]{1,}               # Resource name
        \.(?:[a-zA-Z]{1,4}|action)        # Rest + extension (length 1-4 or action)
        (?:[\?|/][^"|']{0,}|)))           # ? mark with parameters
        |
        (?:(?:[a-zA-Z0-9_\-]{1,}          # filename
        \.(?:php|asp|aspx|jsp|json|
             action|html|js|txt|xml|jpg|png)       # . + extension
        (?:\?[^"|']{0,}|)))               # ? mark with parameters
    )
    (?:"|')                               # End newline delimiter
""", re.VERBOSE)

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
                        # try:
                        #     result = re.search('(.*?)<|(.*?)>', url)
                        #     result = re.search('(.*?)>|(.*?)<', url)
                        #     result = re.search('(.*?))|(.*?)(', url)
                        #     result = re.search('(.*?)(|(.*?))', url)
                        #     result=result.group(1)
                        #     urls.append(result)
                        # except:
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
    file_path = r"..\downloads\index.html"
    urls_in_file, paths_in_file = find_urls_and_paths_in_file(file_path)
    print("URLs:", urls_in_file)
    print("Paths:", paths_in_file)


