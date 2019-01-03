import math 

class Cylinder(object):
    pi = math.pi
    
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        area_base = Cylinder.pi * self.radius * self.radius
        volume = area_base * self.height
        return f'Volume of cylinder with height = {self.height} and radius = {self.radius} is equal to {round(volume,2)} cubic units.'

    def surface_area(self):
        area_base = Cylinder.pi * self.radius * self.radius
        area_side = 2*Cylinder.pi*self.radius*self.height
        surface_area = 2* area_base + area_side
        return f'Surface area of cylinder with height = {self.height} and radius = {self.radius} is equal to {round(surface_area,2)} square units.'


class Line(object):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        distance = math.sqrt((math.pow(self.coor2[1]- self.coor1[1],2)+(math.pow(self.coor2[0]- self.coor1[0],2))))
        return f'Distance between two coordinates {self.coor1} and {self.coor2} is equal to {round(distance,2)}.'
        
    def slope(self):
        slope = (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
        return f'Slope of the line is equal to {round(slope,2)}.'


my_line = Line((3,2),(8,10))

#print(my_line.coor1)
print(my_line.slope())

    

#my_cylinder = Cylinder(2,3)

#print(my_cylinder.volume())
#print(my_cylinder.surface_area())
