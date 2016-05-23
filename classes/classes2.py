"""
Notes: =========================================================================
Notes: Define arthmatic operations for non-builtin object class.
Notes: 
Notes: __add__      for     +
Notes: __sub__      for     -
Notes: __mul__      for     *
Notes: __div__      for     /
Notes: 
Notes: __str__      for     string representation of a class
Notes: 
"""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2D(self.x-other.x, self.y-other.y)

    # Dot product of vectors
    def __mul__(self, other):
        return Vector2D(self.x*other.x, self.y*other.y)

    def __div__(self, other):
        return Vector2D(self.x/float(other.x), self.y/float(other.y))

    # Following definition is used for string representation of a Class.
    def __str__(self):
        return "(X:" + str(self.x) + ", Y:" + str(self.y) + ")"

    def __repr__(self):
        return "(X:" + str(self.x) + ", Y:" + str(self.y) + ")"

#===============================================================================
# Create two vectors
vec1 = Vector2D(3,4)
vec2 = Vector2D(6,8)
vec3 = Vector2D(9,12)

print "vec1 = ", vec1
print "vec2 = ", str(vec2)
print "vec3 = ", repr(vec3)
print ""


#===============================================================================
# Addition
print "x = ", (vec1 + vec2 + vec3).x, "y = ", (vec1 + vec2 + vec3).y

vec4 = Vector2D(0,0)
vec4 += vec1 + vec2 + vec3
print "vec1 + vec2 + vec3 = ", vec4
print ""


#===============================================================================
# Subtraction
print "x = ", (vec3 - vec2).x, "y = ", (vec3 - vec2).y

vec4 = vec3 - vec2
print "vec3 - vec2 = ", vec4
print ""


#===============================================================================
# Multiplication
print "x = ", (vec1 * vec2).x, "y = ", (vec1 * vec2).y

vec4 = vec1 * vec2
print "vec1 * vec2 = ", vec4
print ""


#===============================================================================
# Division
print "x = ", (vec3 / vec1).x, "y = ", (vec3 / vec1).y

vec4 = vec3 / vec1
print "vec3 / vec1 = ", vec4
print ""
