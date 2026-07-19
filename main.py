from game import Game
import os


class TicTacToeApp:
    def __init__(self):
        self.game = Game()

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def banner(self):
        print("=" * 45)
        print("         TIC TAC TOE AI")
        print("      Powered by Minimax AI")
        print("=" * 45)

    def instructions(self):
        print("\nBoard Positions\n")
        print("1 | 2 | 3")
        print("--+---+--")
        print("4 | 5 | 6")
        print("--+---+--")
        print("7 | 8 | 9")
        print("\nYou are X")
        print("Computer is O\n")

    def menu(self):
        while True:
            self.clear()
            self.banner()

            print("\n1. Play Game")
            print("2. Instructions")
            print("3. Exit")

            choice = input("\nEnter choice: ")

            if choice == "1":
                self.game.play()

            elif choice == "2":
                self.clear()
                self.banner()
                self.instructions()
                input("\nPress Enter to continue...")

            elif choice == "3":
                print("\nGoodbye!")
                break

            else:
                input("\nInvalid choice. Press Enter...")


def main():
    app = TicTacToeApp()
    app.menu()


if __name__ == "__main__":
    main()
