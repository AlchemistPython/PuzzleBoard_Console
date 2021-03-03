def showBoard(method_to_decorate):
    """Method that print the puzzle board"""
    def printPuzzle(self):
        method_to_decorate(self)
        # printing the puzzle
        for account,rows in enumerate(self.puzzle_board):
            print("\n-----------------------")
            for element in rows:
                if len(element) > 1:
                    print(f"|{element} |".rjust(4),end=' ')
                else:
                    print(f"| {element} |".rjust(4),end=' ')
            if account == 3:
                print("\n-----------------------")
    return printPuzzle

def shuffleItems(method_to_decorate):
    """Method that shuffle the items inside the list"""
    def shuffle(self):
        method_to_decorate(self)
        from random import shuffle
        shuffle(self.puzzle_board)
        for sublist in self.puzzle_board:
            shuffle(sublist)
    return shuffle
            
class Puzzle:
    def __init__(self):
        self.puzzle_board = []
        self.EMPTY = ' '
    
    @showBoard
    @shuffleItems
    def fillBoard(self):
        """Method that fills the list puzzle_board with list of numbers from 1 to 15 and an empty space"""
        new_list = list()
        account = 0
        for account, number in enumerate(range(1,17),start=1):
            number = str(number) if account != 16 else self.EMPTY
            new_list.append(number)
            if account in (4,8,12,16):
                self.puzzle_board.append(new_list)
                new_list = list()
    
    def findItem(self, value=' '):
        """Method that find the coordenates of the value, if the value it's empty use the default value"""
        row, col = 0,0
        for rows in range(len(self.puzzle_board)):
            if value in self.puzzle_board[rows]:
                row, col = rows, self.puzzle_board[rows].index(value)
                break
        return row, col
    
    #getter function
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        numbers = [str(str_number) for str_number in range(1,16)]
        if value in numbers:
            self.__number = value
        else:
            print("This number there isn't in the board!")
    
    @number.deleter
    def number(self):
        del self.__number
    
    @showBoard
    def swapItems(self):
        """Method that swap the items if there are near"""
        empty_row, empty_col = self.findItem(self.EMPTY)
        value_row, value_col = self.findItem(self.__number)
        patterns = [(empty_row - 1,empty_col),(empty_row + 1,empty_col),(empty_row,empty_col -1),(empty_row,empty_col + 1)]
        
        if (value_row,value_col) in patterns:
            self.puzzle_board[value_row][value_col], self.puzzle_board[empty_row][empty_col] = self.puzzle_board[empty_row][empty_col],self.puzzle_board[value_row][value_col]
        else:
            print("\nCan't move, empty space is not close")
    
    

new_puzzle = Puzzle()
new_puzzle.fillBoard()

new_puzzle.number = '8'
new_puzzle.swapItems()
del new_puzzle.number

new_puzzle.number = '15'
new_puzzle.swapItems()
del new_puzzle.number

new_puzzle.number = '14'
new_puzzle.swapItems()
del new_puzzle.number

# new_puzzle.number = 13
# new_puzzle.swapItems()
# del new_puzzle.number

new_puzzle.number = '10'
new_puzzle.swapItems()
# del new_puzzle.number