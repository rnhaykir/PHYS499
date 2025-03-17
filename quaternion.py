import math

class Quaternions():
    # Initialize the components
    def __init__(self, a = [0, 0, 0, 0]):
        self.__a0, self.__a1, self.__a2, self.__a3 = a[0], a[1], a[2],a[3]

    # Calculate the magnitude of the vector
    def __abs__(self):
        return math.sqrt(self.__a0**2 + self.__a1**2 + self.__a2**2 + self.__a3**2)
    
    # Vector addition for a + b
    def __add__(self, b):
        return Quaternions([self.__a0 + b.__a0, self.__a1 + b.__a1, self.__a2 + b.__a2, self.__a3 + b.__a3])
    
    # Vector multiplication for a * b
    def __mul__(self, b):
        return Quaternions([
            self.__a0 * b.__a0 - self.__a1 * b.__a1 - self.__a2 * b.__a2 - self.__a3 * b.__a3,
            self.__a0 * b.__a1 + self.__a1 * b.__a0 + self.__a2 * b.__a3 - self.__a3 * b.__a2,
            self.__a0 * b.__a2 - self.__a1 * b.__a3 + self.__a2 * b.__a0 + self.__a3 * b.__a1,
            self.__a0 * b.__a3 + self.__a1 * b.__a2 - self.__a2 * b.__a1 + self.__a3 * b.__a0
        ])
    
    # Check if given two vectors are equal
    def __equal__(self, b):
        if self.__a0 == b.__a0 and self.__a1 == b.__a1 and self.__a2 == b.__a2 and self.__a3 == b.__a3:
            return True
        return False
    
    # Calculate the conjugate vector of the given vector
    def conjugate(self):
        return Quaternions([self.__a0, -1 * self.__a1, -1 * self.__a2, -1 * self.__a3])
    
    # Calculate the inverse vector of the given vector
    def inverse(self):
        a_mag = abs(self*self)
        a_conj = self.conjugate()
        return Quaternions([a_conj.__a0 / a_mag, a_conj.__a1 / a_mag, a_conj.__a2 / a_mag, a_conj.__a3 / a_mag])
    
    # Vector division for a / b
    def quotient(self, b):
        return self.__mul__(b.inverse())
    
    # Return the string form of the vector
    def __str__(self):
        return f"a = ({str(self.__a0)}, {str(self.__a1)}, {str(self.__a2)}, {str(self.__a3)})"
