import pygame

class Player:

    def __init__(self):
        self.direction = 0  # up, right, down, left
        self.body = [(0,0), (0,1), (0,2)]


    def changeDirection(self, key):
        if key == pygame.K_w:
            self.direction = 0

        elif key == pygame.K_d:
            self.direction = 1

        elif key == pygame.K_s:
            self.direction = 2

        elif key == pygame.K_a:
            self.direction = 3


    def updateLocation(self):
        inFront = self.checkInFront()
        if inFront == "self":
            print('You lose!')

        head = self.body[0]
        if self.direction == 0:
            self.body.insert(0, (head[0] - 1 , head[1] + 0) )
        if self.direction == 1:
            self.body.insert(0, (head[0] + 0 , head[1] + 1) )
        if self.direction == 2:
            self.body.insert(0, (head[0] + 1 , head[1] + 0) )
        if self.direction == 3:
            self.body.insert(0, (head[0] + 0 , head[1] - 1) )

        if inFront != "food":
            self.body.pop( len(self.body) -1 )
    
    def checkInFront(self):
        return "empty"
