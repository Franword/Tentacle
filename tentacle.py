import segment
import random
import math


class tentacle:
    def __init__(self,number_of_segments,tentacle_length,width_range=[1,30],color=(255,255,255)):
        self.number_of_segments = number_of_segments
        self.color = color
        #width
        width_range[0] = max(width_range[0],1)
        width_range[1] = max(width_range[1],1)
        self.width_shrink = (width_range[1]-width_range[0])/number_of_segments
        #length
        self.tentacle_length = tentacle_length
        self.length_of_Segments = (tentacle_length/number_of_segments)
        #init angle
        self.init_angle_range = int(360/number_of_segments)
        #init segments
        self.Seg_list = []
        width = width_range[1]
        self.Seg_list.append(segment.Segment(random.randint(0,360),self.length_of_Segments,number_of_segments=number_of_segments,width=width))
        for ind,Seg in enumerate(range(1,number_of_segments)):
            width = int(width_range[1] - self.width_shrink*ind)
            self.Seg_list.append(segment.Segment(random.randint(-self.init_angle_range,self.init_angle_range),
                self.length_of_Segments,number_of_segments=number_of_segments,width=width))
            
    def draw(self,screen):
        for Seg in self.Seg_list:
            Seg.draw(screen,self.color)
            
    # def update_angle(self,range_of_angle):
    #     for Seg in self.Seg_list:
    #         Seg.update_angle(Seg.get_angle()+random.randint(-range_of_angle,range_of_angle))
            
    def wiggle(self,range_of_angle):
        for Seg in self.Seg_list:
            if Seg.get_direction_of_movement():
                if Seg.get_id() == 0:
                    pass
                    # Seg.update_angle(Seg.get_angle()+random.randint(0,range_of_angle))
                else:
                    Seg.update_angle(self.Seg_list[Seg.get_id()-1].get_angle()+random.randint(0,range_of_angle))
            else:
                if Seg.get_id() == 0:
                    pass
                    # Seg.update_angle(Seg.get_angle()+random.randint(-range_of_angle,0))
                else:
                    Seg.update_angle(self.Seg_list[Seg.get_id()-1].get_angle()+random.randint(-range_of_angle,0))
                    
    def follow(self,point):
        temp = 0
        for Seg in reversed(self.Seg_list):
            if temp == 0:
                temp = 1
                Seg.follow(point)
            else:
                Seg.follow()