import random

def print_board(board):
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if r != 2:
            print("---|---|---")

def check_win(board, player):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                return False
    return True

def computer_move(board):
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == ' ':
            return x, y

board = [[' ' for _ in range(3)] for _ in range(3)]
while True:
    print_board(board)
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))
    if board[x][y] != ' ':
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y] = 'X'
    if check_win(board, 'X'):
        print_board(board)
        print("축하합니다! 당신이 이겼습니다.")
        break
    elif check_draw(board):
        print_board(board)
        print("무승부입니다!")
        break

    print("컴퓨터의 차례입니다.")
    cx, cy = computer_move(board)
    board[cx][cy] = 'O'
    if check_win(board, 'O'):
        print_board(board)
        print("컴퓨터가 이겼습니다.")
        break
    elif check_draw(board):
        print_board(board)
        print("무승부입니다!")
        break
