def get_valid_score():
    while True:
        try:
            score = int(input("请输入成绩："))
            if score < 0 or score > 100:
                raise ValueError("成绩应在0到100之间")
            return score
        except ValueError as e:
            print(f"输入错误: {e}，请重新输入")

def get_score():
    score = get_valid_score()
    print("成绩为：", score)
    return score

# 示例调用
if __name__ == "__main__":
    get_score()