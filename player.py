class Player:
    
    def __init__(self, name):
        self.__name = name
        self.__number = None
    
    @property
    def name(self):
        return f"Player name: {self.__name}"
    
    @name.setter
    def name(self, name):
        if name == "Player 1":
            self.__name = name
    
    @name.deleter
    def name(self):
        del self.__name
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number=None):
        while True:
            if number != None:
                self.__number = str(number)
                break
            print("Error, pls write a number.")
    
    @number.deleter
    def number(self):
        del self.__number