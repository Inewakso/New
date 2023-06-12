import copy 

    def PrintMoves(self,Choice,StartSquareRef):
        PossibleMoves =[]
        tempBoard = copy.deepcopy(self._Board)
        for row in range(1,self._NoOfRows+1):
            for col in range(1,self._NoOfColumns+1):
                tRef = row*10+col  
                if self.__CheckSquareIsValid(tRef,False):
                    if self._CurrentPlayer.CheckPlayerMove(Choice, StartSquareRef, tRef):
                        PossibleMoves.append(tRef)
        print("Possible moves are: ")
        for ref in PossibleMoves:
            print(ref,end=" ")
            self._Board[self.__GetIndexOfSquare(ref)].SetPiece(Piece("m",self._CurrentPlayer,0,"m"))
        print("")
        self.__DisplayBoard()
        self._Board = copy.deepcopy(tempBoard)

    def PlayGame(self):
        GameOver = False
        while not GameOver:
            self.__DisplayState()
            SquareIsValid = False
            Choice = 0
            while Choice < 1 or Choice > 3:
                Choice = int(input("Choose move option to use from queue (1 to 3) or 9 to take the offer: "))
                if Choice == 9:
                    self.__UseMoveOptionOffer()
                    self.__DisplayState()
            while not SquareIsValid:
                StartSquareReference = self.__GetSquareReference("containing the piece to move")
                SquareIsValid = self.__CheckSquareIsValid(StartSquareReference, True)
            self.PrintMoves(Choice,StartSquareReference)
            SquareIsValid = False
            while not SquareIsValid:
                FinishSquareReference = self.__GetSquareReference("to move to")
                SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False)
            MoveLegal = self._CurrentPlayer.CheckPlayerMove(Choice, StartSquareReference, FinishSquareReference)
            if MoveLegal:
                PointsForPieceCapture = self.__CalculatePieceCapturePoints(FinishSquareReference)
                self._CurrentPlayer.ChangeScore(-(Choice + (2 * (Choice - 1))))
                self._CurrentPlayer.UpdateQueueAfterMove(Choice)
                self.__UpdateBoard(StartSquareReference, FinishSquareReference)
                self.__UpdatePlayerScore(PointsForPieceCapture)
                print("New score: " + str(self._CurrentPlayer.GetScore()) + "\n")
            if self._CurrentPlayer.SameAs(self._Players[0]):
                self._CurrentPlayer = self._Players[1]
            else:
                self._CurrentPlayer = self._Players[0]
            GameOver = self.__CheckIfGameOver()
        self.__DisplayState()
        self.__DisplayFinalResult()