# Import a library of functions called 'pygame'
from ast import For
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

tentacles = []
number_of_tentacles = 1
wiggle_range = 1
number_of_segments = 100
tentancle_length = 500
for tentaclee in range(number_of_tentacles):
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tentacles.append(tentacle.tentacle(number_of_segments,tentacle_length=tentancle_length,width_range=[10,40],color=color))

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # Clear the screen and set the screen background
    screen.fill(BLACK)
    #update angle of segments
    for tentaclee in tentacles:
        # tentaclee.update_angle(range_of_angle=1)
        # tentaclee.wiggle(wiggle_range)
        tentaclee.follow(list(pygame.mouse.get_pos()))
    # Draw the screen elements
    for tentaclee in tentacles:

        tentaclee.draw(screen)
        
    #update screen
    pygame.display.flip()
    
# Be IDLE friendly
pygame.quit()