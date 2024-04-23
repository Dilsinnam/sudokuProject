import customtkinter as ctk
import tkinter as tk


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")


class SudokuUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.create_game_start_screen()

    def create_game_start_screen(self):
        self.start_frame = ctk.CTkFrame(
            master=self.root, fg_color="black", bg_color="red"
        )
        self.start_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(
            master=self.start_frame,
            text="Sudoku",
            font=("Roboto Medium", 18),
            text_color="white",
            fg_color="black",
        )
        self.title_label.pack(pady=12)

        button_style = {
            "fg_color": "black",
            "hover_color": "darkred",
            "text_color": "white",
        }
        self.easy_button = ctk.CTkButton(
            master=self.start_frame,
            text="Easy",
            command=lambda: self.start_game("easy"),
            **button_style
        )
        self.easy_button.pack(pady=8)

        self.medium_button = ctk.CTkButton(
            master=self.start_frame,
            text="Medium",
            command=lambda: self.start_game("medium"),
            **button_style
        )
        self.medium_button.pack(pady=8)

        self.hard_button = ctk.CTkButton(
            master=self.start_frame,
            text="Hard",
            command=lambda: self.start_game("hard"),
            **button_style
        )
        self.hard_button.pack(pady=8)

    def start_game(self, difficulty):
        self.start_frame.destroy()
        self.create_game_in_progress_screen(difficulty)

    def create_game_in_progress_screen(self, difficulty):
        self.game_frame = ctk.CTkFrame(master=self.root)
        self.game_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.board_canvas = tk.Canvas(
            master=self.game_frame, width=360, height=360, bg="white"
        )
        self.board_canvas.pack(pady=20)

        self.reset_button = ctk.CTkButton(
            master=self.game_frame, text="Reset", command=self.reset_board
        )
        self.reset_button.pack(side="left", padx=10)

        self.restart_button = ctk.CTkButton(
            master=self.game_frame, text="Restart", command=self.restart_game
        )
        self.restart_button.pack(side="left", padx=10)

        self.exit_button = ctk.CTkButton(
            master=self.game_frame, text="Exit", command=self.exit_game
        )
        self.exit_button.pack(side="left", padx=10)

    def reset_board(self):
        pass

    def restart_game(self):
        self.game_frame.destroy()
        self.create_game_start_screen()

    def exit_game(self):
        self.root.quit()


if __name__ == "__main__":
    root = ctk.CTk()
    app = SudokuUI(root)
    root.mainloop()
