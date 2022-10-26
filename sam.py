from results import Triangle

class ColoredTriangle(Triangle):
    def __init__(self,a,b,color):
        super().__init__(a,b)
        self.color = color
    def describe(self): 
        #return f"I am a triangle with sides: {self.a} & {self.b}. I am {self.color}"
        msg=super().describe()
        return msg + f"I am {self.color}"
