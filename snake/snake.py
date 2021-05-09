import sys, pygame
import PlayerData
import time

SQ_SIZE = 20


def main():
    pygame.init()
    width = 320
    height = 440
    score = 0
    highscore = 0

    size = width, height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Snake.py')
    font = pygame.font.Font('freesansbold.ttf', 20)
 
    scoreStr = 'Score: ' + str(score)
    scoreTxt = font.render(scoreStr, True, 'black')
    scoreTextRect = scoreTxt.get_rect()
    
    highscoreStr = 'Highscore: ' + str(highscore)
    highScoreTxt = font.render(highscoreStr, True, 'black')
    highscoreTextRect = highScoreTxt.get_rect()
    highscoreTextRect.right = width - 15
    

    screen.fill("white")
    
    data = PlayerData.Data()
    notNow = int(time.time())
    moved = False

    while(True):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            elif event.type == pygame.KEYDOWN and moved == False:
                data.changeDirection(event.key)
                moved = True 

        now = int(time.time()*10 % 60)
        if now != notNow:
            status = data.updatePlayerLocation()
            if status == 1:
                score += 1
            elif status == -1:
                score = 0
            
            if (highscore < score):
                highscore = score

            scoreStr = 'Score: ' + str(score)
            scoreTxt = font.render(scoreStr, True, 'black')
            highscoreStr = 'Highscore: ' + str(highscore)
            highscoreTxt = font.render(highscoreStr, True, 'black')

            moved = False
            
            notNow = int(time.time()*10 % 60)

        drawState(screen, data)
        screen.blit(scoreTxt, scoreTextRect)
        screen.blit(highscoreTxt, highscoreTextRect)
        pygame.display.flip()

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