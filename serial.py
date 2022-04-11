"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.incrament = 0
    
    def generate(self):
        new_serial = self.start + self.incrament
        self.incrament += 1
        return new_serial

    def reset(self):
        self.incrament = 0




        

