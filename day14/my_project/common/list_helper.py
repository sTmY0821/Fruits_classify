def calculate_live_days():
    """
    计算活细胞数
    :return:
    """
    live_cell_count = 0
    for i in range(1, 101):
        if i % 2 == 0:
            live_cell_count += 1
    return live_cell_count