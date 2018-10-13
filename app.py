from pygame import *
import menu #import the menu
import random   #import random

from classes import *   #import from the file classes




def run_game():
    """game play interface"""
    screen = pygame.display.set_mode((800, 600))    #the widht of the display for the game
    display.set_caption("Jet mission")              #set the title of the game


    scores = 0                          #the score starts from 0
    theClock = pygame.time.Clock()
    bg_image = Star_bg("star.gif")      #call the star image into the game

    #coordinate of moving background
    x = 0
    y = 0
    x1 = bg_image.width
    y1 = 0

    pygame.init()       #initialize pygame


    #creating a jet
    jet1 = Jet(screen)
    Jet_sprites = Group(jet1)

    #create asteroid object group
    asteroid_group = Group()

    #create bullets object Group
    bullets = Group()



    Fps = 60
    asteroid_timer = pygame.time.get_ticks()
    while True:
        theClock.tick(Fps)
        Fps += 0.01#game phase goes faster after every frame

        """background move"""

        x -= 5
        x1 -= 5
        bg_image.draw(screen,x,y)
        bg_image.draw(screen,x1, y1)    #spawn the asteroids
        if x < -bg_image.width:
            x = 0
        if x1 < 0:
            x1 = bg_image.width

        # create score board
        font=pygame.font.SysFont("Times New Romans",36)
        score_board=font.render("score:"+str(scores),True,(255,255,255))
        # update refered to the word's method
        screen.blit(score_board,(10,550))



        Jet_sprites.draw(screen)    #to make the jet in the screen

        bullets.draw(screen)        #to make the bullets in the screen

        asteroid_group.draw(screen) #to make the asteroid in the screen
        display.update()#update jet and screen view

        event.get()
        """moving the jet according to key pressed"""

        key = pygame.key.get_pressed()
        if key[K_LEFT] and jet1.rect.x>0:       #moves the jet to the left, and if it is not over the screen
            jet1.moveleft()                     #moves the jet to the left

        if key[K_RIGHT] and jet1.rect.x<=700:   #moves the jet to the right, and if it is not over the right screen
            jet1.moveright()

        if key[K_DOWN] and jet1.rect.y<=500:    #moves the jet downwards, and if it is not over the screen
            jet1.movedown()

        if key[K_UP] and jet1.rect.y>0:         #moves the jet upwards, and if it is not over the screen
            jet1.moveup()

        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000):
            bullet = Bullet(screen, jet1.rect.x+50, jet1.rect.y+42)     #set the bullets spawning place when space is pressed
            bullets.add(bullet)     #add the bullets
            pygame.mixer.music.load("LaserBlast.wav")   #make a sound every time you shoot
            pygame.mixer.music.play()       #play the sound

        if key[K_ESCAPE]:
            menu.menu_screen(Button,run_game)   #press escape to go back to the menu screen, and run the main menu to start the game again if wanted

        if key[K_p]:
            menu.pause_menu(Button,run_game)    #press p to pause the game, and run the pause menu


        """generate asteroid randomly"""
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            asteroid = Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20))    #set the spawn place for the asteroid random
            asteroid_group.add(asteroid)        #add the variable asteroid to asteroid group
            asteroid_timer = pygame.time.get_ticks()

        """update the movement of asteroid"""
        for asteroid in asteroid_group:
            asteroid.movement()             #movement for asteroids
            if asteroid.rect.right <= 0:    #if the asteroid moves to the left of the screen and didnt hit
                asteroid_group.remove(asteroid) #remove after screen
            if groupcollide(Jet_sprites,asteroid_group,dokilla=True,dokillb=True):#collition check
                menu.lose_menu(Button,run_game,scores)  #if the jet touches the asteroid, it goes to the lose menu and shows the score and ask if you want to play again

        """update bullet movement on screen"""
        for bullet in bullets:
            bullet.movement()       #movements for bullets
            if bullet.rect.left > 800:      #if the bullet goes further than the screen of the right, it is removed
                bullets.remove(bullet)      #removes bullet
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):
                scores += 100       #if the bullet touches the asteroid, the score will be up by 100

menu.menu_screen(Button,run_game)   #TO RUN THE GAME

#---------------SPECIAL THANKS to Pier,Excel,georgius,William,Nicander,Nicolas,Andy,Guntur,Adrian-----------------------
"""Acknowledgement:
LaserBlast.wav(shooting sound) http://soundbible.com/472-Laser-Blasts.html
"""
