import pygame, sys, random
from pygame.math import Vector2

class HOT_DOG:
    def __init__(self):
        # create an x and y position
        # draw a square in whatever this position is
        self.x = random.randint(0,cell_number - 1) #sub 1 will ensure the hotdog will always be on screen (limits to 799px)
        self.y = random.randint(0,cell_number - 1)
        self.pos = pygame.Vector2(self.x,self.y)

    def draw_hotdog(self):
        #create a rectangle
        hotdog_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size,cell_size)
        #draw the rectangle
        pygame.draw.rect(screen, (126,166,114), hotdog_rect)

pygame.init()
cell_size = 40
cell_number = 20
screen_size = (cell_number * cell_size)
screen = pygame.display.set_mode((screen_size,screen_size))
clock = pygame.time.Clock() #set maximum frames per second

fruit = HOT_DOG()

#loop for running the game
while True:
    # draw all elements and display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #ends any kind of code thats running on
    
    screen.fill((175,215,70))          
    fruit.draw_hotdog()
    pygame.display.update()
    clock.tick(60) #maximum 60 frames per second (adds consistency to the game)
