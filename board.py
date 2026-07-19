class Board:
    def __init__(self):
        self.cells=[" "]*9

    def reset(self):
        self.cells=[" "]*9

    def display(self):
        for i in range(3):
            r=self.cells[i*3:(i+1)*3]
            print(f" {r[0]} | {r[1]} | {r[2]} ")
            if i<2: print("---+---+---")

    def move(self,pos,p):
        if 0<=pos<9 and self.cells[pos]==" ":
            self.cells[pos]=p
            return True
        return False

    def undo(self,pos):
        self.cells[pos]=" "

    def moves(self):
        return [i for i,v in enumerate(self.cells) if v==" "]

    def winner(self):
        w=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for a,b,c in w:
            if self.cells[a]!=" " and self.cells[a]==self.cells[b]==self.cells[c]:
                return self.cells[a]
        return None

    def full(self):
        return " " not in self.cells
