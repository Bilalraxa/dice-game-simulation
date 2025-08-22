# Dice Game Simulation (Craps)

This project simulates a dice game similar to **Craps**, where players roll two dice and try to win based on the sum of the dice.

---

## Files

- **main.py** – Entry point of the program. Handles running a single game or multiple games, printing results, and logging statistics.
- **player.py** – Contains the `Player` class, which rolls dice, tracks outcomes, and determines wins or losses according to the game rules.
- **die.py** – Contains the `Die` class, which simulates a six-sided die with methods to roll it and retrieve its value.

---

## How to Run

1. Clone or download the repository:

```bash
git clone https://github.com/YourUsername/dice-game-simulation.git


Navigate to the project folder:

cd dice-game-simulation


Run the program:

python main.py

Program Flow

The program first runs one sample game and prints the results after each roll.

The user is then prompted to enter the number of games to simulate.

The program runs the specified number of games, calculating:

Total wins

Total losses

Average rolls per win/loss

Winning percentage

Multi-game results are saved in log.txt in the project directory.

Example
Running one sample game in full:
(3, 4) total = 7
You win!
How many games would you want to have tested: 10
The total number of wins is 6
The total number of losses is 4
The average number of rolls per win is 1.50
The average number of rolls per loss is 1.75
The winning percentage is 0.600
The multi-game has been saved into the log.


Make sure Python 3.x is installed on your system.

All files must be in the same directory (main.py, player.py, die.py) for the program to work correctly.
