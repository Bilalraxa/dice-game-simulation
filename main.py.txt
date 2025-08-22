from player import Player
from datetime import datetime

def playOneGame():
    player = Player()
    while not player.isWinner() and not player.isLoser():
        player.rollDice()
        print(player)

    if player.isWinner():
        print("You win!")
    else:
        print("You lose!")

def playMultipleGames(number):
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0

    for count in range(number):
        player = Player()
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls

    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    if wins > 0:
        print("The average number of rolls per win is %0.2f" % (winRolls / wins))
    if losses > 0:
        print("The average number of rolls per loss is %0.2f" % (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))
    print("The multi-game has been saved into the log.")

    logStats(wins, losses, winRolls, lossRolls, number)

def logStats(wins, losses, winRolls, lossRolls, number):
    file = open("log.txt", "a")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file.write("\n\ndate and time = " + dt_string)
    file.write("\nThe total number of wins is " + str(wins))
    file.write("\nThe total number of losses is " + str(losses))
    if wins > 0:
        file.write("\nThe average number of rolls per win is " + str(winRolls / wins))
    if losses > 0:
        file.write("\nThe average number of rolls per loss is " + str(lossRolls / losses))
    file.write("\nThe winning percentage is " + str(wins / number))

def main():
    print("Running one sample game in full:")
    playOneGame()
    number = 0
    while number <= 0:
        user_input = input("How many games would you want to have tested: ")
        try:
            number = int(user_input)
            if number <= 0:
                print("Please enter in a positive number.")
                number = 0
            else:
                playMultipleGames(number)
        except ValueError:
            print("Please enter in a number for the number of games.")

if __name__ == "__main__":
    main()
