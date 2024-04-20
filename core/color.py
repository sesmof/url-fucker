
import os
try:
    os.system('')  # 开启windows CMD的ANSI转义序列支持
except:
    pass

def TOred(st):
    return '\033[31m'+st+'\033[0m'
def TOgreen(st):
    return '\033[32m'+st+'\033[0m'
def TOmiku(st):
    return '\033[36m'+st+'\033[0m'
def TObulue(st):
    return '\033[34m'+st+'\033[0m'
def TObling(st):
    return '\033[5m'+st+'\033[0m'
def TOyellow(st):
    return '\033[33m'+st+'\033[0m'


if __name__=='__main__':
    print(TOgreen('测试'))
    print(TOred('测试'))
    print(TObulue('测试'))
    print(TOmiku('hatsune miku'))
    print(TObling('测试'))
    print(TOyellow('测试'))


'''
COPILOT:
当然，这是ANSI转义序列的完整颜色列表：

\033[0m：重置所有属性
\033[1m：加粗
\033[2m：一般的灰色
\033[3m：斜体
\033[4m：下划线
\033[5m：闪烁
\033[6m：快速闪烁
\033[7m：反显
\033[8m：不可见
颜色代码：

\033[30m：黑色
\033[31m：红色
\033[32m：绿色
\033[33m：黄色
\033[34m：蓝色
\033[35m：洋红色
\033[36m：青色
\033[37m：白色
背景颜色代码：

\033[40m：黑色
\033[41m：红色
\033[42m：绿色
\033[43m：黄色
\033[44m：蓝色
\033[45m：洋红色
\033[46m：青色
\033[47m：白色
每个颜色代码都以\033[开头，然后是两位数的颜色代码，最后以m结尾。例如，\033[31m就是设置文本颜色为红色。

希望这个信息对你有所帮助！
'''