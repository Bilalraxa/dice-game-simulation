from die import Die

class Player:
    def __init__(self):
        self.firstDie = Die()
        self.secondDie = Die()
        self.roll = ""
        self.rollsCount = 0
        self.startOfGame = True
        self.winner = self.loser = False

    def getNumberOfRolls(self):
        return self.rollsCount

    def rollDice(self):
        self.rollsCount += 1
        self.firstDie.roll()
        self.secondDie.roll()
        v1, v2 = self.firstDie.getValue(), self.secondDie.getValue()
        self.roll = str((v1, v2)) + " total = " + str(v1 + v2)

        if self.startOfGame:
            self.initialSum = v1 + v2
            self.startOfGame = False
            if self.initialSum in (2, 3, 12):
                self.loser = True
            elif self.initialSum in (7, 11):
                self.winner = True
        else:
            laterSum = v1 + v2
            if laterSum == 7:
                self.loser = True
            elif laterSum == self.initialSum:
                self.winner = True

        return v1, v2

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser

    def play(self):
        while not self.isWinner() and not self.isLoser():
            self.rollDice()
        return self.isWinner()

    def __str__(self):
        return self.roll
