class Rectangle:
    def __init__(self, width, height):
        if any(not isinstance(arg, (int, float)) for arg in [width, height]):
            raise TypeError("Argument must be of type 'int' or 'float'")
        
        self.width = width
        self.height = height
        
    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return 'Too big for picture.'
        
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, other):
        if not isinstance(other, (Rectangle, Square)):
            raise TypeError('Argument must be a rectangle or square object')
        
        if self.width < other.width or self.height < other.height:
            return 0
        
        amount_inside = self.get_area() // other.get_area()
        return amount_inside
    
        
        
        



class Square:
    pass


rect = Rectangle(10,5)
rect1 = Rectangle(10,5)
print(rect)
print(rect.get_picture())
print(rect.get_amount_inside(rect1))