class PuzzleBoard:
    
    def fillPuzzle(self, array):
        """ Method that fill the list of lists """
        account,opening,ending = 0,1,5
        
        while account < 16:
            newlist:list = list()
            for number in range(opening, ending):
                number = ' ' if  number == 16 else number
                newlist.append(str(number))
            account += 4
            array.append(newlist)
            opening, ending = ending, ending + 4
        
        return array
    
    def defineKeys(self, array):
        """Define the keys of every value in the list of lists"""
        account = 1
        identifies = dict()
        
        for row in array:
            for col in row:
                identifies.setdefault(account,col)
                account += 1
            account = account      
        return identifies
    
    def shuffleItems(self, array):
        """Method the return a list of lists shuffles"""
        from random import shuffle
        
        shuffle(array)
        
        for sublist in array:
            shuffle(sublist)
        
        return array
    
    def showPuzzle(self, d):
        """Print the board"""
        account,newline = 0,4
        print("-------------------")
        for key,value in d.items():
            if len(value) == 2:
                print(f"{value}|".rjust(4),end=' ')
            else:
                print(f"{value} |".rjust(4),end=' ')
            account += 1
            if account == newline:
                print("\n-------------------")
                newline += 4

new_puzzle = PuzzleBoard()
board = list()
new_puzzle.fillPuzzle(board)
new_puzzle.shuffleItems(board)
dictionary = new_puzzle.defineKeys(board)
new_puzzle.showPuzzle(dictionary) 
