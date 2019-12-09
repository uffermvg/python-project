import pygame, random, math
from pygame import mixer


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('game')
icon = pygame.image.load('skull.png')
pygame.display.set_icon(icon)

dead = pygame.image.load('dead.png')
rib = pygame.image.load('win.png')

mixer.music.load('music.ogg')
mixer.music.play(-1)

font = pygame.font.Font('freesansbold.ttf',32)
textx = 100
texty = 100

win_con = False

def win():
    wintext = font.render('You Win!!!!',True,(255,255,255))
    screen.blit(wintext, (500,300))
    screen.blit(rib, (400,300))
    
def lose():
    losetext = font.render('You have lost',True,(255,255,255))
    screen.blit(losetext, (500,300))
    screen.blit(dead, (400,300))

lives = 3

#images
finish = pygame.image.load('finish.png')
standing = pygame.image.load('standing.png')
player_right = pygame.image.load('player_right.png')
player_left = pygame.image.load('player_left.png')
jump = pygame.image.load('jump.png')
push = pygame.image.load('wall_left.png')
life = pygame.image.load('skull.png')
heart = pygame.image.load('heart.png')
grass = pygame.image.load('grass.png')
rec = pygame.image.load('large_rec.png')

player = standing

#player stats
playerx = 370
playery = 480
playerx_change = 0
playery_change = 0

jumping = False

#enemy stats
spikes = pygame.image.load('spikes.png')
spikesx = 500
spikesy = 485
enemyx_change = 1

#color variables
R = 0
G = 0
B = 255

def playerdraw(x,y):
    screen.blit(player, (x,y))

def enemydraw(x,y,enemy):
    
    screen.blit(enemy, (x,y))

def finishdraw():
    screen.blit(finish, (700,480))
def clouddraw(x,y, img):
    screen.blit(img, (x,y))

def drawlives (lives):
    c = 0
    x = 1
    while (c < lives):
        x = x + 50
        screen.blit(heart, (x,10))
        c+=1
def drawground():
    c = 1
    
    while(c < 800):
        clouddraw(c,472,grass)
        
        c += 50
        

c = 0
q = 1
running = True
while running:
    
    screen.fill((R,G,B))
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -1
                player = player_left
                playery = 480
                
            if event.key == pygame.K_RIGHT:
                playerx_change = 1
                player = player_right
                playery = 480
                
            if event.key == pygame.K_UP:
                playery -=  50
                playery_change = 9
                playerx = playerx + 50
                player = jump
                playerx_change = 0
                jumping = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP:
                playerx_change = 0
                player = standing
                playery = 480
    if spikesx >=750:
        enemyx_change = -.5 * q
    if spikesx <= 10:
        enemyx_change = .5 * q
    spikesx += enemyx_change        
    playerx += playerx_change
    
    if jumping == True:
        c+= 1
        if c == 5:
            jumping = False
            playery += 50
            
    if playerx > 800:
        playerx = 1
        if(((B - 50) > 0 or (R + 50) < 255) and playery < 2000):
            B -= 50
            R += 50
            q += 1
            enemyx_change = .5 * q
            numspikes = random.randint(0,5)
            spikesx =random.randint(5,750)
        else:
            player = push
            playerx = 1
            
    if playerx < 0:
        playerx = 799
        if(((B + 50) < 255 or (R - 50) > 255) and playery < 2000):
            B += 50
            R -= 50
            q -= 1
            enemyx_change = .5 * q
            numspikes = random.randint(0,5)
            spikesx =random.randint(5,750)
            
        else:
            player = push
            playerx = 1
            
    if R+50 > 255:
        finishdraw()

    if((int(playerx) == int(spikesx) and int(playery) == spikesy - 5) ):
        playerx = 1
        screen.fill((255,0,0))
        lives-=1
        q = 1
        enemyx_change = .5
        R = 0
        B = 255
    if lives <= 0:
        spikesy = 2000
        playery = 2000
        lose()
        
        
    
    if((int(playerx) == 700 and R + 50 >= 255)):
       
       win_con = True
    if win_con:
        win()
        spikesy = 2000
        playery = 2000
       
    drawground()
    clouddraw(-10,470,rec)
    clouddraw(485,470,rec)
    drawlives(lives)
    playerdraw(playerx,playery)
    enemydraw(spikesx,spikesy,spikes)
    
    pygame.display.update()
    
pygame.quit()    
    

    
    
