import pygame

pygame.init()

window_w = 600
window_h = 600

window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
light_grey = (180, 180, 180)

def draw_grid():
    block_size = 30
    for x in range((window_w // block_size) - 150 // block_size):
        for y in range((window_h // block_size)):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(window, black, rect, 1)

def game_loop():
    running = True

    window.fill(light_grey)
    while running:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

if __name__ == "__main__":
    game_loop()
