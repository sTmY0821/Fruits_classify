"""
二进制文件
"""
#二进制操作用“rb”
with open("day20pic.webp","rb") as file:
    with open("copy.webp","wb") as file_write:
        content = file.read()
        file_write.write(b"110")#先写入三个干扰字节
        file_write.write(content)