# Sudoku Project

## Overview
This project implements a **Sudoku** solver and generator in Python. The Sudoku solver takes an incomplete Sudoku grid and solves it using a backtracking algorithm. The generator, on the other hand, creates new Sudoku puzzles of varying difficulties.

## Features
- **Sudoku Solver**: Uses backtracking to solve a 9x9 Sudoku puzzle.
- **Sudoku Generator**: Generates Sudoku puzzles with different levels of difficulty.
- **User Interface (CLI)**: Command-line interface for easy interaction with the program.

## File Descriptions
### `sudoko.py`
This file contains the implementation of the Sudoku solver. It can take a 9x9 grid of numbers, with zeros representing empty cells, and solve the puzzle using a recursive backtracking algorithm.

**Main Functions:**
- `solve_sudoku(grid)`: Solves the Sudoku puzzle using backtracking.
- `is_valid(grid, row, col, num)`: Checks if placing a number at a given position is valid according to Sudoku rules.
- `print_grid(grid)`: Prints the Sudoku grid in a user-friendly format.

### `sudoku_generator.py`
This file generates Sudoku puzzles by first creating a fully solved grid, then removing numbers to create an incomplete puzzle. It also allows for different difficulty levels by controlling how many numbers are removed.

**Main Functions:**
- `generate_sudoku(difficulty)`: Generates a Sudoku puzzle of a specified difficulty.
- `remove_numbers_from_grid(grid, difficulty)`: Removes a certain number of cells based on the difficulty level.
  
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dilsinnam/sudokuProject.git

2. Navigate to the project directory:
    ```bash
    cd sudokuProject

3. Ensure you have Python installed (preferably version 3.6+). You can install any required dependencies (if any) using:
    ```bash
    pip install -r requirements.txt

## Usage

**Solving a Sudoku Puzzle**
1. Prepare a 9x9 grid with zeros representing empty cells.
2. Run the solver:
    ```bash
    python sudoko.py

3. Follow the prompts to enter the puzzle, and the solver will output the solution.

## Generating a Sudoku Puzzle

1. Run the generator:
    ```bash
    python sudoku_generator.py
    
2. Choose a difficulty level and a new puzzle will be printed.

## Example

Sample input for the Sudoku solver:

    5 3 0 0 7 0 0 0 0
    6 0 0 1 9 5 0 0 0
    0 9 8 0 0 0 0 6 0
    8 0 0 0 6 0 0 0 3
    4 0 0 8 0 3 0 0 1
    7 0 0 0 2 0 0 0 6
    0 6 0 0 0 0 2 8 0
    0 0 0 4 1 9 0 0 5
    0 0 0 0 8 0 0 7 9


