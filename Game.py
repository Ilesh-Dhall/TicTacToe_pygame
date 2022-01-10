import pygame
import time
import os

pygame.init()

# Game Window
WIDTH, HEIGHT = 450, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe Game!")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Variables
FPS = 60
XO = "x"
winner = None
draw = None

# Load Images
X = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "X.png")), (140, 140))
O = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "O.png")), (140, 140))
TTT_OP = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TTT_op.png")), (WIDTH, 480))

# Initializing Game Board
Game_board = [[None] * 3, [None] * 3, [None] * 3]


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(TTT_OP, (0, 47))
    pygame.display.update()
    time.sleep(1.5)
    WIN.fill(WHITE)

    # Game Board Borders
    pygame.draw.line(WIN, BLACK, (150, 0), (150, 450), 5)
    pygame.draw.line(WIN, BLACK, (300, 0), (300, 450), 5)
    pygame.draw.line(WIN, BLACK, (0, 150), (WIDTH, 150), 5)
    pygame.draw.line(WIN, BLACK, (0, 300), (WIDTH, 300), 5)
    pygame.draw.line(WIN, BLACK, (0, 450), (WIDTH, 450), 5)

    # Game Window Borders
    pygame.draw.line(WIN, BLACK, (0, 0), (0, HEIGHT), 5)
    pygame.draw.line(WIN, BLACK, (0, 0), (WIDTH, 0), 5)
    pygame.draw.line(WIN, BLACK, (WIDTH, 0), (WIDTH, HEIGHT), 5)
    pygame.draw.line(WIN, BLACK, (0, HEIGHT), (WIDTH, HEIGHT), 5)

    pygame.draw.rect(WIN, BLACK, pygame.Rect(0, 450, WIDTH, 150))

    pygame.display.update()


def draw_status():
    global draw
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " Won!"
    if draw:
        message = "Its a Tie!"

    text = pygame.font.SysFont("comicsans", 40)
    text = text.render(message, 1, WHITE)
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0, 450, WIDTH, 150))

    WIN.blit(text, (WIDTH / 2 - 55, 435 + 150 / 2))
    pygame.display.update()


def draw_XO(row, col):
    global XO, Game_board

    if col == 1:
        posx = 5

    if col == 2:
        posx = 5 + (WIDTH / 3)

    if col == 3:
        posx = 5 + ((WIDTH / 3) * 2)

    if row == 1:
        posy = 5

    if row == 2:
        posy = 5 + (450 / 3)

    if row == 3:
        posy = 5 + ((450 / 3) * 2)

    Game_board[row - 1][col - 1] = XO

    if (XO == "x"):
        WIN.blit(X, (posx, posy))
        XO = "o"

    else:
        WIN.blit(O, (posx, posy))
        XO = "x"
    pygame.display.update()


def user_click():
    x, y = pygame.mouse.get_pos()

    if (x < WIDTH / 3 and x > 0):
        col = 1

    elif (x < (WIDTH / 3) * 2 and x > WIDTH / 3):
        col = 2

    elif (x < WIDTH and x > (WIDTH / 3) * 2):
        col = 3

    else:
        col = None

    if (y < 450 / 3 and y > 0):
        row = 1

    elif (y < (450 / 3) * 2 and y > 450 / 3):
        row = 2

    elif (y < 450 and y > (450 / 3) * 2):
        row = 3

    else:
        row = None

    if (row and col and Game_board[row - 1][col - 1] is None):
        # global XO
        draw_XO(row, col)
        check_win(row, col)


def check_win(row, col):
    global Game_board, winner, draw

    # Win check across rows

    if Game_board[0][0] == Game_board[0][1] == Game_board[0][2] is not None:
        winner = Game_board[0][0]
        pygame.draw.line(WIN, RED, (0, 150 / 2), (WIDTH, 150 / 2), 5)

    if Game_board[1][0] == Game_board[1][1] == Game_board[1][2] is not None:
        winner = Game_board[1][0]
        pygame.draw.line(WIN, RED, (0, (150 + 150 / 2)),
                         (WIDTH, 150 + 150 / 2), 5)

    if Game_board[2][0] == Game_board[2][1] == Game_board[2][2] is not None:
        winner = Game_board[2][0]
        pygame.draw.line(WIN, RED, (0, 300 + 150 / 2), (WIDTH, 300 + 150 / 2), 5)

    # Win check across columns

    if Game_board[0][0] == Game_board[1][0] == Game_board[2][0] is not None:
        winner = Game_board[0][0]
        pygame.draw.line(WIN, RED, (150 / 2, 0), (150 / 2, 450), 5)

    if Game_board[0][1] == Game_board[1][1] == Game_board[2][1] is not None:
        winner = Game_board[0][1]
        pygame.draw.line(WIN, RED, ((150 + 150 / 2), 0), (150 + 150 / 2, 450), 5)

    if Game_board[0][2] == Game_board[1][2] == Game_board[2][2] is not None:
        winner = Game_board[0][2]
        pygame.draw.line(WIN, RED, (300 + 150 / 2, 0), (300 + 150 / 2, 450), 5)

    # Win check across diagonals

    if Game_board[0][0] == Game_board[1][1] == Game_board[2][2] is not None:
        winner = Game_board[0][0]
        pygame.draw.line(WIN, RED, (0, 0), (WIDTH, 450), 5)

    if Game_board[0][2] == Game_board[1][1] == Game_board[2][0] is not None:
        winner = Game_board[0][2]
        pygame.draw.line(WIN, RED, (WIDTH, 0), (0, 450), 5)

    if all([all(row) for row in Game_board]) and winner is None:
        draw = True
    draw_status()


def reset_game():
    global Game_board, winner, XO, draw
    time.sleep(1.3)
    WIN.fill(WHITE)
    XO = 'x'
    draw = False
    winner = None
    Game_board = [[None] * 3, [None] * 3, [None] * 3]
    draw_window()


def main():
    clock = pygame.time.Clock()
    run = True
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                user_click()

            if winner or draw:
                reset_game()

    pygame.quit()


if __name__ == "__main__":
    main()
