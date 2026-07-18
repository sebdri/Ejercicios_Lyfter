# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.


class Circle: 
    radius= 5 

    def get_area(self):
        area =  3.1416 *self.radius*self.radius     
        return area


circle = Circle()
print(circle.get_area())