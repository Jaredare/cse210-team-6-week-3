import random



class card:
    """A small piece of paper with intelligible writing on the front
   
    Attributes:
        none
    """
    def __init__(self):
        pass

    def card_draw(self):
        return random.randint(1, 13)

        
