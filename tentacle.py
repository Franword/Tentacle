import segment
import random
import math


class tentacle:
    def __init__(self,number_of_segments,tentacle_length,width_range=[1,30],color=(255,255,255)):
        self.color = color
        width_range[0] = max(width_range[0],1)
        width_range[1] = max(width_range[1],1)
        self.width_shrink = (width_range[1]-width_range[0])/number_of_segments
        self.number_of_segments = number_of_segments
        self.tentacle_length = tentacle_length
        self.angle_of_segments = int(360/number_of_segments)
        self.length_of_Segments = (tentacle_length/number_of_segments)
        self.Seg_list = []
        width = width_range[1]
        self.Seg_list.append(segment.Segment(random.randint(0,360),self.length_of_Segments,number_of_segments=number_of_segments,width=width))
        for ind,Seg in enumerate(range(1,number_of_segments)):
            width = int(width_range[1] - self.width_shrink*ind)
            self.Seg_list.append(segment.Segment(random.randint(-self.angle_of_segments,self.angle_of_segments),self.length_of_Segments,self.Seg_list[Seg-1],number_of_segments=number_of_segments,width=width))
            
    def draw(self,screen):
        for Seg in self.Seg_list:
            Seg.draw(screen,self.color)
            
    def update_angle(self,range_of_angle):
        for Seg in self.Seg_list:
            Seg.update_angle(Seg.get_angle()+random.randint(-range_of_angle,range_of_angle))
            
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
            
            
                   
    # def inverse_kinematics3(self,target_point):
    #     cosq2=math.radians((target_point[0]**2+target_point[1]**2-self.Seg_list[0].get_length()**2-self.Seg_list[1].get_length()**2)/(2*self.Seg_list[0].get_length()*self.Seg_list[1].get_length()))
    #     print(cosq2)
    #     sinq2=math.sqrt(1-cosq2**2) #+-
    #     q2 = math.atan2(sinq2,cosq2)
    #     k1 = self.Seg_list[0].get_length() + self.Seg_list[1].get_length()*cosq2
    #     k2 =  self.Seg_list[1].get_length()*sinq2
    #     q1 = math.atan2(target_point[0],target_point[1])-math.atan2(k2,k1)

    #     self.Seg_list[0].update_angle(q1)
    #     self.Seg_list[1].update_angle(q2)