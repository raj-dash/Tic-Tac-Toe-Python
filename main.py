import pygame,sys
import numpy as np

#functions
def draw_lines(l_colour):
    pygame.draw.line(win, l_colour, (width/3, 0), (width/3, width), 10)
    pygame.draw.line(win, l_colour, ((width/3)*2, 0), ((width/3)*2, width), 10)
    pygame.draw.line(win, l_colour, (0, width/3), (width, width/3), 10)
    pygame.draw.line(win, l_colour, (0, (width/3)*2), (width, (width/3)*2), 10)

def mark_square(grid, row,col,player):
    grid[col][row] = player

def avail_square(grid, row,col):
    return grid[col][row] == 0

def check_draw(grid, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if grid[col][row] == 0:
                return False

    return True

def get_clicked_pos(pos, rows, width):
    gap = width//rows
    y,x = pos
    row = y//gap
    col = x//gap
    return row,col

def draw_figures(grid, rows, cols,):
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                pygame.draw.circle(win, white,  (int(col*width/3 + circle_space), int(row*width/3 + circle_space)), c_radius, c_width)
            elif grid[row][col] == 2:
                pygame.draw.line(win, black, (int(col*width/3 + line_space), int(row*width/3 + width/3-line_space)), (int(col*width/3+width/3-line_space), int(row*width/3+line_space)), line_width)
                pygame.draw.line(win, black, (int(col * width / 3 + line_space), int(row * width / 3 + line_space)),(int(col * width/3 + width / 3 - line_space), int(row * width / 3 + width / 3 - line_space)), line_width)

def check_win(grid,mark):
    return ((grid[0][0] == mark and grid[0][1] == mark and grid[0][2] == mark) or
    (grid[1][0] == mark and grid[1][1] == mark and grid[1][2] == mark) or
    (grid[2][0] == mark and grid[2][1] == mark and grid[2][2] == mark) or
    (grid[0][0] == mark and grid[1][1] == mark and grid[2][2] == mark) or
    (grid[2][0] == mark and grid[1][1] == mark and grid[0][2] == mark) or
    (grid[0][0] == mark and grid[1][0] == mark and grid[2][0] == mark) or
    (grid[0][1] == mark and grid[1][1] == mark and grid[2][1] == mark) or
    (grid[0][2] == mark and grid[1][2] == mark and grid[2][2] == mark))

def draw_win(grid,mark):
    if mark == 1:
        color = white
    elif mark == 2:
        color = black
    else:
        color = red
    if grid[0][0] == mark and grid[0][1] == mark and grid[0][2] == mark:
        pygame.draw.line(win, color, (width//30, width//6), (width - (width//30), width//6), line_width)
    elif grid[1][0] == mark and grid[1][1] == mark and grid[1][2] == mark:
        pygame.draw.line(win, color, (width // 30, width // 2), (width - (width//30), width//2), line_width)
    elif grid[2][0] == mark and grid[2][1] == mark and grid[2][2] == mark:
        pygame.draw.line(win, color, (width // 30, (width // 2) + (width//3)), (width - (width // 30), (width // 2) + (width//3)), line_width)
    elif grid[0][0] == mark and grid[1][1] == mark and grid[2][2] == mark:
        pygame.draw.line(win, color, (width//20, width//20), (width - (width//20), width - (width//20)), line_width)
    elif grid[2][0] == mark and grid[1][1] == mark and grid[0][2] == mark:
        pygame.draw.line(win, color, (width//20, width - (width//20)), (width - (width//20), width//20), line_width)
    elif grid[0][0] == mark and grid[1][0] == mark and grid[2][0] == mark:
        pygame.draw.line(win, color, (width//6, width//30), (width//6, width - (width//30)), line_width)
    elif grid[0][1] == mark and grid[1][1] == mark and grid[2][1] == mark:
        pygame.draw.line(win, color, (width // 2, width // 30), (width // 2, width - (width // 30)), line_width)
    elif grid[0][2] == mark and grid[1][2] == mark and grid[2][2] == mark:
        pygame.draw.line(win, color, ((width//2) + (width//3), width//30), ((width//2) + (width//3), width - (width//30)), line_width)

def draw_score():
    global score_font
    score_draw = score_font.render('o:{} x:{} draw:{}'.format(score['pl_1'], score['pl_2'], score['draw']), True,text_colour)
    score_text_rect = text_draw.get_rect()
    score_text_rect.x = width - (width//5)
    score_text_rect.y = width - (width // 40)
    win.blit(score_draw, score_text_rect)

def reset(grid):
    global game_over, player, draw
    win.fill(green)
    draw_lines(line_colour)
    draw_score()
    game_over = False
    draw = False
    player = 1
    for row in range(rows):
        for col in range(cols):
            grid[row][col] = 0

def quit():
    print(score)
    pygame.quit()
    sys.exit()

#initialising
pygame.init()

#colours
red = (255,0,0)
green = (28,170,156)
black = (0,0,0)
white = (255,255,255)
text_colour = (18, 75, 219)
line_colour = (23,145,135)

#screen
width = 600
win = pygame.display.set_mode((width,width))
pygame.display.set_caption('Tic Tac Toe')
win.fill(green)
draw_lines(line_colour)

#variables
rows = cols = 3
player = 1
c_radius = width//10
c_width = width//40
circle_space = width//6
line_space = width//13
line_width = width//30
game_over = False
score = {'pl_1':0,'pl_2':0,'draw':0}
font = pygame.font.Font('KGHAPPYSolid.ttf', 100)
score_font = pygame.font.Font('KGHAPPYSolid.ttf', 10)
draw = False
FPS = 60

#text
text_draw = font.render('DRAW', True, text_colour)
text_rect = text_draw.get_rect()
text_rect.center = (width//2, width//2)
draw_score()

#board
board = np.zeros((rows,cols))

#clock
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x,y = get_clicked_pos(pos, rows, width)
            if not game_over:
                if avail_square(board, x, y):
                    if player == 1:
                        mark_square(board, x, y, player)
                        if check_win(board,player):
                            score['pl_1'] += 1
                            draw_win(board, player)
                            game_over = True
                        elif check_draw(board, rows, cols):
                            score['draw'] += 1
                            draw = True
                            game_over = True
                        player = 2
                    elif player == 2:
                        mark_square(board, x, y, player)
                        if check_win(board,player):
                            score['pl_2'] += 1
                            draw_win(board, player)
                            game_over = True
                        elif check_draw(board, rows, cols):
                            score['draw'] += 1
                            draw = True
                            game_over = True
                        player = 1
                    draw_figures(board, rows, cols)
                    if draw:
                        win.blit(text_draw, text_rect)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reset(board)
            elif event.key == pygame.K_ESCAPE:
                quit()

    #end stuff
    pygame.display.update()
    clock.tick(FPS)