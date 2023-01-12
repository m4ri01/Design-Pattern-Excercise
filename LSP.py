class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def width(self):
        pass
    
    @width.setter
    def width(self,width):
        self._width = width
    
    @width.getter
    def width(self):
        return self._width

    @property
    def height(self):
        pass

    @height.setter
    def height(self,height):
        self._height = height

    @height.getter
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self,width):
        super().__init__(width,width)
    
    @Rectangle.width.setter
    def width(self,width):
        self._width = self._height = width
    
    @Rectangle.height.setter
    def height(self,height):
        self._height = self._width = height

def useIt(r):
    w = r.width
    r.height = 10
    expected = w*10 
    print("expected {}, got {}".format(expected,r.area))

s = Square(3)
useIt(s)
rc = Rectangle(2,3)
useIt(rc)