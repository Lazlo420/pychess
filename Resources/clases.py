[0,0]
[1,2]

[1,-1,0,1,-1,0,1,-1,0]
[1,1,1,0,0,0,-1,-1,-1]

[]
[]

[]
[]

[]
[]

class ficha():
    def __init__(self, x, y,movex,movey):
        self.x=x
        self.y=y
        self.movex=movex
        self.movey=movey
        self.atack=[]

class peon(ficha):
    def __init__(self, x, y, movex, movey):
        super().__init__(x, y, movex, movey)
        

class king(ficha):
    def __init__(self, x, y, movex, movey):
        super().__init__(x, y, movex, movey)

class queen(ficha):
    def __init__(self, x, y, movex, movey):
        super().__init__(x, y, movex, movey)

class towr(ficha):
    def __init__(self, x, y, movex, movey):
        super().__init__(x, y, movex, movey)

class bishp(ficha):
    def __init__(self, x, y, movex, movey):
        super().__init__(x, y, movex, movey)

class knght(ficha):
    def __init__(self, x, y, movex, movey):
        super().__init__(x, y, movex, movey)

