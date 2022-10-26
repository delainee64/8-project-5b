# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/25/2022
# Description: Write a class named Taxicab that has three private data members:
# one that holds the current x-coordinate, one that holds the current y-coordinate,
# and one that holds the current odometer reading.

class Taxicab:
    """Represents a taxi cab's traveling distance."""

    def __init__(self, x, y):
        self.x = x              # x coordinate of the cab
        self.y = y              # y coordinate of the cab
        self.odometer = 0

    def get_x(self):
        """Returns the x coordinate of the cab."""
        return self.x

    def get_y(self):
        """Returns the y coordinate of the cab."""
        return self.y

    def get_odometer(self):
        """Returns the odometer reading of the cab."""
        return self.odometer

    def move_x(self, distance):
        """Calculates the absolute distance of how far the taxi cab travels left or right."""
        self.x += distance
        self.odometer += abs(distance)

    def move_y(self, distance):
        """Calculates the absolute distance of how far the taxi cad travels up or down."""
        self.y += distance
        self.odometer += abs(distance)


cab1 = Taxicab(5, -8)  # creates a new taxi cab with specific traveling parameters.
cab1.move_x(3)  # sets the number of units the taxi cab moves right.
cab1.move_y(-4)  # sets the number of units the taxi cab moves down.
cab1.move_x(-1)  # sets the number of units the taxi cab moves left.
# print(cab1.get_odometer())  # prints the odometer reading.
# print(cab1.get_x())  # prints the correct amount of units traveled left and right.
# print(cab1.get_y())  # prints the correct number of units traveled down.
