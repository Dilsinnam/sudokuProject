import customtkinter as ctk
import tkinter as tk
import math, random
# User can only enter a single digit, need to implement sketched values (LOOK AT PDF)
# need to allow user to select cells via mouse and arrow keys and have a border around the cell to let user know
# Add border around board and so that 3x3 subgrids are visible
# Need Win and Lose still


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class SudokuUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.initial_board = None
        self.cells = []
        self.create_game_start_screen()
        self.create_game_end_screen()

    def create_game_start_screen(self):
        self.start_frame = ctk.CTkFrame(master=self.root)
        self.start_frame.pack(pady=180, padx=180, fill="both", expand=True)

        title_label = ctk.CTkLabel(
            master=self.start_frame, text="Sudoku", font=("Roboto", 18)
        )
        title_label.pack(pady=12)

        self.easy_button = ctk.CTkButton(
            master=self.start_frame,
            text="Easy",
            command=lambda: self.set_difficulty("easy"),
            font=("Roboto", 10),
        )
        self.easy_button.pack(pady=8)
        self.medium_button = ctk.CTkButton(
            master=self.start_frame,
            text="Medium",
            command=lambda: self.set_difficulty("medium"),
            font=("Roboto", 10),
        )
        self.medium_button.pack(pady=8)
        self.hard_button = ctk.CTkButton(
            master=self.start_frame,
            text="Hard",
            command=lambda: self.set_difficulty("hard"),
            font=("Roboto", 10),
        )
        self.hard_button.pack(pady=8)

    def create_game_end_screen(self):
        self.end_frame = ctk.CTkFrame(master=self.root)

        self.end_label = ctk.CTkLabel(
            master=self.end_frame, text="Game Over", font=("Roboto", 18)
        )
        self.end_label.pack(pady=12)

        self.play_again_button = ctk.CTkButton(
            master=self.end_frame,
            text="Play Again",
            command=self.restart_game,
            font=("Roboto", 10),
        )
        self.play_again_button.pack(pady=8)

    def display_game_end_screen(self):
            self.end_frame.pack_forget()
            self.lose_label = ctk.CTkLabel(
                master=self.root, text="Game Over! Try again!", font=("Roboto", 18)
            )
            self.lose_label.pack(pady=12)
            self.play_again_button.pack(pady=8)
            self.exit_button.pack(pady=8)

    def display_win_screen(self):
        self.end_frame.pack_forget()
        self.win_label = ctk.CTkLabel(
            master=self.root, text="Congratulations! You've won!", font=("Roboto", 18)
        )
        self.win_label.pack(pady=12)
        self.play_again_button.pack(pady=8)
        self.exit_button.pack(pady=8)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.start_frame.pack_forget()
        self.create_game_board()
        if difficulty == "easy":
            removed_cells = 30
        elif difficulty == "medium":
            removed_cells = 40
        elif difficulty == "hard":
            removed_cells = 50
        else:
            removed_cells = 30
        board = SudokuGenerator.generate_sudoku(9, removed_cells)
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    self.cells[i][j].set_cell_value(board[i][j])
        self.initial_board = board

    def create_game_board(self):
        self.board_frame = ctk.CTkFrame(master=self.root)
        self.board_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.cells = [
            [Cell(0, i, j, self.board_frame) for j in range(9)] for i in range(9)
        ]

        self.reset_button = ctk.CTkButton(
            master=self.board_frame,
            text="Reset",
            command=self.reset_board,
            font=("Roboto", 10),
        )
        self.reset_button.grid(row=10, column=0, columnspan=3, pady=8)
        self.restart_button = ctk.CTkButton(
            master=self.board_frame,
            text="Restart",
            command=self.restart_game,
            font=("Roboto", 10),
        )
        self.restart_button.grid(row=10, column=3, columnspan=3, pady=8)
        self.exit_button = ctk.CTkButton(
            master=self.board_frame,
            text="Exit",
            command=self.exit_game,
            font=("Roboto", 10),
        )
        self.exit_button.grid(row=10, column=6, columnspan=3, pady=8)

        self.progress_bar = ctk.CTkProgressBar(master=self.root, width=200)
        self.progress_bar.place(relx=0.5, rely=0.95, anchor="center")

    def reset_board(self):
        if self.initial_board is not None:
            for i in range(9):
                for j in range(9):
                    if self.initial_board[i][j] != 0:
                        self.cells[i][j].set_cell_value(self.initial_board[i][j])
                    else:
                        self.cells[i][j].set_cell_value(0)


    def restart_game(self):
        self.board_frame.pack_forget()
        self.end_frame.pack_forget()
        self.create_game_start_screen()
        self.update_progress()

    def exit_game(self):
        self.root.destroy()

    def update_progress(self):
        total_cells = 81
        filled_cells = sum(1 for row in self.cells for cell in row if cell.value != 0)
        progress = filled_cells / total_cells
        self.progress_bar.set(progress)


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketch_value = None
        self.row = row
        self.col = col
        self.screen = screen
        self.entry = ctk.CTkEntry(master=screen, width=40, height=40, justify='center')
        self.entry.grid(row=row, column=col, padx=2, pady=2)
        self.selected = False
        self.entry.configure(validate="key")
        self.entry.bind("<Key>", self.validate_input)

    def validate_input(self, new_value):
        current_value = self.entry.get()
        if new_value.char.isdigit() and 1 <= int(new_value.char) <= 9:
            return True
        else:
            return False

    def submit_guess(self, event):
        if self.sketch_value is None:
            self.value = self.sketch_value
            self.sketch_value = None
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.value)
            self.entry.config(state="disabled")

    def set_cell_value(self, value):
        self.value = value
        if value == 0:
            self.entry.delete(0, tk.END)
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, value)
            self.entry.configure(state="disabled")

    def set_random_value(self):
        self.value = random.randint(1, 9)
        self.entry.insert(0, self.value)

    def draw(self):
        if self.selected:
            self.entry.configure(border_color="red")
        else:
            self.entry.configure(border_color="default")

        if self.value != 0:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.value)

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.grid = [[0] * row_length for _ in range(row_length)]

    def get_board(self):
        return self.grid

    def print_board(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def valid_in_row(self, row, num):
        return num not in self.grid[row]

    def valid_in_col(self, col, num):
        return all(self.grid[i][col] != num for i in range(self.row_length))

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.grid[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (
            self.valid_in_row(row, num)
            and self.valid_in_col(col, num)
            and self.valid_in_box(row - row % 3, col - col % 3, num)
        )

    def fill_box(self, row_start, col_start):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                while True:
                    num = nums.pop()
                    if self.is_valid(row_start + i, col_start + j, num):
                        self.grid[row_start + i][col_start + j] = num
                        break

    def fill_remaining(self, row, col):
        if col >= self.row_length:
            row += 1
            col = 0
        if row >= self.row_length:
            return True

        if self.grid[row][col] != 0:
            return self.fill_remaining(row, col + 1)

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.grid[row][col] = 0  # Reset the value if filling remaining fails
        return False  # No solution found

    def fill_values(self):
        self.fill_remaining(0, 0)

    def remove_cells(self):
        count = self.removed_cells
        while count != 0:
            cell_num = random.randint(0, self.row_length * self.row_length - 1)
            row = cell_num // self.row_length
            col = cell_num % self.row_length
            if self.grid[row][col] != 0:
                count -= 1
                self.grid[row][col] = 0

    @staticmethod
    def generate_sudoku(size, removed):
        sudoku = SudokuGenerator(size, removed)
        sudoku.fill_values()
        sudoku.remove_cells()
        return sudoku.get_board()


if __name__ == "__main__":
    root = ctk.CTk()
    app = SudokuUI(root)
    root.mainloop()
