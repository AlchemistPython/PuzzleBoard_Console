class PuzzleBoard:
    
    def fillPuzzle(self):
        counter = 0
        board = list()
        opening, ending = 1,5
        while counter < 16:
            nlist = list()
            for n in range(opening,ending):
                n = '' if n == 16 else n
                nlist.append(str(n))
            counter += 4
            board.append(nlist)
            opening, ending = ending,ending + 4
            
        return board
    
    def showList(self):
        return self.fillPuzzle()

new_puzzleboard = PuzzleBoard()
print(new_puzzleboard.showList())