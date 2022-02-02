import math
import random


# defining super class player
class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
        
    def get_move(self, game):
        pass
    
    #subclass of super Class
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        #initializing super class on the sub class
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves()) #picks a random spot
        return square
    
    #subclass of super Class
class HumanPlayer(Player):
    def __init__(self, letter):
        #initializing super class on the sub class
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. input move (0-8): ')
            # check if it is a valid input
            try:
                val = int(square) # check if string can be converted
                if val not in game.available_moves(): #if selection is available
                    raise ValueError
                valid_square = True
            except ValueError:
                print( "invalid sqaure, please try again")
                
        return val