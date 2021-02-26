class Puzzle:
    
    def __init__(self):
        self.array = list()
        self.dict = dict()
        self.account = 0
    
    def fillPuzzle(self):
        """Method that fill the list of lists"""
        # account = self.account
        newlist = list()
        for account, number in enumerate(range(1,17),start=1):
            number = str(number) if number != 16 else 'X'
            newlist.append(number)
            if account in (4,8,12,16):
                self.array.append(newlist)
                newlist = list()
        return self.array
    
    def shuffleItems(self):
        """Method that shuffle a list of lists """
        from random import shuffle
        # shuffle(self.array)
        for sublist in self.array:
            shuffle(sublist)
        return self.array
    
    def establishKeys(self):
        account = self.account
        for boxes in self.array:
            for account, element in enumerate(boxes,start=account+1):
                self.dict.setdefault(account,element)
            account = account
        return self.dict
        
    def showArray(self):
        print(f"\nLista : {self.array}")
    
    def showPuzzle(self):
        print("-----------------------".rjust(4))
        for account, value in enumerate(self.dict.values()):
            if len(value) > 1:
                print(f"|{value} |".rjust(3),end=' ')
            else:
                print(f"| {value} |".rjust(4),end=' ')
            if account in (3,7,11,15):
                print("\n-----------------------")


newpuzzle = Puzzle()
newpuzzle.showArray()
newpuzzle.fillPuzzle()
newpuzzle.showArray()
newpuzzle.shuffleItems()
print(f"\nDictionary: {newpuzzle.establishKeys()}")
# newpuzzle.showArray()
# newpuzzle.showArray()
newpuzzle.showPuzzle()
print()