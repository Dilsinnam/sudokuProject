import customtkinter as ctk
import tkinter as tk


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class SudokuUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.create_game_start_screen()
        self.create_game_end_screen()

    def create_game_start_screen(self):
        self.start_frame = ctk.CTkFrame(master=self.root)
        self.start_frame.pack(pady=20, padx=20, fill="both", expand=True)

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
        self.progress_bar.place(relx=0.5, rely=0.9, anchor="center")

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

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.start_frame.pack_forget()
        self.create_game_board()

    def reset_board(self):
        for row in self.cells:
            for cell in row:
                cell.set_cell_value(0)
        self.update_progress()

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
        self.row = row
        self.col = col
        self.screen = screen
        self.entry = ctk.CTkEntry(master=screen, width=40, height=40)
        self.entry.grid(row=row, column=col, padx=2, pady=2)
        self.selected = False

    def set_cell_value(self, value):
        self.value = value
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def set_sketched_value(self, value):

        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def draw(self):
        if self.selected:
            self.entry.configure(border_color="red")
        else:
            self.entry.configure(border_color="default")

        if self.value != 0:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.value)


if __name__ == "__main__":
    root = ctk.CTk()
    app = SudokuUI(root)
    root.mainloop()
