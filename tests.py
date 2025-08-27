class single_method:
    print(f"greeting called with name=")
    print(f"greeting called with name=")
    def func31():
        print("HII123!45")
    def func378():
        print("HII123!45")
    def func32():
        print("HII123!45")
        def func33():
            print("HII123!45")
            def func34():
                print("HII123!45")
    class second:
        def funccc():
            print("Hello")
            def func32():
                print("HII123!45")
            def funccc2():
                print("HII123!45")
       

class Rectangle:
    """A class with multiple methods and different method types."""

    def __init__(self, width, height):
        print(f"Rectangle.__init__ called with width={width}, height={height}")
        self.width = width
        self.height = height

    def area(self):
        print(f"Rectangle.area called on width={self.width}, height={self.height}")
        return self.width * self.height

    def perimeter(self):
        print(f"Rectangle.perimeter called on width={self.width}, height={self.height}")
        return 2 * (self.width + self.height)

    @staticmethod
    def is_square(width, height):
        print(f"Rectangle.is_square called with width={width}, height={height}")
        return width == height

    @classmethod
    def from_side(cls, side_length):
        print(f"Rectangle.from_side called with side_length={side_length}")
        return cls(side_length, side_length)
def demo2():
    print("demo2 called")
    print("demo2 called")
    def demo3():
        print("demo3 called")
        print("demo3 called")
    demo3()

def demo():
    """Small demo that exercises the above utilities."""
    print("demo called")
    print("demo called")
    def demo2():
        print("demo2 called")
        print("demo2 called")   
    r = Rectangle(3, 4)
    square = Rectangle.from_side(5)
    return {
        "rect_area": r.area(),
        "rect_perimeter": r.perimeter(),
        "is_square_3x4": Rectangle.is_square(3, 4),
        "square_area": square.area(),
    }