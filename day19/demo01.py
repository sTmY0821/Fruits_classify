"""
读取文件
"""
# 1.打开
with open("/Users/suotiemengyang/Desktop/Python项目/month1/pythonProject1/day18/demo01.py", "r",
          encoding="utf-8") as file:
    print(file.read())
file01 = open("/Users/suotiemengyang/Desktop/Python项目/month1/pythonProject1/day18/demo01.py", "r", encoding="utf-8")
try:
    print(file01.read())
finally:
    file01.close()
# 路径
with open("../day01/homework.py", "r", encoding="utf-8") as file:
    print(file.read())
#离开缩进后一定自动关闭