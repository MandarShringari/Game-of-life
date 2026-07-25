import pygame
from pygame.locals import *
import sys 


window_width = 1000
window_length = 1000
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
live_pos = []
is_running = False


def pygame_intilization():
    global SCREEN, CLOCK, click_pos, is_running, live_pos
    pygame.init()
    SCREEN = pygame.display.set_mode((window_length, window_width))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    pygame.display.set_caption('Game of life')
    global white_tup
    white_tup = None
    
    while True:
        create_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                user_input()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_running = not is_running

                elif event.key == pygame.K_DELETE:
                    is_running = False
                    live_pos.clear()
        
       
        if is_running:
            live_pos = step_generation()
            pygame.time.delay(200)
        
        draw_the_blocks()
        pygame.display.update()
        CLOCK.tick(60)
 
                                       
                
        pygame.display.update()
  
    
def create_grid():
    blockSize = 20
    for x in range(0, window_width, blockSize):
        for y in range(0, window_length, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def user_input():
    global white_tup, x_box, y_box
    a = click_pos[0] // 20
    b = click_pos[1] // 20
    x_box = a*20
    y_box = b*20
    white_tup = (x_box,y_box)
    rect_1 = pygame.Rect(x_box, y_box, 20, 20)
        


def step_generation():
    alive_pos = []
    for i in range(0, window_width, 20):
        for j in range(0, window_length, 20):
            live_neighbors = 0
            for dx in [-20, 0, 20]:
                for dy in [-20, 0, 20]:
                    if dx == 0 and dy == 0:
                        continue  
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < window_width and 0 <= ny < window_length:
                        temp_tup = (nx, ny)
                        if temp_tup in live_pos:
                            live_neighbors += 1    
            cell = (i, j)
            is_alive = cell in live_pos 
            if is_alive and live_neighbors in (2,3):
                alive_pos.append(cell)
            elif not is_alive and live_neighbors == 3:
                alive_pos.append(cell)

    return alive_pos


def draw_the_blocks():
    SCREEN.fill(BLACK)
    create_grid()

    global white_tup
    if not is_running and white_tup is not None:
        if white_tup in live_pos:
            live_pos.remove(white_tup)
        else:
            live_pos.append(white_tup)
        white_tup = None

    for cell in live_pos:
        pygame.draw.rect(SCREEN, WHITE, pygame.Rect(cell[0], cell[1], 20, 20))
  
pygame_intilization()