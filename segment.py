from math import sin, cos, radians,atan2
from random import randint
import pygame

class Segment:
    
    def __init__(self,id, angle, length,start,width=1):
        
        self.length = length
        self.start = start
        self.angle = angle
        self.id = id
        self.width = max(width,1)
        self.calculate_end()

    def calculate_end(self):
        self.end = [self.start[0]+self.length*sin(radians(self.angle)),self.start[1]+self.length*cos(radians(self.angle))]    
        
    def draw(self, screen,color=(255,255,255)):
        pygame.draw.circle(screen, color, self.start, self.width/2)
        # pygame.draw.circle(screen, color, self.end, self.width/2)
        pygame.draw.line(screen, color, self.start, self.end, self.width)
    def move_segment(self,vector):
        self.start[0] += vector[0]
        self.start[1] += vector[1]
        self.end[0] += vector[0]
        self.end[1] += vector[1]

    def update_angle(self,angle): 
        self.angle = angle
        self.calculate_end()
        
    def follow(self,point=None):
        dir = [point[0] - self.start[0],point[1] - self.start[1]]
        angle = atan2(dir[0],dir[1])
        self.end = point
        self.start = [point[0] - self.length*sin(angle),point[1] - self.length*cos(angle)]
