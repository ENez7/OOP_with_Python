class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height

# Square class extends (inherits) Rectangle class
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        # When init a subclass is a good practice to
        # init its super class
        
if __name__ == '__main__':
    rect = Rectangle(base=3, height=4)
    print(rect.area())
    
    square = Square(side=4)
    print(square.area())
    