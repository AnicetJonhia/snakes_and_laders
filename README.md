# Snakes and Ladders - Board Game Simulation

## Project Overview

This project simulates the classic board game of **Snakes and Ladders** using Python. The simulation runs 10,000 games to analyze various aspects of the game mechanics and answer key questions about player statistics and probabilities.

## Game Rules

### Board Setup
- **Start square**: 0
- **Finish square**: 34
- **Players**: Begin at square 0 (unless modified for testing)

### Ladders (Shortcuts)
| From | To |
|------|-----|
| 1    | 12  |
| 5    | 16  |
| 11   | 22  |
| 15   | 23  |
| 20   | 31  |

### Snakes (Setbacks)
| From | To |
|------|-----|
| 7    | 4   |
| 10   | 2   |
| 21   | 13  |
| 24   | 6   |
| 33   | 19  |

### Game Mechanics
- Players take turns rolling a standard 6-sided die
- Move forward by the number shown on the die
- Landing on the bottom of a ladder advances you to the top
- Landing on a snake's head sends you to the tail
- First player to reach or exceed square 34 wins
- No exact roll required to finish

## Project Structure

```
snakes_and_laders/
├── main.py          # Main simulation script
└── README.md        # This file
```

## How to Run

```bash
python main.py
```

The script will:
1. Run 10,000 simulations for each question
2. Display detailed results including averages and probabilities
3. Print the final answers to all questions

## Questions & Answers

### Quick Links
- [Question 1: Solo Game](#question-1-solo-game)
- [Question 2: Two-Player Game - Combined Rolls](#question-2-two-player-game---combined-rolls)
- [Question 3: Two-Player Game - Win Probability](#question-3-two-player-game---win-probability)
- [Question 4: Fair Odds Adjustment](#question-4-fair-odds-adjustment)

### Question 1: Solo Game
**"If you played the game by yourself, what is the average number of rolls required to finish?"**

- **Options**: 7, 9, 11, 13 rolls
- **Answer**: **c. 11 rolls**

### Question 2: Two-Player Game - Combined Rolls
**"In a two person game, what is the average number of combined rolls by both players required for the game to finish?"**

- **Options**: 13, 15, 17, 19 rolls
- **Answer**: **b. 15 rolls**

### Question 3: Two-Player Game - Win Probability
**"In a two person game, what is the probability that Player 1 wins?"**

- **Options**: 50%, 53%, 57%, 60%
- **Answer**: **b. 53 %**

Player 1 has a slight advantage because they move first, giving them more opportunities to reach the finish before Player 2.

### Question 4: Fair Odds Adjustment
**"From which starting square for Player 2 do we get the closest to equal odds for both players?"**

- **Options**: Square 3, Square 6, Square 9, Square 12
- **Answer**: **b. Square 6**

When Player 2 starts at square 6, the win probability approaches approximately 50%, creating nearly fair odds despite Player 1's first-move advantage.

## Code Structure

### Main Functions

#### `play_move(current_pos)`
Simulates a single turn:
- Rolls a die (1-6)
- Moves the player forward
- Checks for ladder or snake interactions
- Returns the new position

#### `solve_q1()`
Simulates 10,000 solo games and returns the average number of rolls needed to finish.

#### `solve_q2_q3(p2_start=0)`
Simulates 10,000 two-player games with configurable start position for Player 2.
- Returns average combined rolls and Player 1's win probability percentage

## Key Insights

1. **Solo gameplay** averages around 11 rolls due to the mixture of ladders and snakes
2. **Player 1 advantage** is approximately 3% due to moving first
3. **Starting position compensation** shows that advancing Player 2 by 6 squares creates nearly equal odds
4. Results are consistent across multiple runs due to the Law of Large Numbers (10,000 simulations)

## Notes

- Results may vary slightly between runs due to random variation in dice rolls
- The simulation uses Python's `random.randint()` for authentic dice rolls
- Select the answer closest to your simulated results when there are minor discrepancies

## Requirements

- Python 3.x



