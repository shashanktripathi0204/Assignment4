class Triangle:
    def __init__(self):
        self.a=int(input(""))
        self.b = int(input(""))
        self.c = int(input(""))
class Area(Triangle):
    def __init__(self):
        Triangle.__init__(self)
    def answer(self):
        s=(self.a+self.b+self.c)/2.0
        p=(s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        print (p)

ans=Area()
ans.answer()