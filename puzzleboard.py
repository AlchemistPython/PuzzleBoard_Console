from random import shuffle
def showPuzzle(function):
    def printPuzzle(self):
        puzzle = function(self)
        
        for account, rows in enumerate(puzzle):
            print("\n-----------------------")
            for value in rows:
                if len(value) > 1:
                    print(f"|{value} |".rjust(4),end=' ')
                else:
                    print(f"| {value} |".rjust(4),end=' ')
            if account == 3:
                print("\n-----------------------")
    return printPuzzle          
class Puzzle:
    
    def __init__(self):
        self.__numbers =  [str(number) for number in range(1,17)]
        self.__board = list()
        self.__predefinedboard = list()
        self.__kind = ''
        self.__EMPTY = ' '
    
    @showPuzzle
    def fillBoard(self):
        """Method that fill the list"""
        temporal_list = list()
        shuffle(self.__numbers) 
        for account, number in enumerate(self.__numbers,start=1):
            number = str(number) if account != 16 else self.__EMPTY
            temporal_list.append(number)
            if account in (4,8,12,16):
                self.__board.append(temporal_list)
                temporal_list = list()
        return self.__board
    
    def __findItem(self, number):
        """Method that find the coordenates of the vlue, if the value it's empty use the default value"""
        row, col = 0, 0
        for rows in range(len(self.__board)):
            if number in self.__board[rows]:
                row, col = rows, self.__board[rows].index(number)
                break
        return row, col
    
    @showPuzzle
    def swapItems(self):
        """Method that swap the items if there are near"""
        empty_row, empty_col = self.__findItem(self.__EMPTY)
        player_row, player_col = self.__findItem(self.__number)
        
        move_player = [(empty_row - 1, empty_col),(empty_row + 1,empty_col),(empty_row,empty_col +1),(empty_row, empty_col -1)]
        
        if (player_row, player_col) in move_player:
            self.__board[player_row][player_col], self.__board[empty_row][empty_col] = self.__board[empty_row][empty_col], self.__board[player_row][player_col]
        else:
            print("\nCan't move, empty space isn't close!")
        
        return self.__board
    # it's just temporal, this it's gonna be in player class
    # getter
    @property
    def number(self):
        return self.__number
    # setter
    @number.setter
    def number(self, n):
        if n in self.__numbers:
            self.__number = n
        else:
            raise TypeError("Expected a number from the board!")
    # deleter
    @number.deleter
    def number(self):
        del self.__number
    
    # getter
    @property
    def kind(self):
        return self.__kind
    
    @kind.setter
    def kind(self, kind="Horizontal"):
        difficulty = {
            1:'Horizontal',
            2:'Vertical',
            3:'Diagonal',
            4:'Snail',
            5:'Spiral',
            6:'Impossible'
            }
        if kind in difficulty.values():
            self.__kind = kind
        else:
            raise ValueError("The option isn't here!")
    
    @kind.deleter
    def kind(self):
        del self.__kind
    # i don't know if this its convinces me, think more at respect
    def __patternBoard(self):
        """Method that store the patterns of the challenge of this game"""
        boards = {
            "Horizontal" : [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15',' ']],
            "Vertical" : [['1','5','9','13'],['2','6','10','14'],['3','7','11','15'],['4','8','12',' ']],
            "Diagonal" : [['7','11','14',' '],['4','8','12','15'],['2','5','9','13'],['1','3','6','10']],
            "Snail": [['1','2','3','4'],['12','13','14','5'],['11',' ','15','6'],['10','9','8','7']],
            "Spiral": [['7','8','9','10'],['6','1','2','11'],['5','4','3','12'],[' ','15','14','13']],
            "Impossible": [['15','14','13','12'],['11','10','9','8'],['7','6','5','4'],['3','2','1',' ']]
        }
        self.__predefinedboard = boards[self.__kind]
        return self.__predefinedboard
    @showPuzzle
    def whatBoard(self):
        """Method that print the board to use"""
        self.__patternBoard()
        print(f"\n== {self.__kind} Puzzle ==")
        puzzle_board = self.__predefinedboard
        return puzzle_board
        
        
new_puzzle = Puzzle()
new_puzzle.fillBoard()

# new_puzzle.kind = "Diagonal"
# new_puzzle.whatBoard()
# del new_puzzle.kind

# new_puzzle.kind = "Spiral"
# new_puzzle.whatBoard()
# del new_puzzle.kind

# new_puzzle.kind = "Impossible"
# new_puzzle.whatBoard()
# del new_puzzle.kind

# new_puzzle.kind = "Snail"
# new_puzzle.whatBoard()
# del new_puzzle.kind
# new_puzzle.number='15'
# new_puzzle.swapItems()
# del new_puzzle.number
# new_puzzle.number='11'
# new_puzzle.swapItems()
# del new_puzzle.number
# new_puzzle.number='3'
# new_puzzle.swapItems()
# del new_puzzle.number