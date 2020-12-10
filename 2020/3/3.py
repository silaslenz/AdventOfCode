board = []

with open("input.txt",'r') as file:
    lines = file.read().splitlines()

for line in lines:
    board_row = []
    for col in line:
        board_row.append(col == "#")
    board.append(board_row)

def get_trees(board, diff_x, diff_y):
    trees = 0
    pos = [0,0]
    while pos[0] < len(board):
        if board[pos[0]][pos[1]%(len(board[0]))]:
            trees += 1
        pos[0] += diff_x
        pos[1] += diff_y
    return trees

print(get_trees(board, 1, 3))
print(get_trees(board, 1, 1) * get_trees(board, 1, 3) * get_trees(board, 1, 5) * get_trees(board, 1, 7) * get_trees(board, 2, 1))