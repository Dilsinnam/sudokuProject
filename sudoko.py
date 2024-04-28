import pygame
import sys
import random
import sudoku_generator

# Need to be able to edit user imputed cells
# Fix difficulty <DONE>
# Fix exit button
# Implement arrow keys <DONE>

WIDTH = 540
HEIGHT = 600
CELL_SIZE = WIDTH // 9


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

solved_board = sudoku_generator.generate_sudoku(9, 0)


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.selected = False
        self.screen = screen
        self.user_input = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE

        if self.selected:
            pygame.draw.rect(self.screen, RED, (x, y, CELL_SIZE, CELL_SIZE), 2)
        else:
            pygame.draw.rect(self.screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

        font = pygame.font.Font(None, 36)
        if self.value:
            text = font.render(str(self.value), True, BLACK)
            self.screen.blit(text, (x + CELL_SIZE // 3, y + CELL_SIZE // 3))
        elif self.sketched_value:
            text = font.render(str(self.sketched_value), True, GRAY)
            self.screen.blit(text, (x + 5, y + 5))


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = []
        self.initial_board = []
        self.generate_board()
        self.selected_cell = None
        self.selected_cell_position = None


    def generate_board(self):

        self.board = []
        for row in range(9):
            current_row = []
            current_row_initial = []
            for col in range(9):
                cell_value = solved_board[row][col]
                if self.difficulty == "easy" and random.randint(1, 81) >= 50:
                    cell_value = 0
                elif self.difficulty == "medium" and random.randint(1, 81) >= 40:
                    cell_value = 0
                elif self.difficulty == "hard" and random.randint(1, 81) >= 30:
                    cell_value = 0
                current_row.append(Cell(cell_value, row, col, self.screen))
                current_row_initial.append(cell_value)
            self.board.append(current_row)
            self.initial_board.append(current_row_initial)





    def draw(self):

        for row in range(10):
            line_thickness = 1 if row % 3 != 0 else 3
            pygame.draw.line(
                self.screen, BLACK, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), line_thickness
            )
        for col in range(10):
            line_thickness = 1 if col % 3 != 0 else 3
            pygame.draw.line(
                self.screen, BLACK, (col * CELL_SIZE, 0), (col * CELL_SIZE, HEIGHT - 60), line_thickness
            )
        # Draw the cells
        for row in self.board:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.board[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):
        if 0 <= x < WIDTH and 0 <= y < HEIGHT - 60:
            return (y // CELL_SIZE, x // CELL_SIZE)
        return None

    def sketch(self, value):
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                if self.initial_board[i][j] != self.board[i][j].value or self.initial_board[i][j] == 0:
                    self.board[i][j].set_cell_value(0)
                    self.board[i][j].set_sketched_value(0)

    def is_full(self):
        for row in self.board:
            for cell in row:
                if not cell.value:
                    return False
        return True

    def check_board(self):

        for row in range(9):
            for col in range(9):
                if self.board[row][col].value != solved_board[row][col]:
                    return False
        return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()

    game_start = True
    game_in_progress = False
    game_over = False
    difficulty = None
    board = None

    while True:
        screen.fill(WHITE)

        if game_start:
            font = pygame.font.Font(None, 74)
            text = font.render("Sudoku", True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))
            # Difficulty buttons
            font = pygame.font.Font(None, 36)
            text_easy = font.render("Easy", True, BLACK)
            text_medium = font.render("Medium", True, BLACK)
            text_hard = font.render("Hard", True, BLACK)
            screen.blit(text_easy, (WIDTH // 4 - text_easy.get_width() // 2, HEIGHT // 2))
            screen.blit(text_medium, (WIDTH // 2 - text_medium.get_width() // 2, HEIGHT // 2))
            screen.blit(text_hard, (3 * WIDTH // 4 - text_hard.get_width() // 2, HEIGHT // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if (WIDTH // 4 - text_easy.get_width() // 2) <= x <= (WIDTH // 4 + text_easy.get_width() // 2) and \
                       (HEIGHT // 2) <= y <= (HEIGHT // 2 + 36):
                        difficulty = "easy"
                        game_start = False
                        game_in_progress = True
                    elif (WIDTH // 2 - text_medium.get_width() // 2) <= x <= (WIDTH // 2 + text_medium.get_width() // 2) and \
                         (HEIGHT // 2) <= y <= (HEIGHT // 2 + 36):
                        difficulty = "medium"
                        game_start = False
                        game_in_progress = True
                    elif (3 * WIDTH // 4 - text_hard.get_width() // 2) <= x <= (3 * WIDTH // 4 + text_hard.get_width() // 2) and \
                       (HEIGHT // 2) <= y <= (HEIGHT // 2 + 36):
                        difficulty = "hard"
                        game_start = False
                        game_in_progress = True

            if not game_start:
                board = Board(WIDTH, HEIGHT - 60, screen, difficulty)

        elif game_in_progress:
            board.draw()
            font = pygame.font.Font(None, 36)
            text_reset = font.render("Reset", True, BLACK)
            screen.blit(text_reset, (10, HEIGHT - 50))
            text_restart = font.render("Restart", True, BLACK)
            screen.blit(text_restart, (WIDTH // 2 - text_restart.get_width() // 2, HEIGHT - 50))
            # Exit button
            text_exit = font.render("Exit", True, BLACK)
            screen.blit(text_exit, (WIDTH - text_exit.get_width() // 2, HEIGHT - 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if y < HEIGHT - 60:
                        board.selected_cell_position = list(board.click(x, y))
                        if board.selected_cell_position:
                            board.select(board.selected_cell_position[0], board.selected_cell_position[1])
                    else:
                        if (10 <= x <= 10 + text_reset.get_width()) and \
                                (HEIGHT - 50 <= y <= HEIGHT - 50 + 36):
                            board.reset_to_original()
                        elif (WIDTH // 2 - text_restart.get_width() // 2 <= x <= WIDTH // 2 + text_restart.get_width() // 2) and \
                                (HEIGHT - 50 <= y <= HEIGHT - 50 + 36):
                            game_in_progress = False
                            game_start = True
                            difficulty = None
                            board = None
                        elif (WIDTH - text_exit.get_width() // 2 <= x <= WIDTH) and \
                                (HEIGHT - 50 <= y <= HEIGHT - 50 + 36):
                            pygame.quit()
                            sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if board.selected_cell:
                        if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                         pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                            value = int(pygame.key.name(event.key))
                            board.sketch(value)
                        elif event.key == pygame.K_RETURN:
                            value = board.selected_cell.sketched_value
                            if value:
                                board.place_number(value)
                            if board.is_full():
                                if board.check_board():
                                    game_in_progress = False
                                    game_start = False
                                    game_over = True
                                else:
                                    game_in_progress = False
                                    game_start = False
                                    game_over = True

                        # Arrow Keys movement
                        elif event.key == pygame.K_UP:
                            board.selected_cell_position[0] -= 1
                            board.select(board.selected_cell_position[0], board.selected_cell_position[1])

                        elif event.key == pygame.K_DOWN:
                            board.selected_cell_position[0] += 1
                            board.select(board.selected_cell_position[0], board.selected_cell_position[1])

                        elif event.key == pygame.K_LEFT:
                            board.selected_cell_position[1] -= 1
                            board.select(board.selected_cell_position[0], board.selected_cell_position[1])

                        elif event.key == pygame.K_RIGHT:
                            board.selected_cell_position[1] += 1
                            board.select(board.selected_cell_position[0], board.selected_cell_position[1])

        elif game_over:
            font = pygame.font.Font(None, 74)
            if board.check_board():
                text = font.render("You Win!", True, BLACK)
            else:
                text = font.render("Game Over!", True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

            font = pygame.font.Font(None, 36)

            text_restart = font.render("Restart", True, BLACK)
            screen.blit(text_restart, (WIDTH // 2 - text_restart.get_width() // 2, HEIGHT - 50))

            text_exit = font.render("Exit", True, BLACK)
            screen.blit(text_exit, (WIDTH - text_exit.get_width() // 2, HEIGHT - 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if (WIDTH // 2 - text_restart.get_width() // 2 <= x <= WIDTH // 2 + text_restart.get_width() // 2) and \
                            (HEIGHT - 50 <= y <= HEIGHT - 50 + 36):
                        game_in_progress = False
                        game_start = True
                        difficulty = None
                        board = None
                        game_over = False
                    elif (WIDTH - text_exit.get_width() // 2 <= x <= WIDTH) and \
                            (HEIGHT - 50 <= y <= HEIGHT - 50 + 36):
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()

