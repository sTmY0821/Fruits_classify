#调用生成器函数 会产生生成器函数
"""
生成器的运用：
定义一个函数，在列表中筛选出偶数
"""
list01 = [4,3,45,13,13,4,5,6,87,50]
def find_even():
    for iterm in list01:
        if iterm % 2 == 0:
            yield iterm

for iterm in find_even():
    print(iterm)