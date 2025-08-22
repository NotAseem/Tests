def summarize_numbers(values):
    """Return a tuple of (count, total, average) for an iterable of numbers."""
    values = list(values)
    count = len(values)
    total = sum(values) if values else 0
    average = (total / count) if count else 0
    return count, total, average


class SingleMethodExample:
    """A simple class demonstrating a single instance method."""

    def greeting(self, name):
        return f"Hello, {name}!"


class Rectangle:
    """A class with multiple methods and different method types."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    @staticmethod
    def is_square(width, height):
        return width == height

    @classmethod
    def from_side(cls, side_length):
        return cls(side_length, side_length)


def demo():
    """Small demo that exercises the above utilities."""
    r = Rectangle(3, 4)
    square = Rectangle.from_side(5)
    greet = SingleMethodExample().greeting("Tester")
    return {
        "rect_area": r.area(),
        "rect_perimeter": r.perimeter(),
        "is_square_3x4": Rectangle.is_square(3, 4),
        "square_area": square.area(),
        "greeting": greet,
        "summary": summarize_numbers([1, 2, 3, 4]),
    }