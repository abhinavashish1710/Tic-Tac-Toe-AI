class AI:
    def best_move(self,board):
        best_score=-10
        move=None
        for m in board.moves():
            board.move(m,"O")
            score=self.minimax(board,False)
            board.undo(m)
            if score>best_score:
                best_score=score
                move=m
        return move

    def minimax(self,board,maximizing):
        w=board.winner()
        if w=="O": return 1
        if w=="X": return -1
        if board.full(): return 0

        if maximizing:
            best=-10
            for m in board.moves():
                board.move(m,"O")
                best=max(best,self.minimax(board,False))
                board.undo(m)
            return best
        else:
            best=10
            for m in board.moves():
                board.move(m,"X")
                best=min(best,self.minimax(board,True))
                board.undo(m)
            return best
