import random


def init_board():
    """初始化4x4游戏板"""
    board = [[0] * 4 for _ in range(4)]
    add_new_number(board)
    add_new_number(board)
    return board


def add_new_number(board):
    """在空白位置随机生成2（90%概率）或4（10%概率）"""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4


def print_board(board):
    """打印游戏板"""
    print("-" * 25)
    for row in board:
        print("|" + "|".join(f"{num:4d}" if num != 0 else "    " for num in row) + "|")
        print("-" * 25)


def merge(row):
    """合并一行中的相同数字并左对齐"""
    new_row = [0] * 4
    index = 0
    prev = None

    for num in row:
        if num:
            if prev is None:
                prev = num
            else:
                if prev == num:
                    new_row[index] = prev * 2
                    index += 1
                    prev = None
                else:
                    new_row[index] = prev
                    index += 1
                    prev = num
    if prev is not None:
        new_row[index] = prev

    return new_row, new_row != row


def move_left(board):
    """向左移动"""
    moved = False
    for i in range(4):
        new_row, changed = merge(board[i])
        if changed:
            board[i] = new_row
            moved = True
    return moved


def move_right(board):
    """向右移动"""
    moved = False
    for i in range(4):
        reversed_row = board[i][::-1]
        new_row, changed = merge(reversed_row)
        if changed:
            board[i] = new_row[::-1]
            moved = True
    return moved


def move_up(board):
    """向上移动"""
    moved = False
    transposed = list(zip(*board))
    for i in range(4):
        new_row, changed = merge(list(transposed[i]))
        if changed:
            transposed[i] = new_row
            moved = True
    if moved:
        for i in range(4):
            board[i] = list(transposed[i])
    return moved


def move_down(board):
    """向下移动"""
    moved = False
    transposed = list(zip(*board))
    for i in range(4):
        reversed_row = transposed[i][::-1]
        new_row, changed = merge(list(reversed_row))
        if changed:
            transposed[i] = list(new_row[::-1])
            moved = True
    if moved:
        for i in range(4):
            board[i] = list(transposed[i])
    return moved


def is_game_over(board):
    """检查游戏是否结束"""
    # 检查是否有空位
    if any(0 in row for row in board):
        return False

    # 检查水平或垂直方向是否有可合并的数字
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False
    return True


def main():
    board = init_board()
    while True:
        print_board(board)
        if is_game_over(board):
            print("游戏结束！")
            break

        move = input("使用方向键（W上 S下 A左 D右 Q退出）：").upper()
        moved = False

        if move == 'A':
            moved = move_left(board)
        elif move == 'D':
            moved = move_right(board)
        elif move == 'W':
            moved = move_up(board)
        elif move == 'S':
            moved = move_down(board)
        elif move == 'Q':
            break
        else:
            print("无效输入！请使用W/A/S/D")
            continue

        if moved:
            add_new_number(board)

        # 检查胜利条件
        if any(2048 in row for row in board):
            print_board(board)
            print("恭喜！你成功合成了2048！")
            break


if __name__ == "__main__":
    main()