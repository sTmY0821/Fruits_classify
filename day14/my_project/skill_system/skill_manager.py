import skill_deployer as sd
def calculate_live_days():
    """
    计算活细胞数
    :return:
    """
    live_cell = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if i % 2 == 0 and j % 2 == 0:
                live_cell += 1
            elif i % 2 == 1 and j % 2 == 1:
                live_cell += 1
    return live_cell

sd.ai()