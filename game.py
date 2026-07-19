from board import Board
from ai import AI

class Game:
    def __init__(self):
        self.board=Board()
        self.ai=AI()

    def play(self):
        print("Positions:")
        print("1|2|3\n4|5|6\n7|8|9\n")
        while True:
            self.board.display()
            try:
                p=int(input("Your move (1-9): "))-1
            except:
                continue
            if not self.board.move(p,"X"):
                continue
            if self.board.winner() or self.board.full():
                break
            m=self.ai.best_move(self.board)
            if m is not None:
                self.board.move(m,"O")
            if self.board.winner() or self.board.full():
                break
        self.board.display()
        w=self.board.winner()
        if w=="X":
            print("You win!")
        elif w=="O":
            print("Computer wins!")
        else:
            print("Draw!")
