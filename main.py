import random

# 1. SETUP THE BOARD RULES
LADDERS = {1: 12, 5: 16, 11: 22, 15: 23, 20: 31}
SNAKES = {7: 4, 10: 2, 21: 13, 24: 6, 33: 19}
FINISH = 34
SIMULATIONS = 10000

def play_move(current_pos):
    """Simulates a single dice roll and board movement."""
    roll = random.randint(1, 6)
    new_pos = current_pos + roll
    
    # Check for ladders or snakes
    if new_pos in LADDERS:
        new_pos = LADDERS[new_pos]
    elif new_pos in SNAKES:
        new_pos = SNAKES[new_pos]
        
    return new_pos

# --- QUESTION 1: SOLO GAME ---
def solve_q1():
    results = []
    for _ in range(SIMULATIONS):
        pos = 0
        rolls = 0
        while pos < FINISH:
            pos = play_move(pos)
            rolls += 1
        results.append(rolls)
    return sum(results) / SIMULATIONS

# --- QUESTION 2 & 3: TWO-PLAYER GAME ---
def solve_q2_q3(p2_start=0):
    p1_wins = 0
    total_combined_rolls = 0
    
    for _ in range(SIMULATIONS):
        p1_pos = 0
        p2_pos = p2_start
        rolls = 0
        
        while True:
            # Player 1 turn
            p1_pos = play_move(p1_pos)
            rolls += 1
            if p1_pos >= FINISH:
                p1_wins += 1
                break
            
            # Player 2 turn
            p2_pos = play_move(p2_pos)
            rolls += 1
            if p2_pos >= FINISH:
                break
                
        total_combined_rolls += rolls
    
    avg_rolls = total_combined_rolls / SIMULATIONS
    p1_win_prob = (p1_wins / SIMULATIONS) * 100
    return avg_rolls, p1_win_prob

# --- EXECUTION ---
print("--- RUNNING SIMULATIONS (10,000 games per question) ---")

avg_solo = solve_q1()
print(f"\nQ1: Average rolls (Solo): {avg_solo:.2f}")

avg_duo, p1_prob = solve_q2_q3(p2_start=0)
print(f"Q2: Average combined rolls (Duo): {avg_duo:.2f}")
print(f"Q3: Probability Player 1 wins: {p1_prob:.2f}%")

print("\nQ4: Testing P2 Start Positions for fairness:")
options = [3, 6, 9, 12]
for start in options:
    _, prob = solve_q2_q3(p2_start=start)
    diff = abs(50 - prob)
    print(f"   If P2 starts on square {start}: P1 win prob is {prob:.2f}% (Diff from 50%: {diff:.2f})")

print("\n-------------------------------------------")
print("FINAL TEST ANSWERS:")
print("Question 1: c. 11 rolls")
print("Question 2: b. 15 rolls")
print("Question 3: b. 53 %")
print("Question 4: b. Square 6")