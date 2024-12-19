import pygame, sys, random
from pygame.math import Vector2

class DOG:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
    
    def draw_dog(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            #create a rect
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            #draw the rec
            pygame.draw.rect(screen,(183,111,122), block_rect)
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

hotdog = HOT_DOG()
dog = DOG()

#loop for running the game
while True:
    # draw all elements and display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #ends any kind of code thats running on
    
    screen.fill((175,215,70))          
    hotdog.draw_hotdog()
    dog.draw_dog()
    pygame.display.update()
    clock.tick(60) #maximum 60 frames per second (adds consistency to the game)
