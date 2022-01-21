import random
from Hilo.cards import card

CARD = card()

class hilo:

    def __init__(self):
        

        self.current_card = CARD.card_draw()
        self.next_card = CARD.card_draw()
        self.is_playing = True
        self.score = 300

    def start_game(self):
        
        while self.is_playing:
            print(f"The current card is: {self.current_card}")

            self.h_l = input(f"Higher or lower? [h/l] ")
            self.next_card = CARD.card_draw()
            print(f"Next card was: {self.next_card}")
            

            if (self.h_l.lower() == "h" and self.next_card > self.current_card) or (self.h_l.lower() == "l" and self.next_card < self.current_card):
                self.score += 100
            else:
                self.score -= 75

            self.current_card = self.next_card
            
            print(f"Your score is: {self.score}")

            if self.score <= 0:
                self.is_playing = False

            if self.is_playing:
                continue_ = input(f"Play again? [y/n] ")
                self.is_playing = (continue_.lower() == "y")
            print()

        print(f"Thanks for playing! Your end score was {self.score}")


