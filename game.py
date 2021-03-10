from puzzleboard import Puzzle
from player import Player

class Game(Puzzle):
    
    def __init__(self):
        super().__init__()
        self.__counter = 100
    
    @staticmethod
    def instructions():
        """Static Method that I use to show instructions to the puzzle game."""
        print("""Welcome to Puzzle Game 
              Instructions:
              
              1.- Order the numbers equal at level showed.
              
              2.- Every change of numbers will rest the points given at the beginning.
              
              3.- If the points are equal to 0, the game it's over. 
              
              From the next puzzles select one of them to solve.
              
              1.- Horizontal.
              2.- Vertical
              3.- Diagonal
              4.- Snail
              5.- Spiral
              6.- Impossible
              """)
        
    @property
    def points(self):
        return self.__counter
    
    @points.setter
    def points(self):
        self.__counter -= 1
    
    @points.deleter
    def points(self):
        del self.__counter
                


def start_game():
    Game().instructions()
    type_board = input("Select the number of board: ")
    player_name = input("Your Player Name is: ")
    # instance three objects
    new_game = Game()
    new_game.kind = type_board
    new_game.whatBoard()
    # begin the puzzle
    

start_game()