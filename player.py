class Player:
    
    def __init__(self, player_name="Player None"):
        self.__name = player_name
    # getter player name
    @property
    def playerName(self):
        return self.__name
    # setter player name
    @playerName.setter
    def playerName(self, player_name):
        self.__name = player_name
    # deleter player name
    @playerName.deleter
    def playerName(self):
        del self.__name
    
    @property
    def playerNumber(self):
        return self.__number_player
    
    @playerNumber.setter
    def playerNumber(self, number_player):
        inside_of_board = [str(numbers) for numbers in range(1,16)]
        if self.__number_player in inside_of_board:
            self.__number_player = number_player
        else:
            raise TypeError("Expected a number from the board!")
    
    
    # @property
    # def number(self):
    #     return self.__number
    
    # @number.setter
    # def number(self, number):
    #     self.__number = number
    
    # @number.deleter
    # def number(self):
    #     return self.__number