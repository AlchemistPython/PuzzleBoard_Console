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
        # for rows in range(len(array)):
        #     for cols in array[rows]:
        #         if cols == '':
        #             identifies.setdefault(16,cols)
        #         else:
        #             identifies.setdefault(int(cols),cols)
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
# new_puzzle = PuzzleBoard()
# board = list()
# new_puzzle.fillPuzzle(board)
# dictionary = new_puzzle.defineKeys(board)


# print("Antes: ")
# new_puzzle.showPuzzle(board)
# new_puzzle.shuffleItems(board)
# # dictionary = new_puzzle.defineKeys(board)
# # print("Diccionario:")
# # new_puzzle.showPuzzle(dictionary)
# print("Despues: ")
# new_puzzle.showPuzzle(board)
# """ que con el diccionario el usuario identificara el numero inicial a cambiar y el numero por el cual quiere
# intercambiar, se hace un swap """
#     def fillPuzzle(self):
#         counter:int = 0
#         opening:int, ending:int = 1,5
#         while counter < 16:
#             nlist:list = list()
#             for n:int in range(opening,ending):
#                 n = '' if n == 16 else n
#                 nlist.append(str(n))
#             counter += 4
#             self.board.append(nlist)
#             opening, ending = ending,ending + 4
            
#         return board:list
    
#     def shuffleItems(self,board):
#         from random import shuffle
#         for n in board:
#             shuffle(n) 
#         return board:list
    
#     def labelItems(self,board:list):
#         diccionary:dict = {}
#         cont = 0
#         for f in range(4):
#             for c in board[f]:
#                 cont+=1
#                 diccionary.setdefault(cont,c)
#         return diccionary
                
#     def showList(self):
#         print(self.labelItems()) self.shuffleItems(self.fillPuzzle())

# new_puzzleboard = PuzzleBoard()
# print(new_puzzleboard.showList())