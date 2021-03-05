def showBoard(decorating):
    """Decorator that print the puzzle board"""
    def printPuzzle(self):
        board = decorating(self)
        for account, rows in enumerate(board):
            print("\n-----------------------")
            for element in rows:
                if len(element) > 1:
                    print(f"|{element} |".rjust(4),end=' ')
                else:
                    print(f"| {element} |".rjust(4),end=' ')
            if account == 3:
                print("\n-----------------------")
    return printPuzzle
class Puzzle:
    
    def __init__(self):
        self.__player_board = list()
        self.__challenge = list()
        self.__type_board  = ''
        self.__EMPTY = ' '
    
    @showBoard
    def fillBoard(self):
        """ Method that fill the list of lists and shuffle the principal board"""
        aux_list = list()
        for account, number in enumerate(range(1,17), start=1):
            number = str(number) if account != 16 else self.__EMPTY
            aux_list.append(number)
            if account in (4,8,12,16):
                self.__player_board.append(aux_list)
                aux_list = list()
        return self.__player_board
    
    def findItem(self, value):
        """Method that find the coordenates of the value, if the value it's empty use the default value"""
        row, col = 0,0
        for rows in range(len(self.__player_board)):
            if value in self.__player_board[rows]:
                row, col = rows, self.__player_board[rows].index(value)
                break
        return row, col
    # checa aqui ya que cambie el decorador y ahora almacena el valor en una variable local
    # y puede llegar a ocasionar un problema ya que no hay return aqui
    @showBoard
    def swapItems(self, number):
        """Method that swap the items if there are near"""
        empty_row, empty_col = self.findItem(self.__EMPTY)
        player_row, player_col = self.findItem(number)
        
        patterns = [(empty_row -1,empty_col),(empty_row + 1, empty_col),(empty_row,empty_col -1),(empty_row,empty_col + 1)]
        
        if (player_row,player_col) in patterns:
            self.__player_board[player_row][player_col], self.__player_board[empty_row][empty_col] = self.__player_board[empty_row][empty_col], self.__player_board[player_row][player_col]
        else:
            print("\nCan't move, empty space isn't close!")
    
    # important temporal!
    # getter
    @property
    def putANumber(self):
        return self.__number
    # setter
    @putANumber.setter
    def putANumber(self,player_number):
        in_the_board = [str(numbers) for numbers in range(1,16)]
        if player_number in in_the_board:
            self.__number = player_number
        else:
            raise TypeError("Expected a number from the board!")
    
    # deleter
    @putANumber.deleter
    def putANumber(self):
        del self.__number
        
    # getter name of the board
    @property
    def typeBoard(self):
        return self.__type_board
    
    # Setter
    @typeBoard.setter
    def typeBoard(self, board = "Horizontal"):
        difficulty = {1:'Horizontal',2:'Vertical',3:'Diagonal',4:'Snail',5:'Spiral',6:'Impossible'}
        if board in difficulty.values():
            self.__type_board = board
        else:
            print("The option enter isn't here!")
    
    def __patternBoard(self):
        """Method that store the patterns of the challenge of this game"""
        patterns = {
            "Horizontal": [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15',' ']],
            "Vertical": [['1','5','9','13'],['2','6','10','14'],['3','7','11','15'],['4','8','12',' ']],
            "Diagonal": [['7','11','14',' '],['4','8','12','15'],['2','5','9','13'],['1','3','6','10']],
            "Snail": [['1','2','3','4'],['12','13','14','5'],['11',' ','15','6'],['10','9','8','7']],
            "Spiral": [['7','8','9','10'],['6','1','2','11'],['5','4','3','12'],[' ','15','14','13']],
            "Impossible": [['15','14','13','12'],['11','10','9','8'],['7','6','5','4'],['3','2','1',' ']]
        }
        self.__challenge = patterns[self.__type_board]
    
    @showBoard
    def challengeBoard(self):
        """Challenge Board"""
        self.__patternBoard()
        print(f"\n== {self.__type_board} Puzzle ==")
        challenge_board = self.__challenge
        return challenge_board
    
    
        

new_puzzle = Puzzle()
new_puzzle.fillBoard()
new_puzzle.typeBoard = "Diagonal"
new_puzzle.challengeBoard()
new_puzzle.typeBoard = "Spiral"
new_puzzle.challengeBoard()