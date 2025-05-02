"""
可迭代对象工具集
"""
import math


class IterableHelper:
    """
    封装对可迭代对象常用的高阶函数
    """
    @staticmethod
    def find_single(iterable, condition):
        """
        根据任意可迭代对象，以任意条件查找第一个满足的对象
        :param iterable:
        :param condition:
        :return: 第一个满足条件的元素
        """
        for iterm in iterable:
            if condition(iterm):
                return iterm

    @staticmethod
    def find_everything(iterable,condition):
        for iterm in iterable:
            if condition(iterm):
                yield iterm

    @staticmethod
    def accumulate(iterable, condition):
        value = 0
        for item in iterable:
            value += condition(item)
        return value

    @staticmethod
    def del_single(iterable, condition):
        for index,item in enumerate(iterable):
            if condition(item):
                del iterable[index]
                break

    @staticmethod
    def del_everything(iterable, condition):
        for i in range(len(iterable)-1,-1,-1):
            # 倒序遍历
            if condition(iterable[i]):
                del iterable[i]
    @staticmethod
    def get_max(iterable, condition):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_value) < condition(iterable[i]):
                max_value = iterable[i]
        return max_value
    @staticmethod
    def get_min(iterable,condition):
        min_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(min_value) > condition(iterable[i]):
                min_value = iterable[i]
        return min_value

    @staticmethod
    def sort_from_small_big(iterable, condition):
        for i in range(len(iterable)-1):
            for j in range(i+1,len(iterable)):
                if condition(iterable[i]) > condition(iterable[j]):
                    iterable[i],iterable[j] = iterable[j],iterable[i]

    @staticmethod
    def sort_from_big_small(iterable, condition):
        for i in range(len(iterable) - 1):
            for j in range(i + 1, len(iterable)):
                if condition(iterable[i]) < condition(iterable[j]):
                    iterable[i], iterable[j] = iterable[j], iterable[i]

    @staticmethod
    def if_same_attribute(iterable, condition):
        for i in range(len(iterable) - 1):
            for j in range(i + 1, len(iterable)):
                if condition(iterable[i]) == condition(iterable[j]):
                    return True
        return False




