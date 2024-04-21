# import requests
# from bs4 import BeautifulSoup
# def getxxx(url):
# # 发送GET请求

#     response = requests.get(url)

#     # 获取状态码
#     status_code = response.status_code
#     #print(f"状态码: {status_code}")

#     # 如果状态码为200，解析网页并获取标题
#     if status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         title = soup.title.string if soup.title else "No title found"
#     return status_code,title
import requests
from bs4 import BeautifulSoup
def getxxx(url):
    # 发送GET请求
    response = requests.get(url)
    response.encoding='utf-8'

    # 获取状态码
    status_code = response.status_code

    # 初始化title为None
    title = "No title found"
    status_code == 'None'


    # 如果状态码为200，解析网页并获取标题
    if status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"

    return status_code, title
