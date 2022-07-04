# Import a library of functions called 'pygame'
import pygame
from math import pi
import segment
import random
import tentacle

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [1000,1000]
screen = pygame.display.set_mode(size)
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

seg = segment.Segment(0,100)
seg2 = segment.Segment(0,100,seg)
while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # Clear the screen and set the screen background
    screen.fill(BLACK)
    #update angle of segments
    seg2.follow(list(pygame.mouse.get_pos()))
    seg.follow()
    seg2.draw(screen)
    seg.draw(screen)
    #update screen
    pygame.display.flip()
    
# Be IDLE friendly
pygame.quit()