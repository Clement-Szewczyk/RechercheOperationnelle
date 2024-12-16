
class Transition:

    def __init__(self, depart, arrive):
        self.depart = depart
        self.arrive = arrive
    
    def __str__(self):
        return f'{self.depart} -> {self.arrive}'