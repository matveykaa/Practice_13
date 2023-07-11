class Rectangle:
    def __init__(self, width: str, height: str):
        self.width = int(width)
        self.height = int(height)

    @property
    def get_perimeter(self):
        return (self.width + self.height) * 2

    @property
    def get_area(self):
        return self.width * self.height

def rectangle_calc(input_info):
    width, height = input_info.split()
    rect = Rectangle(width, height)
    print("Perimeter = ", rect.get_perimeter, " and area = ", rect.get_area)

if __name__ == "__main__":
    input_info = input("Enter width and height for rectangle - ")
    rectangle_calc(input_info)