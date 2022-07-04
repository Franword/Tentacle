from math import sin, cos, radians,atan2
from random import randint
import pygame

class Segment:
    
    def __init__(self, angle, length, parent=None,number_of_segments=None,width=1):
        self.direction_of_movement = randint(0,1)
        self.movement_counter = 0
        self.length = length
        self.parent = parent
        self.number_of_segments = number_of_segments
        if self.parent == None:
            self.start = [500,500]
            self.angle = angle
            self.id = 1
        else:
            self.parent.set_child(self)
            self.start = self.parent.get_end()
            self.id = self.parent.get_id() + 1  
            self.angle = angle + self.parent.get_angle()
            
        if self.number_of_segments != None:
                self.width = number_of_segments-self.id
        else:
            self.width = 1
                
        self.end = [self.start[0]+self.length*sin(radians(self.angle)),self.start[1]+self.length*cos(radians(self.angle))]
        self.width = max(width,1)
    def get_end(self):
        return self.end
    
    def get_start(self):
        return self.start
    
    def get_angle(self):
        return self.angle
    
    def get_id(self):
        return self.id
    def get_length(self):
        return self.length
    def set_child(self,child):
        self.child = child
        
    def draw(self, screen,color=(255,255,255)):
        if self.parent == None:
           pygame.draw.circle(screen, color, self.start, self.width/2)
        pygame.draw.circle(screen, color, self.end, self.width/2)
        pygame.draw.line(screen, color, self.start, self.end, self.width)
        
    def set_direction_of_movement(self,direction_of_movement):
        self.direction_of_movement=direction_of_movement
        self.movement_counter = 0
        
    def get_direction_of_movement(self):
        return self.direction_of_movement
    
    def update_angle(self,angle):
        self.movement_counter += 1
        if self.movement_counter > self.id: #tu zamiast id moze cos innego
            self.direction_of_movement = randint(0,1)
            self.movement_counter = 0
            
        if self.parent != None:
            start = self.parent.get_end()
        else:
            start = self.start
            
        self.start = start
        self.angle = angle
        self.end = [self.start[0]+self.length*sin(radians(self.angle)),self.start[1]+self.length*cos(radians(self.angle))]
        
    def follow(self,point=None):
        if point == None:
            point = self.child.get_start()
        dir = [point[0] - self.start[0],point[1] - self.start[1]]
        angle = atan2(dir[0],dir[1])
        self.end = point
        self.start = [point[0] - self.length*sin(angle),point[1] - self.length*cos(angle)]
        
    def info(self):
        print(f'angle = {self.angle}')
        print(f'start = {self.start}')
        print(f'end = {self.end}')
        print(f'len = {self.length}')
        try:
            print(f'parent = {self.parent}')
            print(f'child = {self.child}')
        except:
            pass