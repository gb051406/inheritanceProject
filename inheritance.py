class Technology:
    def __init__(self,brand = "", model = "", color = "black"):
        self.color = color
        self.brand = brand
        self.model = model
    def __repr__(self):
        return "make: " + self.brand + ", model: " + self.model + ", color:" + self.color
class Phone(Technology):
    def __init__(self):
        Technology.__init__(self)
