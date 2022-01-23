import random
from Hilo.cards import card

CARD = card()

class hilo:
    """
    A game in which the player guesses if the next card drawn 
    by the dealer will be higher or lower than the previous one.
    
    Attributes:
        current_card (int): The value of the last card drawn.
        next_card (int): The value of the next card drawn.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score the player has accumulated.
    """

    def __init__(self):
        """Constructs a new instance of hilo with a value and points attribute.
        
        Args:
            self (hilo): an instance of hilo.
        """

        self.current_card = CARD.card_draw()
        self.next_card = CARD.card_draw()
        self.is_playing = True
        self.score = 300

    def run_game(self):
        """Runs through every step of the game in order.
        
        Args:
            self (hilo): an instance of hilo.
        """


        while self.is_playing:

            # Print the current card
            print(f"The current card is: {self.current_card}")

            # Take high or low
                        
            self.h_l = input(f"Higher or lower? [h/l] ")

            # Cristian De La Hoz added this code to validate the entry of highest and lowest. 

            if self.h_l != "h":
                pass
                if self.h_l != "l":
                    print("The entered value is not valid, re-enter it!")
                    self.h_l = input(f"Higher or lower? [h/l] ")
                    if self.h_l != "h":
                        pass
                        if self.h_l != "l":
                            print("You have entered the wrong value again, thanks for playing!")
                            exit()

            # Draw the next card and show it
            self.next_card = CARD.card_draw()
            print(f"Next card was: {self.next_card}")
            
            # If they guessed right, + 100 points, if they guessed wrong, -75 points.
            if (self.h_l.lower() == "h" and self.next_card > self.current_card) or (self.h_l.lower() == "l" and self.next_card < self.current_card):
                self.score += 100
            else:
                self.score -= 75
            
                # Replace the current card with the next card to set up for the next loop.
            self.current_card = self.next_card
                    
                # Show them their current score
            print(f"Your score is: {self.score}")
                    
                # Ends the game if the score is 0 or less.
            if self.score <= 0:
                self.is_playing = False

                # Asks if the user wants to play again and ends the game if they say no.
            if self.is_playing:
                continue_ = input(f"Play again? [y/n] ")
                self.is_playing = (continue_.lower() == "y")
            print()

        # Thanks the user for playing and displays their end score.
        print(f"Thanks for playing! Your end score was {self.score}")
 
