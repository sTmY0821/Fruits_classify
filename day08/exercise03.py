def course_name(number):
    """

    :param number:
    :return:
    """
    if number == "1":
        return "Python语言和心教程"
    elif number == "2":
        return "Python高级软件技术"
    elif number == "3":
        return "web全栈"
    elif number == "4":
        return "人工智能"
    else:
        return

def course_name02(number):
    dict_course ={
        "1":"Python语言和心教程",
        "2":"Python高级软件技术",
        "3":"web全栈",
        "4":"人工智能"
    }
    return dict_course[number]


def calculate_iq(ma, ca):
    """
    计算IQ
    :param ma: int，心理年龄
    :param ca: int，实际年龄
    :return: str，IQ等级
    """
    iq = ma / ca * 100
    if iq >= 140:
        return "天才"
    elif iq >= 120:
        return "超常"
    elif iq >= 110:
        return "聪慧"
    elif iq >= 90:
        return "正常"
    elif iq >= 80:
        return "迟钝"
    else:
        return "低能"


