"""Exploring __init__() method"""

class Computer:
    """Init methode exploration class"""
    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu

    def config(self):
        """Config printing method"""
        print(f"This is an {self.cpu} machine with {self.ram} ram")

computer_1 = Computer( 8,"i5")

computer_1.config()

