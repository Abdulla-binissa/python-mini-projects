import sys, pygame
import PlayerData
import time

SQ_SIZE = 20


def main():
    width = 320
    height = 440

    size = width, height
    screen = pygame.display.set_mode(size)
    screen.fill("white")
    
    data = PlayerData.Data()
    notNow = int(time.time())

    while(True):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            elif event.type == pygame.KEYDOWN: # Arrow keys
                data.changeDirection(event.key)

        now = int(time.time()*10 % 60)
        if now != notNow:
            data.updatePlayerLocation()
            
            notNow = int(time.time()*10 % 60)

        drawState(screen, data)
        pygame.display.flip()

def addFood():
    # If there is no food
    
    return "hello"
    #add food randomly somehwere 

def drawState(screen, data):
    HEIGHT = screen.get_height()
    WIDTH = screen.get_width()

    left = (WIDTH / SQ_SIZE / 2) - (WIDTH / SQ_SIZE)
    right = (WIDTH / SQ_SIZE / 2 )
    top = (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE)
    bottom = (HEIGHT / SQ_SIZE / 2)

    for r in range( int(top) -1, int(bottom) +1):
        for c in range( int(left) -1, int(right) +1):

            padding, margin = 0.5, 4
            squareOuter = pygame.Rect(
                (right+c)*SQ_SIZE + padding, 
                (bottom+r)*SQ_SIZE + padding, 
                SQ_SIZE - 2*padding, 
                SQ_SIZE - 2*padding)
            squareInner = pygame.Rect(
                (right+c)*SQ_SIZE + padding + margin, 
                (bottom+r)*SQ_SIZE + padding + margin, 
                SQ_SIZE - 2*padding - 2*margin, 
                SQ_SIZE - 2*padding - 2*margin)

            pygame.draw.rect(screen, pygame.Color( "gray"), squareOuter)
            pygame.draw.rect(screen, pygame.Color( "white"), squareInner)

            if (r, c) in data.body:
                center = ((right+c)*SQ_SIZE + padding - (SQ_SIZE/2), (bottom+r)*SQ_SIZE + padding - (SQ_SIZE/2))
                pygame.draw.circle(screen, pygame.Color("black"), center, SQ_SIZE // 2.1)

            if (r,c) == data.food:
                center = ((right+c)*SQ_SIZE + padding - (SQ_SIZE/2), (bottom+r)*SQ_SIZE + padding - (SQ_SIZE/2))
                pygame.draw.circle(screen, pygame.Color("green"), center, SQ_SIZE // 2.1)



main()