import segment
import random

class tentacle:
    def __init__(self,root=[0,0],number_of_segments=3,tentacle_length=300,width_range=[1,30],color=(255,255,255)):
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
        self.segments.append(segment.Segment(0,angle=random.randint(init_angle_range,init_angle_range),length=segment_length,start=root,width=width_range[0]))
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

    def shift(self,vector):
        #where tentacle is unpinned
        for segment in self.segments:
            segment.move_segment(vector)
    def gravity(self,vector):
        #works if tentacle is pinned
        for i in range(2,len(self.segments)+1):
            self.segments[-i].move_segment(vector)

    def pin(self,point):
        self.segments[-1].set_start(point)
        for i in range(2,len(self.segments)+1):
            self.segments[-i].set_start(self.segments[-i+1].end)

    def is_straigth(self,intolerance):
        for previous, current in zip(self.segments, self.segments[1:]):
            if abs(previous.angle - current.angle) > intolerance:
                return False
        return True
        # if all(print(seg.angle) == 0 for seg in self.segments[1:]):
        #     return True
        # else:
        #     return False

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
                    
