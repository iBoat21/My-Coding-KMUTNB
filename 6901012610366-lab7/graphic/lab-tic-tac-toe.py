from processing import *

CELL = 150
GRID = 3
BOARD_SIZE = CELL * GRID
INFO_HEIGHT = 80
WIDTH = BOARD_SIZE
HEIGHT = BOARD_SIZE + INFO_HEIGHT

board = [["" for _ in range(GRID)] for _ in range(GRID)]
current_player = "X"
winner = None       # "X", "O", "Draw" หรือ None
win_line = None     # ((r1, c1), (r2, c2)) จุดเริ่มและจุดสิ้นสุดของเส้นที่ชนะ


def setup():
    size(WIDTH, HEIGHT)
    rectMode(CORNER)
    textAlign(CENTER, CENTER)


def draw():
    background(245)
    draw_grid()
    draw_marks()
    draw_info()
    if win_line:
        draw_win_line()


def draw_grid():
    stroke(40)
    strokeWeight(4)
    for i in range(1, GRID):
        line(i * CELL, 0, i * CELL, BOARD_SIZE)
        line(0, i * CELL, BOARD_SIZE, i * CELL)


def draw_marks():
    strokeWeight(6)
    for r in range(GRID):
        for c in range(GRID):
            mark = board[r][c]
            x = c * CELL
            y = r * CELL
            pad = 30
            if mark == "X":
                stroke(220, 60, 60)
                line(x + pad, y + pad, x + CELL - pad, y + CELL - pad)
                line(x + CELL - pad, y + pad, x + pad, y + CELL - pad)
            elif mark == "O":
                stroke(60, 100, 220)
                noFill()
                ellipse(x + CELL / 2, y + CELL / 2, CELL - 2 * pad, CELL - 2 * pad)


def draw_info():
    noStroke()
    fill(30)
    rect(0, BOARD_SIZE, WIDTH, INFO_HEIGHT)
    fill(255)
    textSize(22)
    if winner is None:
        msg = f"ตาของผู้เล่น: {current_player}"
    elif winner == "Draw":
        msg = "เสมอ!  กด R เพื่อเริ่มใหม่"
    else:
        msg = f"{winner} ชนะ!  กด R เพื่อเริ่มใหม่"
    text(msg, WIDTH / 2, BOARD_SIZE + INFO_HEIGHT / 2)


def draw_win_line():
    (r1, c1), (r2, c2) = win_line
    x1 = c1 * CELL + CELL / 2
    y1 = r1 * CELL + CELL / 2
    x2 = c2 * CELL + CELL / 2
    y2 = r2 * CELL + CELL / 2
    stroke(20, 160, 20)
    strokeWeight(8)
    line(x1, y1, x2, y2)


# เปลี่ยนเป็น mousePressed และ mouseX, mouseY
def mousePressed():
    global current_player, winner, win_line

    if winner is not None or mouseY >= BOARD_SIZE:
        return

    col = int(mouseX // CELL)
    row = int(mouseY // CELL)

    if board[row][col] == "":
        board[row][col] = current_player
        result, matched_line = check_winner()
        if result:
            winner = result
            win_line = matched_line
        else:
            current_player = "O" if current_player == "X" else "X"


# เปลี่ยนเป็น keyPressed
def keyPressed():
    if key in ("r", "R"):
        reset_game()


def reset_game():
    global board, current_player, winner, win_line
    board = [["" for _ in range(GRID)] for _ in range(GRID)]
    current_player = "X"
    winner = None
    win_line = None


def check_winner():
    lines = []
    for i in range(GRID):
        lines.append([(i, 0), (i, 1), (i, 2)])
        lines.append([(0, i), (1, i), (2, i)])

    lines.append([(0, 0), (1, 1), (2, 2)])
    lines.append([(0, 2), (1, 1), (2, 0)])

    for combo in lines:
        (r1, c1), (r2, c2), (r3, c3) = combo
        v1, v2, v3 = board[r1][c1], board[r2][c2], board[r3][c3]
        if v1 != "" and v1 == v2 == v3:
            return v1, (combo[0], combo[2])

    if all(board[r][c] != "" for r in range(GRID) for c in range(GRID)):
        return "Draw", None

    return None, None


run()