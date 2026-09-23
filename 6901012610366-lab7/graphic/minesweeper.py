from processing import *
import random

# กำหนดขนาดกระดาน
COLS = 20
ROWS = 20
CELL = 90
BOARD_W = COLS * CELL
BOARD_H = ROWS * CELL
INFO_H = 70
WIDTH = BOARD_W
HEIGHT = BOARD_H + INFO_H

TOTAL_MINES = 15

# สถานะของเกม
grid_mines = []       # เก็บ True/False ว่ามีระเบิดไหม
grid_revealed = []    # เก็บ True/False ว่าเปิดแล้วหรือยัง
grid_flagged = []     # เก็บ True/False ว่าปักธงอยู่ไหม
grid_counts = []      # เก็บตัวเลขจำนวนระเบิดรอบช่อง

first_click = True
game_over = False
game_won = False


def setup():
    size(WIDTH, HEIGHT)
    rectMode(CORNER)
    textAlign(CENTER, CENTER)
    reset_game()


def reset_game():
    global grid_mines, grid_revealed, grid_flagged, grid_counts
    global first_click, game_over, game_won

    grid_mines = [[False for _ in range(COLS)] for _ in range(ROWS)]
    grid_revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
    grid_flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]
    grid_counts = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    first_click = True
    game_over = False
    game_won = False


def place_mines(start_r, start_c):
    # วางระเบิดแบบสุ่ม โดยเว้นช่องแรกที่ผู้เล่นคลิกไว้
    positions = [(r, c) for r in range(ROWS) for c in range(COLS) if not (r == start_r and c == start_c)]
    mine_positions = random.sample(positions, TOTAL_MINES)

    for r, c in mine_positions:
        grid_mines[r][c] = True

    # คำนวณจำนวนระเบิดรอบช่อง
    for r in range(ROWS):
        for c in range(COLS):
            if grid_mines[r][c]:
                continue
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid_mines[nr][nc]:
                            count += 1
            grid_counts[r][c] = count


def reveal_cell(r, c):
    if not (0 <= r < ROWS and 0 <= c < COLS):
        return
    if grid_revealed[r][c] or grid_flagged[r][c]:
        return

    grid_revealed[r][c] = True

    # ถ้าช่องนี้ไม่มีระเบิดรอบข้าง (เลข 0) ให้เปิดช่องข้างเคียงแบบอัตโนมัติ
    if grid_counts[r][c] == 0 and not grid_mines[r][c]:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr != 0 or dc != 0:
                    reveal_cell(r + dr, c + dc)


def check_win():
    for r in range(ROWS):
        for c in range(COLS):
            if not grid_mines[r][c] and not grid_revealed[r][c]:
                return False
    return True


def draw():
    background(200)
    draw_board()
    draw_info()


def draw_board():
    stroke(120)
    strokeWeight(1)

    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL
            y = r * CELL

            if grid_revealed[r][c]:
                if grid_mines[r][c]:
                    # ช่องระเบิดที่ระเบิดแล้ว
                    fill(230, 70, 70)
                    rect(x, y, CELL, CELL)
                    fill(0)
                    textSize(20)
                    text("*", x + CELL / 2, y + CELL / 2 + 5)
                else:
                    # ช่องที่เปิดแล้ว
                    fill(235)
                    rect(x, y, CELL, CELL)
                    count = grid_counts[r][c]
                    if count > 0:
                        set_number_color(count)
                        textSize(18)
                        text(str(count), x + CELL / 2, y + CELL / 2)
            else:
                # ช่องที่ยังไม่ได้เปิด
                fill(170)
                rect(x, y, CELL, CELL)

                # ปักธง
                if grid_flagged[r][c]:
                    fill(230, 50, 50)
                    textSize(18)
                    text("F", x + CELL / 2, y + CELL / 2)


def set_number_color(num):
    colors = {
        1: (20, 40, 220),
        2: (25, 130, 30),
        3: (210, 30, 30),
        4: (110, 20, 130),
        5: (140, 30, 30),
        6: (30, 140, 140),
        7: (0, 0, 0),
        8: (100, 100, 100),
    }
    rgb = colors.get(num, (0, 0, 0))
    fill(rgb[0], rgb[1], rgb[2])


def draw_info():
    noStroke()
    fill(35)
    rect(0, BOARD_H, WIDTH, INFO_H)

    fill(255)
    textSize(18)

    # นับจำนวนธงที่ปักไป
    flags_used = sum(row.count(True) for row in grid_flagged)
    remaining_mines = TOTAL_MINES - flags_used

    if game_won:
        msg = "ชนะแล้ว! ยินดีด้วย (กด R เพื่อเริ่มใหม่)"
    elif game_over:
        msg = "โดนระเบิด! จบเกม (กด R เพื่อเริ่มใหม่)"
    else:
        msg = f"กับระเบิดคงเหลือ: {remaining_mines} | R: รีเซ็ต"

    text(msg, WIDTH / 2, BOARD_H + INFO_H / 2)


def mousePressed():
    global first_click, game_over, game_won

    if game_over or game_won or mouseY >= BOARD_H:
        return

    c = int(mouseX // CELL)
    r = int(mouseY // CELL)

    if not (0 <= r < ROWS and 0 <= c < COLS):
        return

    # คลิกขวา: ปักธง หรือ ถอนธง
    if mouseButton == RIGHT:
        if not grid_revealed[r][c]:
            grid_flagged[r][c] = not grid_flagged[r][c]
        return

    # คลิกซ้าย: เปิดช่อง
    if mouseButton == LEFT:
        if grid_flagged[r][c]:
            return

        if first_click:
            place_mines(r, c)
            first_click = False

        if grid_mines[r][c]:
            # เหยียบระเบิด
            grid_revealed[r][c] = True
            game_over = True
            # เปิดให้เห็นระเบิดทั้งหมด
            for i in range(ROWS):
                for j in range(COLS):
                    if grid_mines[i][j]:
                        grid_revealed[i][j] = True
        else:
            reveal_cell(r, c)
            if check_win():
                game_won = True


def keyPressed():
    if key in ("r", "R"):
        reset_game()


run()