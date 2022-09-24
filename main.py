import pygame, sys

# functions

def draw_lines(l_colour):
    pygame.draw.line(win, l_colour, (width / 3, 0), (width / 3, width), 10)
    pygame.draw.line(win, l_colour, ((width / 3) * 2, 0), ((width / 3) * 2, width), 10)
    pygame.draw.line(win, l_colour, (0, width / 3), (width, width / 3), 10)
    pygame.draw.line(win, l_colour, (0, (width / 3) * 2), (width, (width / 3) * 2), 10)


def get_clicked_pos(pos, rows, width):
    gap = width//rows
    y, x = pos
    row = y//gap
    col = x//gap
    return row, col


def quit():
    pygame.quit()
    sys.exit()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = get_clicked_pos(pos, rows, width)
                if not game_over:
                    pass

        # drawing
        pygame.display.update()
        clock.tick(FPS)

# initialising pygame
pygame.init()

# variables

rows = cols = 3
game_over = False
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
draw_lines(line_colour)

if __name__ == "__main__":
    main()