import pygame, random

class Data:

    def __init__(self):
        self.direction = (0,-1)  #
        self.body = [(0,0), (0,1), (0,2)]
        self.food = (5,5)

    def changeDirection(self, key):
        # Add restrictions from going backwards
        if key == pygame.K_w and self.direction != (1, 0): 
            self.direction =  (-1,0)

        elif key == pygame.K_d and self.direction != (0, -1): # right
            self.direction =  (0,1)

        elif key == pygame.K_s and self.direction != (-1, 0): # down
            self.direction =  (1,0)

        elif key == pygame.K_a and self.direction != (0, 1): # left
            self.direction =  (0,-1)

    def updatePlayerLocation(self):
        inFrontCheck = self.checkInFront()

        inFront = (self.body[0][0] + self.direction[0] , self.body[0][1] + self.direction[1])
        self.body.insert( 0, inFront)

        if inFrontCheck == "self":
            self.restart()
            return -1

        elif inFrontCheck == "food":
            # Randomly sets food somewhere
            self.food = self.addFood()
            return 1

        else:
            self.body.pop( len(self.body) -1 )
            return 0
    
    def checkInFront(self):
        squareInFront = (self.body[0][0] + self.direction[0] , self.body[0][1] + self.direction[1])
        
        if squareInFront == self.food:
            return "food"
        
        elif self.body.__contains__(squareInFront):
            return "self"

        elif squareInFront[0] == -11 or squareInFront[0] == 12:
            return "self"
        
        elif squareInFront[1] == -8 or squareInFront[1] == 9:
            return "self"

        else: 
            return "empty"

    def addFood(self):
        # Random point not in body
        newFood = ( random.randint(-10, 11), random.randint(-7, 8) )
        while( self.body.__contains__(newFood) ):
            newFood = ( random.randint(-10, 11), random.randint(-7, 8) )
            
        return newFood

    def restart(self):
        self.direction = (0,-1)  
        self.body = [(0,0), (0,1), (0,2)]
        self.food = (5,5)