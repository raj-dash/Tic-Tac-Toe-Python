import pygame

# initialising pygame
pygame.init()

# variables

width = 550
clock = pygame.time.Clock()
FPS = 60

# colours

red = (255,0,0)
green = (28,170,156)
black = (0,0,0)
white = (255,255,255)
text_colour = (18, 75, 219)
line_colour = (23,145,135)

# screen

win = pygame.display.set_mode((width, width))
pygame.display.set_caption("Tic Tac Toe")
win.fill(green)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    # drawing
    pygame.display.update()
    clock.tick(FPS)

if __name__ == "__main__":
    main()