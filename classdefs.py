class person():
    def __init__(self):
        self.life=1
        self.location= {'x':1,'y':1}

class bomberman(person):
    def __init__(self):
        person.__init__(self)
        self.life=3

class bomb():
    def __init__(self):
        self.time_left = 3