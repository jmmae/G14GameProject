class LevelHandler:
    def __init__(self):
        self.levelInstructions = #instruction screen
        self.levelCongrats = # level complete screen
        self.levelHolder = # array to store level objects??
        self.levelBoundary = 5
    def updateLevel(self,player):
        #display instructionscreen
        if player.getStarCount == self.levelBoundary:
            #displaylevelCongrats.
            #updateLevel
            self.levelBoundary+= 5
        #in interaction class, if player.starlevel == x: grab new level from array and load
