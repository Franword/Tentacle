# Import a library of functions called 'pygame'
import pygame
import math
import random
import sys

from sympy import rad
import tentacle

def random_point_on_circle(center,radius):
    # random angle
    angle = 2 * math.pi * random.random()
    # random radius
    r = radius * math.sqrt(random.random())
    # calculating coordinates
    return [r * math.cos(angle) + center[0],r * math.sin(angle) + center[1]]

def points_on_circle(radius,number_of_points):
    return [(math.cos(2*math.pi/number_of_points*x)*radius,math.sin(2*math.pi/number_of_points*x)*radius) for x in range(0,number_of_points+1)]

def vector_subtract(a,b):
    return [a[0]-b[0],a[1]-b[1]]

def vector_add(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
def vector_sign(a):
    return [sign(a[0]),sign(a[1])]

def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
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
number_of_tentacles = 10
radius = 50
tentacle_length = 300
for tentaclee in range(number_of_tentacles):
    color = random_color()
    number_of_segments = 5
    width_range = [int(tentacle_length/100),int(tentacle_length/30)]
    tentacles.append(tentacle.tentacle(number_of_segments=number_of_segments,tentacle_length=tentacle_length,width_range=width_range,color=color))
    # roots.append(random_point_on_circle([0,0],radius))
roots = points_on_circle(radius,number_of_tentacles)
body_color = random_color()
# field_force = [0,20]
player = [size[0]/2,size[1]/2]
velocity = 5
while not done:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player[1] -= velocity
    if keys[pygame.K_DOWN]:
        player[1] += velocity
    if keys[pygame.K_RIGHT]:
        player[0] += velocity
    if keys[pygame.K_LEFT]:
        player[0] -= velocity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False

    mouse = list(pygame.mouse.get_pos())

    # Clear the screen and set the screen background
    screen.fill(BLACK)
    #update angle of segments
    for index,tentaclee in enumerate(tentacles):
        # tentaclee.update_angle(range_of_angle=1)
        # tentaclee.wiggle(wiggle_range)
        tentaclee.follow(mouse)
        # tentaclee.follow(vector_add([random.randint(-100,100),random.randint(-100,100)],player))
        tentaclee.pin(vector_add(roots[index],player))
        # tentaclee.shift(field_force)
        # tentaclee.gravity(field_force)
    # Draw the screen elements
    pygame.draw.circle(screen, body_color, player, radius,width=tentacles[0].segments[-1].width)
    for tentaclee in tentacles:
        # if not tentaclee.is_straigth(intolerance=1):
            tentaclee.draw(screen)
    #update screen
    pygame.display.flip()
# Be IDLE friendly
pygame.quit()