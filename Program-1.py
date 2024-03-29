class Circle:
    # Creating a class named Circle
    def __init__(self,radius):
        self.radius = radius
        # Initialize radius attribute with the provided value
        self.__pi = 3.141
        # Private Variable pi

    def area(self):
        # Created method to calculate area of the Circle
        return self.__pi * self.radius ** 2
    # Calculate and return the area of the circle
    
    def perimeter(self):
        # Created method to calculate perimeter of the Circle
        return 2 * self.__pi * self.radius
    # Calculate and return the perimeter of the circle
    
radius_values = [10, 501, 22, 37, 100, 999, 87, 351]
# List of radii for circles

circle_objects = [Circle(radius) for radius in radius_values]
# Create Circle objects for each radius in the list


area_values = [circle.area() for circle in circle_objects]
perimeter_values = [circle.perimeter() for circle in circle_objects]
# Calculate areas and perimeters for each circle

print("The Area value for each radius value are:", area_values)
print("The Perimeter value for each radius value are:", perimeter_values)

