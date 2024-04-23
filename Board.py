import customtkinter as ctk
import tkinter as tk
from tkinter import font
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.entries = [[None for _ in range(width)] for _ in range(height)]
        self.draw()
    #
    def draw(self):
        entry_font = font.Font(size=12, weight='bold')
        call_size = min(self.width, self.height) // 9
        for row in range(9):
            for col in range(9):
                e = tk.Entry(self.screen, font=entry_font, width=2, justify='center')
                e.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
                self.entries[row][col] = e  # Store the entry for later use
        for i in range(9):
            self.screen.grid_columnconfigure(i, weight=1)
            self.screen.grid_rowconfigure(i, weight=1)

    def select(self, row, col):
        pass


    def click(self, x, y):
        pass


    def clear(self):
        pass


    def sketch(self):
        pass


    def place_number(self):
        pass


    def reset_to_original(self):
        pass


    def is_full(self):
        pass


    def update_board(self):
        pass


    def find_empty(self):
        pass


    def check_board(self):
        pass

