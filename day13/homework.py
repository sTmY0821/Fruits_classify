#practice01
from future.backports.datetime import datetime


def calculate_week():
    year = input("请输入年份")
    month = input("请输入月份")
    day = input("请输入日期")
    weekday = datetime(int(year), int(month), int(day)).weekday()
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    print(f"{year}年{month}月{day}日是{weekdays[weekday]}")

calculate_week()

#practice02
def calculate_live_days():
    year = input("请输入年份")
    month = input("请输入月份")
    day = input("请输入日期")
    live_days = datetime.now() - datetime(int(year), int(month), int(day))
    print(f"您已经活了{live_days.days}天")
    print(f"您已经活了{live_days.seconds}秒")
    print(f"您已经活了{live_days.total_seconds()}秒")
    print()

calculate_live_days()