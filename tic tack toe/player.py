import math
import random

from numpy import square


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
    
    
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        #initializing super class on the sub class
        super().__init__(letter)
    
    def get_move(self, game):
        # if no moves made pick a random space
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #get square based of minimax algoritm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):   # state represents current board but also game variable
        max_player = self.letter 
        other_player = 'O' if player =='X' else 'X'    # if letter x then letter o    
        
        # first, we want to check if the previous move is a winner
        #this is a base case
        if state.current_winner == other_player:
            # we should return the position and score because we need to keep track for minimax to work
            # print({'position': None,
            #        'score': 1* (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            #        })
            return{'position': None,
                   'score': 1* (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
                   }
        elif not state.empty_squares(): # no empty squares
            return{'position':None, 'score': 0}
        
        #start of the algoritm
        if player == max_player:
            #saves best position on the board with the best score
            best = {'position': None, 'score': -math.inf} # each score should be maximized
           
        else:
            best = {'position':None, 'score': math.inf} # each score should be minimized
          
        
        for possible_move in state.available_moves():
            # step 1 make a move, try that spot
            state.make_move(possible_move, player)
           
            # step 2 recurse using minmax to simulate a game after  step 1 move
            sim_score = self.minimax(state, other_player) # here we alternate players

            #step 3 undo that move to try the next one in the next iteration
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # this represents the most optimal move
           
            #step 4 update dictionare if nessassary with best move
            
            if player == max_player: # we are trying to maximize max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else: # minimize other player
                if sim_score['score'] < best['score']:
                    best = sim_score
                    
        return best