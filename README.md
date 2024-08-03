# Blokus Search Algorithms

## Introduction
This project involves implementing various search algorithms to solve puzzles based on the game Blokus. The primary goal is to apply different search strategies to navigate the game board and find solutions to predefined problems.

## Project Structure

### Files to Edit
- `search.py`: Contains the implementations of the search algorithms.
- `blokus_problems.py`: Defines the problem structures and includes helper functions.

### Files to Review
- `game.py`: Main file for running and observing Blokus games.
- `board.py`: Defines the board layout and rules.
- `util.py`: Provides useful data structures for implementing search algorithms.

### Supporting Files
- `displays.py`: Handles the graphics for Blokus.
- `inputs.py`: Contains a random player and an interface for human interaction.
- `pieces.py`: Loads a list of game pieces from a file.

## Search Algorithms Implemented

1. **Depth First Search (DFS)**
   - Implemented in `depth_first_search` function in `search.py`.
   - Avoids expanding already visited states to ensure completeness.

2. **Breadth First Search (BFS)**
   - Implemented in `breadth_first_search` function in `search.py`.
   - Also avoids expanding already visited states.

3. **Uniform Cost Search (UCS)**
   - Implemented in `uniform_cost_search` function in `search.py`.

4. **A* Search**
   - Implemented in `a_star_search` function in `search.py`.
   - Uses heuristics for improved performance.

## Problem Definitions

1. **BlokusCornersProblem**
   - A search problem where the objective is to cover all corners of the board with minimal tiles.
   - Implemented in `blokus_problems.py`.

2. **BlokusCoverProblem**
   - A search problem aimed at covering all specified locations on the board.
   - Implemented in `blokus_problems.py`.

## Heuristics

### Blokus Corner Heuristic

**Expanded Nodes:** 2633, **Score:** 17

#### Valid Heuristic Explanation
1. **Infinity Norm Distance (Chebyshev Distance) Heuristic:**
   - **Objective:** Estimates the minimum number of moves required to reach all unreached corners from any filled position on the board.
   - **Admissibility and Consistency:** The heuristic is initialized with the board's perimeter value, an upper bound on the actual cost, ensuring it never overestimates the cost.
   - **Process:**
     1. Identify the board's corners and filter out those already reached.
     2. For each unreached corner, calculate the minimum infinity norm distance from any occupied cell to the corner.
     3. Return the overall minimum distance among all unreached corners.
   - **Proof of Admissibility:**
     - The heuristic ensures `h(state) ≤ h*(state)`, where `h(state)` is the heuristic function and `h*(state)` is the true minimum number of moves required.
     - The perimeter value serves as an upper bound, ensuring the heuristic remains admissible throughout the computation.

```python
def blokus_corners_heuristic(state, problem):
    corners = [(0, 0), (0, state.board_w - 1), (state.board_h - 1, 0), (state.board_h - 1, state.board_w - 1)]
    unreached_corners = [corner for corner in corners if state.state[corner[0]][corner[1]] == -1]
    if not unreached_corners:
        return 0
    perimeter = 2 * state.board_w + 2 * state.board_h
    min_moves = perimeter
    for corner in unreached_corners:
        min_distance = perimeter
        for row in range(state.board_h):
            for col in range(state.board_w):
                if state.state[row][col] != -1:
                    distance = max(abs(corner[0] - row), abs(corner[1] - col))
                    min_distance = min(min_distance, distance)
        min_moves = min(min_moves, min_distance)
    return min_moves
```

##Conclusion
This project demonstrates the application of various search algorithms to solve Blokus-based problems. The heuristics implemented help in improving the efficiency of the search process, and the project structure allows for easy experimentation and extension.


##Contributors
Raphael Haddad & Daniel Perretz
