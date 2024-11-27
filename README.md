# Solve a Cryptarithmetic Puzzle
This program solves a cryptarithmetic puzzle, `SEND + MORE = MONEY` in the demonstrated example. Each unique letter represents a distinct digit from `0-9`. The goal is to determine the correct digit for each letter such that the sum of the left hand side equals the value of the right hand side.

## Problem Description
The program solves puzzles where:
- Each letter in the words is replaced by a unique digit.
  
- The sum of the words must be valid with the correct digits assigned.
  
- The first letters of each word cannot be 0.

The classic example is:
```
  SEND
+ MORE
------
 MONEY
```
The program tries to assign digits to letters in such a way that the equation holds true.

## Functionality
The program uses a recursive approach to try all possible combinations to get the result. It uses backtracking if one combination is incorrect to determine the next one. It ensures that:
- No two letters have the same digit.

- The first letter of each word in not assigned as 0.

The function `puzzle_solve()` performs a depth-first search to explore all possible assignments, and the helper function `is_valid_solution()`verifies whether a solution satisfies the equation.

## How to Run:
1. Ensure you have Python 3 installed on your system.
   
2. Clone or download the repository.
   
3. Navigate to the directory containing the `find.py` file.
   
4. Run the program:
   ```
   python3 find.py
   ```

You can modify the `puzzle` variable in the `main()` to solve other similar cryptarithmetic puzzles. 

## Example Output
If a solution is found, the program will display the digit assignment for each letter.

```
Solution found:
D = 7
E = 5
M = 1
N = 6
O = 0
R = 8
S = 9
Y = 2
```

## Limitations
The program assumes that there are no more than 10 unique letters in the puzzle.
