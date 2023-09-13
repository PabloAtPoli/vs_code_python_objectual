"""
Composition is a way to combine simple objects or data types into more complex ones.

"""
class Point:
    """ Point class represents and manipulates x,y coords. """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        """ Return the norm (length) of the vector from the origin to the point.)"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
class Segment:
    """ Segment class represents and manipulates a line segment. """
    def __init__(self, x1, y1, x, y):
        self.x1 = x1
        self.y1 = y1

        # shift the point to the origin
        self.x = x - x1
        self.y = y - y1

        # create a point object. This is the use of composition
        self.point = Point(self.x, self.y)
        return

    # Calculate the length of the line segment using the norm method of the Point class
    def length_Segment(self):
        return self.point.norm()
    
# Create a segment object
segment = Segment(3, 4, 5, 6)

# Calculate the length of the line segment
print(f"The length of the line segment invoking length_segment method of class Segment is {segment.length_Segment()}")  

# Calculate the length of the line segment using the norm method of the Point class
print(f"The length of the line segment invoking norm method of class Point is {segment.point.norm()}")

# Test the above code using numpy
import numpy as np
p1 = np.array([3, 4])
p2 = np.array([5, 6])
print(f"The length of the line segment using numpy is {np.linalg.norm(p2 - p1)}")

del segment

# Calculate the length of the line segment using the norm method of the Point class
print(f"The length of the line segment invoking norm method of class Point is {segment.point.norm()}")




