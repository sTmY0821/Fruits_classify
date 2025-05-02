"""
文件写入
w 为覆盖写，会删除原来的

"""
with open ("../day01/arcgis_insert.py","w",encoding="utf-8") as file:
    file.write("#hello world\n")
    file.write("#hello world\n")
    file.write("#hello world")