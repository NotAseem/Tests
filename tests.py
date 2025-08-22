class single_method123:
    def greeting(self, name):
        print(f"greeting called with name={name}")
        print(f"greeting called with name={name}")
        print(f"greeting called with name={name}")
        print(f"greeting called with name={name}")
        print(f"greeting called with name={name}")
        print(f"greeting called with name={name}")
        print(f"greeting called with name={name}")
        print(f"greeting called with name={name}")
        return f"Hello, {name}!"


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


def demo():
    """Small demo that exercises the above utilities."""
    print("demo called")
    r = Rectangle(3, 4)
    square = Rectangle.from_side(5)
    return {
        "rect_area": r.area(),
        "rect_perimeter": r.perimeter(),
        "is_square_3x4": Rectangle.is_square(3, 4),
        "square_area": square.area(),
    }