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
#customization
number_of_segments = 100
tentacle_length = 1000
width_range = [5,40]
#customization caclulation
segment_length = tentacle_length/number_of_segments
width_shrink = (width_range[1]-width_range[0])/number_of_segments

Seg_list = []
Seg_list.append(segment.Segment(0,angle=0,length=segment_length,start=[500,500],width=width_range[0]))
for id,Seg in enumerate(range(1,number_of_segments)):
    Seg_list.append(segment.Segment(id,angle=0,length=segment_length,start=Seg_list[id-1].end,width=int(width_range[0]+id*width_shrink)))

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
    for id, Seg in enumerate(Seg_list):
        if id == 0:
            Seg.follow(list(pygame.mouse.get_pos()))
        else:
            Seg.follow(Seg_list[id-1].start)   
    # Draw the screen elements
    for Seg in Seg_list:
        Seg.draw(screen)
    #update screen
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()