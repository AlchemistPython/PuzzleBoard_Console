from puzzleboard import Puzzle

class Game(Puzzle,Player):
    
    def __init__(self,name="Player 1"):
        Puzzle.__init__(self)
        Player.__init__(self,name)
        self.__counter = 100
    
    @staticmethod
    def instructions():
        print("""Welcome to Puzzle Game 
              Instructions:
              
              1.- Order the numbers equal at level showed.
              
              2.- Every change of numbers will rest the points given at the beginning.
              
              3.- If the points are equal to 0, the game it's over. """)
        
    @property
    def points(self):
        return self.__counter
    
    @points.setter
    def points(self):
        self.__counter -= 1


def game():
    Game().instructions()
    player_name = input("Player Name: ")
    new_game = Game(player_name)
    print(new_game.name)

game()