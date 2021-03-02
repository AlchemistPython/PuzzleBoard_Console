def decorator(function):
    def printPuzzle(obj,*args):
        function(obj,*args)
        # printing the puzzle
        for account,rows in enumerate(obj.puzzle_board):
            print("\n-----------------------")
            for element in rows:
                if len(element) > 1:
                    print(f"|{element} |".rjust(4),end=' ')
                else:
                    print(f"| {element} |".rjust(4),end=' ')
            if account == 3:
                print("\n-----------------------")
    return printPuzzle

def shuffleItems(function):
    def shuffle(obj):
        from random import shuffle
        shuffle(obj.puzzle_board)
        for sublist in obj.puzzle_board:
            shuffle(sublist)
        function(obj)
    return shuffle
            
class Puzzle:
    def __init__(self):
        self.puzzle_board = []
        self.EMPTY = ' '
    # check this
    @decorator
    @shuffleItems
    def fillBoard(self):
        new_list = list()
        account = 0
        for account, number in enumerate(range(1,17),start=1):
            number = str(number) if account != 16 else self.EMPTY
            new_list.append(number)
            if account in (4,8,12,16):
                self.puzzle_board.append(new_list)
                new_list = list()
    
    def findItem(self, value=' '):
        row, col = 0,0
        for rows in range(len(self.puzzle_board)):
            if value in self.puzzle_board[rows]:
                row, col = rows, self.puzzle_board[rows].index(value)
                break
        return row, col
    
    @decorator
    def swapItems(self, value):
        
        empty_row, empty_col = self.findItem(self.EMPTY)
        value_row, value_col = self.findItem(value)
        patterns = [(empty_row - 1,empty_col),(empty_row + 1,empty_col),(empty_row,empty_col -1),(empty_row,empty_col + 1)]
        
        if (value_row,value_col) in patterns:
            self.puzzle_board[value_row][value_col], self.puzzle_board[empty_row][empty_col] = self.puzzle_board[empty_row][empty_col],self.puzzle_board[value_row][value_col]
        else:
            print("No se puede chavo")

    
    

new_puzzle = Puzzle()
new_puzzle.fillBoard()
new_puzzle.swapItems('8')
new_puzzle.swapItems('15')
new_puzzle.swapItems('14')
new_puzzle.swapItems('13')
new_puzzle.swapItems('10')