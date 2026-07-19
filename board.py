class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.cells = [" " for _ in range(9)]

    def display(self):
        print("\n")
        for i in range(3):
            row = self.cells[i * 3:(i + 1) * 3]
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            if i < 2:
                print("---+---+---")
        print()

    def display_positions(self):
        print("\n")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")
        print()

    def is_valid_move(self, position):
        if position < 0 or position > 8:
            return False
        return self.cells[position] == " "

    def make_move(self, position, player):
        if self.is_valid_move(position):
            self.cells[position] = player
            return True
        return False

    def undo_move(self, position):
        self.cells[position] = " "

    def available_moves(self):
        return [i for i in range(9) if self.cells[i] == " "]

    def is_full(self):
        return " " not in self.cells

    def check_winner(self):
        winning_patterns = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for pattern in winning_patterns:
            a, b, c = pattern
            if (
                self.cells[a] == self.cells[b] ==
                self.cells[c] != " "
            ):
                return self.cells[a]

        return None

    def game_over(self):
        return self.check_winner() is not None or self.is_full()

    def get_cell(self, position):
        return self.cells[position]

    def set_cell(self, position, value):
        self.cells[position] = value

    def copy(self):
        new_board = Board()
        new_board.cells = self.cells.copy()
        return new_board

    def print_result(self):
        winner = self.check_winner()

        if winner == "X":
            print("\nYou Win!\n")

        elif winner == "O":
            print("\nComputer Wins!\n")

        else:
            print("\nIt's a Draw!\n")

    def board_state(self):
        return self.cells.copy()

    def __str__(self):
        text = ""
        for i in range(9):
            text += self.cells[i]
            if (i + 1) % 3 == 0:
                text += "\n"
        return text
