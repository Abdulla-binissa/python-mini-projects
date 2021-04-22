import pygame

class Data:

    def __init__(self):
        self.direction = (0,-1)  #
        self.body = [(0,0), (0,1), (0,2), (0,3), (0,4)]
        self.food = (5,5)

    def changeDirection(self, key):
        # Add restrictions from going backwards
        if key == pygame.K_w:   # up
            self.direction =  (-1,0)

        elif key == pygame.K_d: # right
            self.direction =  (0,1)

        elif key == pygame.K_s: # down
            self.direction =  (1,0)

        elif key == pygame.K_a: # left
            self.direction =  (0,-1)

    def updatePlayerLocation(self):
        inFrontCheck = self.checkInFront()
        if inFrontCheck == "self":
            print('You lose!')

        inFront = (self.body[0][0] + self.direction[0] , self.body[0][1] + self.direction[1])
        self.body.insert( 0, inFront)

        # if self.direction == 0:
        #     self.body.insert(0, (head[0] - 1 , head[1] + 0) )
        # if self.direction == 1:
        #     self.body.insert(0, (head[0] + 0 , head[1] + 1) )
        # if self.direction == 2:
        #     self.body.insert(0, (head[0] + 1 , head[1] + 0) )
        # if self.direction == 3:
        #     self.body.insert(0, (head[0] + 0 , head[1] - 1) )

        if inFrontCheck != "food":
            self.body.pop( len(self.body) -1 )

        else:
            self.food = (7,7)
    
    def checkInFront(self):
        inFront = (self.body[0][0] + self.direction[0] , self.body[0][1] + self.direction[1])
        
        if inFront == self.food:
            return "food"
        
        elif self.body.__contains__(inFront):
            return "self"

        else: 
            return "empty"
