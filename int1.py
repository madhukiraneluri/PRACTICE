class Circle:
    def __init__(self,r):
        self.r=r
    @property
    def area(self):
        return f" Area is {math.pi*self.r**2}"
    @property
    def 