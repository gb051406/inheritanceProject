class Technology:
    def __init__(self, color ):
        self.color = color
        self.brand = "unknown"
        self.model = "unkown"
    def __repr__(self):
        return "type: " + self.model + ", make: " + self.brand + ", color: " + self.color

class Phone(Technology):
    def __init__(self,color):
        Technology.__init__(self,color)
        self.model = "phone"
class Android(Phone):
    def __init__(self,color):
        Phone.__init__(self,color)
        self.brand = "android"
class Apple(Phone):
    def __init__(self,color):
        Phone.__init__(self,color)
        self.brand = "apple"

class Television(Technology):
    def __init__(self,color):
        Technology.__init__(self,color)
        self.model = "television"
class lgtv(Television):
    def __init__(self,color):
        Television.__init__(self,color)
        self.brand = "lgtv"
class samsung(Television):
    def __init__(self,color):
        Television.__init__(self,color)
        self.brand = "samsung"

class Computer(Technology):
    def __init__(self,color):
        Technology.__init__(self,color)
        self.model = "computer"
class Apple(Computer):
    def __init__(self,color):
        Technology.__init__(self,color)
        self.model = "apple"
class Microsoft(Computer):
    def __init__(self,color):
        Technology.__init__(self,color)
        self.model = "microsoft"

tech1 = Android("silver")
print(tech1)
tech2 = samsung()
print(tech2)
tech3 = Microsoft("white")
print(tech3)