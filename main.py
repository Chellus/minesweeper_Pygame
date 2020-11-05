import pygame
import random

pygame.init()

# window constants
window_w = 600
window_h = 600

# board constants
board_w = 15
board_h = 20
bombs = 40

window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock() # pygame clock

# colors
white = (255, 255, 255)
black = (0, 0, 0)
light_grey = (180, 180, 180)

# our board
board = []

# in this function we generate the board with random bombs placed in it
def generate_board():
    global board
    global bombs

    bomb_counter = 0

    # fill the board with 0's
    for i in range(board_h):
        row = []
        for j in range(board_w):
            row.append(0)
        board.append(row)

    # generate the bombs
    for i in range(1, bombs):
        aux_x = random.randint(0, 14)
        aux_y = random.randint(0, 19)

        while board[aux_y][aux_x] < 0:
            aux_x = random.randint(0, 14)
            aux_y = random.randint(0, 19)

        board[aux_y][aux_x] = -20 # the number for the board is a negative number

    # count adjacent mines to a square
    for i in range(board_h):
        for j in range(board_w):
            if board[i][j] >= 0: # if this block isn't a mine
                 for k in range(-1, 1):
                     for l in range(-1, 1):
                         if board[i + k][j + l] < 0:
                             board[i][j] += 1

    # print the board to the terminal
    for i in range(board_h):
        for j in range(board_w):
            print(str(board[i][j]), end = ' ')
        print('')

# in this function we draw the grid to the window
def draw_grid():
    block_size = 30
    for x in range((window_w // block_size) - 150 // block_size):
        for y in range((window_h // block_size)):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(window, black, rect, 1)

# main game loop
def game_loop():
    running = True

    generate_board()

    window.fill(light_grey)

    while running:
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the close button of the window is pressed, exit
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(30) # we set the clock to 30 frames per second

if __name__ == "__main__":
    game_loop()
