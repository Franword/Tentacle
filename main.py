# Import a library of functions called 'pygame'
import pygame
import math
import random
import tentacle


def vector_subtract(a,b):
    return [a[0]-b[0],a[1]-b[1]]
def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
def vector_sign(a):
    return [sign(a[0]),sign(a[1])]
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
roots = []
number_of_tentacles = 1
for tentaclee in range(number_of_tentacles):
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tentacle_length = random.randint(1000,1000)
    number_of_segments = 10
    width_range = [int(tentacle_length/30),int(tentacle_length/20)]
    tentacles.append(tentacle.tentacle(number_of_segments=number_of_segments,tentacle_length=tentacle_length,width_range=width_range,color=color))
    roots.append([random.randint(0,size[0]),random.randint(0,size[1])])
# field_force = [0,20]


while not done:
    clock.tick(60)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    mouse = list(pygame.mouse.get_pos())

    # Clear the screen and set the screen background
    screen.fill(BLACK)
    #update angle of segments
    for index,tentaclee in enumerate(tentacles):
        # tentaclee.update_angle(range_of_angle=1)
        # tentaclee.wiggle(wiggle_range)
        tentaclee.follow(mouse)
        tentaclee.pin(roots[index])
        # tentaclee.shift(field_force)
        # tentaclee.gravity(field_force)
    # Draw the screen elements
    for tentaclee in tentacles:
        if not tentaclee.is_straigth(intolerance=1):
            tentaclee.draw(screen)
    #update screen
    pygame.display.flip()
# Be IDLE friendly
pygame.quit()