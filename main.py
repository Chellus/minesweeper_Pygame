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

# create window and clock
window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock() # pygame clock

# load bomb, numbers and flag images
numbersImg = []

for i in range(9):
    numbersImg.append(pygame.image.load('resources/n' + str(i) + '.png'))

bombImg = pygame.image.load('resources/bomb.png')
flagImg = pygame.image.load('resources/flag.png')

# colors
white = (255, 255, 255)
black = (0, 0, 0)
light_grey = (150, 150, 150)

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

    # generate the bombs, they can't be generated on the edges
    for i in range(bombs):
        aux_x = random.randint(1, 13)
        aux_y = random.randint(1, 18)

        while board[aux_y][aux_x] < 0:
            aux_x = random.randint(1, 13)
            aux_y = random.randint(1, 18)

        board[aux_y][aux_x] = -20 # the number for the board is a negative number

    # count adjacent mines to a square
    for i in range(1, board_h - 1):
        for j in range(1, board_w - 1):
            if board[i][j] < 0: # if this block is a mine
                for k in range(-1, 2):
                    for l in range(-1, 2):
                             board[i + k][j + l] += 1


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

# button function
def block_press(x, y, img=None):
    block_size = 30

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + block_size > mouse[0] > x and y + block_size > mouse[1] > y:
        if click[0] == 1:
            if img != None:
                window.blit(img, (x, y))


# in this function we draw the numbers and the bomb to the grid
def draw_board():
    block_size = 30

    for x in range((window_w // block_size) - 150 // block_size):
        for y in range((window_h // block_size)):
            if board[y][x] < 0: # if this block contains a bomb
                window.blit(bombImg, (x * block_size, y * block_size))
            else: # if it doesn't
                for i in range(1, 10):
                    if board[y][x] == i:
                        window.blit(numbersImg[i - 1], (x * block_size, y * block_size))


# main game loop
def game_loop():
    running = True
    block_size = 30

    generate_board()
    window.fill(light_grey)

    while running:
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the close button of the window is pressed, exit
                pygame.quit()
                quit()

        for x in range((window_w // block_size) - 150 // block_size):
            for y in range((window_h // block_size)):
                if board[y][x] < 0: # if this block contains a bomb
                    block_press(x * block_size, y * block_size, bombImg)
                elif board[y][x] == 0: # if there isn't a bomb adjacent to this block
                    block_press(x * block_size, y * block_size, numbersImg[0])
                else: # if there are bombs adjacent to this block
                    for i in range(1, 9):
                        if board[y][x] == i:
                            block_press(x * block_size, y * block_size, numbersImg[i])

        pygame.display.update()
        clock.tick(30) # we set the clock to 30 frames per second

if __name__ == "__main__":
    game_loop()
