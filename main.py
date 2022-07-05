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

# Set the height and width of the screen
size = [1000,1000]
screen = pygame.display.set_mode(size)
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

tentacles = []
number_of_tentacles = 1
for tentaclee in range(number_of_tentacles):
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tentacle_length = random.randint(300,600)
    number_of_segments = tentacle_length
    width_range = [int(tentacle_length/30),int(tentacle_length/20)]
    tentacles.append(tentacle.tentacle(number_of_segments,tentacle_length=tentacle_length,width_range=width_range,color=color))

while not done:
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
        tentaclee.pin_root([500,500])
    # Draw the screen elements
    for tentaclee in tentacles:
        tentaclee.draw(screen)
    #update screen
    pygame.display.flip()
# Be IDLE friendly
pygame.quit()