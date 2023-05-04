#2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

my_circle = Circle(float(input("Введіть радіус кола:")))
circle_area = my_circle.area()
print(f"Площа кола = {circle_area}")
