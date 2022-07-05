import segment
import random

class tentacle:
    def __init__(self,number_of_segments,tentacle_length,width_range=[1,30],color=(255,255,255)):
        self.number_of_segments = number_of_segments
        self.color = color
        #width
        width_range[0] = max(width_range[0],1)
        width_range[1] = max(width_range[1],1)
        width_shrink = (width_range[1]-width_range[0])/number_of_segments
        #length
        self.tentacle_length = tentacle_length
        segment_length = (tentacle_length/number_of_segments)
        #init angle
        init_angle_range = int(360/number_of_segments)
        #init segments
        self.segments = []
        self.segments.append(segment.Segment(0,angle=random.randint(init_angle_range,init_angle_range),length=segment_length,start=[500,500],width=width_range[0]))
        for id in range(1,self.number_of_segments):
            self.segments.append(segment.Segment(id,angle=random.randint(init_angle_range,init_angle_range),length=segment_length,start=self.segments[id-1].end,width=int(width_range[0]+id*width_shrink)))
            
    def draw(self,screen):
        for Seg in self.segments:
            Seg.draw(screen,self.color)

    def follow(self,point):
        for id, segment in enumerate(self.segments):
            if id == 0:
                segment.follow(point)
            else:
                segment.follow(self.segments[id-1].start)

    def pin_root(self,fixed_point):
        actual_root = self.segments[0].start
        vector = [actual_root[0]-fixed_point[0],actual_root[1]-fixed_point[1]]
        for segment in self.segments:
            segment.move_segment(vector)
    # def update_angle(self,range_of_angle):
    #     for Seg in self.Seg_list:
    #         Seg.update_angle(Seg.get_angle()+random.randint(-range_of_angle,range_of_angle))
            
    # def wiggle(self,range_of_angle):
    #     for Seg in self.Seg_list:
    #         if Seg.get_direction_of_movement():
    #             if Seg.get_id() == 0:
    #                 pass
    #                 # Seg.update_angle(Seg.get_angle()+random.randint(0,range_of_angle))
    #             else:
    #                 Seg.update_angle(self.Seg_list[Seg.get_id()-1].get_angle()+random.randint(0,range_of_angle))
    #         else:
    #             if Seg.get_id() == 0:
    #                 pass
    #                 # Seg.update_angle(Seg.get_angle()+random.randint(-range_of_angle,0))
    #             else:
    #                 Seg.update_angle(self.Seg_list[Seg.get_id()-1].get_angle()+random.randint(-range_of_angle,0))
                    
