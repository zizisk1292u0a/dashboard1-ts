#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Number Guessing Game Simulator"""

def simulate_game(target, max_attempts):
    import random
    attempts = 0
    
    while attempts < max_attempts:
        guess = random.randint(1, 100)
        attempts += 1
        
        if guess == target:
            return f"Found {target} in {attempts} attempts!"
        elif guess < target:
            print(f"Attempt {attempts}: {guess} - Too low")
        else:
            print(f"Attempt {attempts}: {guess} - Too high")
    
    return f"Failed to find {target} in {max_attempts} attempts"

if __name__ == "__main__":
    result = simulate_game(60, 4)
    print(result)
