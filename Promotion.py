    def __CreateBoard(self):
            for Row in range(1, self._NoOfRows + 1):
                for Column in range(1, self._NoOfColumns + 1):
                    if Row == 1 and Column == self._NoOfColumns // 2:
                        S = Kotla(self._Players[0], "K")
                    elif Row == self._NoOfRows and Column == self._NoOfColumns // 2 + 1:
                        S = Kotla(self._Players[1], "k")
                    elif (Row == 1 and Column == 1):
                        S = Promotion(self._Players[1], "p")
                    elif (Row == 1 and Column == self._NoOfColumns):
                        S = Promotion(self._Players[1], "p")
                    elif (Row == self._NoOfRows and Column == 1):
                        S = Promotion(self._Players[0], "p")
                    elif (Row == self._NoOfRows and Column == self._NoOfColumns):
                        S = Promotion(self._Players[0], "p")                          
                    else:
                        S = Square()
                    self._Board.append(S)

class Promotion(Square):
    def __init__(self, P, S):
        super(Promotion, self).__init__()
        self._BelongsTo = P
        self._Symbol = S    
    
    def SetPiece(self, P):
        if (P.GetBelongsTo().SameAs(self._BelongsTo)):
            if (P.GetSymbol() == "!"):
                self._PieceInSquare = Piece("mirza", self._BelongsTo, 5, "1")
            elif (P.GetSymbol() == '"'):
                self._PieceInSquare = Piece("mirza", self._BelongsTo, 5, "2")            
        else:
            self._PieceInSquare = P

    