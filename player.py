class Player:
    
    def __init__(self, player_name="Player None"):
        self.__name = player_name
    
    @property
    def playerName(self):
        return self.__name
    
    @playerName.setter
    def playerName(self, player_name):
        self.__name = player_name
    
    @playerName.deleter
    def playerName(self):
        del self.__name
    
    # @property
    # def number(self):
    #     return self.__number
    
    # @number.setter
    # def number(self, number):
    #     self.__number = number
    
    # @number.deleter
    # def number(self):
    #     return self.__number