from pygame import *
import sys
import pygame

def menu_screen(Button,run_game):
    """make the screen for menu"""
    display.set_caption("Jet Mission")  #set the title
    screen = pygame.display.set_mode((800, 600))    #set the display width
    #object button for quit and start
    start_button = Button("New Piskel.png")     #add the image for starting the game
    quit_button = Button("quit button.png")     #add the image to quit the game
    #image for the menu's backgound
    bg_image=pygame.image.load("asteroid_wall.jpg")     #load the background image
    bg_image=pygame.transform.scale(bg_image, (800, 600))       #scale the image for the background


    pygame.init()

    while True:
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))  #set the rect when it starts
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))  #set the rec when the game ends
        screen.blit(bg_image,(0,0)) #set the bg image

        screen.blit(start_button.button,(250,200))  #set the size of the start button
        screen.blit(quit_button.button,(250,300))   #set the size fo the quit button

        ev=event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):    #run the game if the mouse click start game
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):     #quit the game if the mouse clich quit game
                sys.exit()

        if ev.type == QUIT: #if the mouse clich quit, the game quits
            sys.exit()

        display.update()

def pause_menu(Button,run_game):
    """pause_menu"""
    #make the screen display
    display.set_caption("Jet Mission")  #if the game is paused, prints Jet mission
    screen = pygame.display.set_mode((800, 600))    #set the size of the text

    # object button for quit and start
    start_button = Button("quit button.png")    #quit button
    return_button = Button("pause button.png")  #return button

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")   #load an image of the background
    bg_image = pygame.transform.scale(bg_image, (800, 600)) #scale the background


    pygame.init()
    paused=True #pause flag
    while paused:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #draw the size of star
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150)) #draw the size of return
        screen.blit(bg_image, (0, 0))   #set the background image

        screen.blit(start_button.button, (250, 200))
        screen.blit(return_button.button, (250, 300))

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):    #clicks start
                menu_screen(Button,run_game)
            if rect_return.collidepoint(mouse.get_pos()):   #clicks return
                paused = False #flag become  False

        if ev.type == QUIT:
            sys.exit()


        display.update()

def lose_menu(Button,run_game,score):
    """make the screen for menu"""
    display.set_caption("Jet Mission")  #display Jet mission when lose
    screen = pygame.display.set_mode((800, 600))    #the size of the caption
    font=pygame.font.SysFont("times new roman",100) #set the font for the caption
    text=font.render("Replay?",True,(255,255,255))  #ask if want to replay or not
    score_text=font.render("score:"+str(score),True,(255,255,255))  #the score

    # object button for quit and start
    start_button = Button("New Piskel.png")     #add the start button
    quit_button = Button("quit button.png")     #add the quit button

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")   #the background image
    bg_image = pygame.transform.scale(bg_image, (800, 600)) #scale the background image

    pygame.init()

    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image, (0, 0))   #call the background image
        screen.blit(text,(200,10))      #call the text
        screen.blit(start_button.button, (250, 200))    #call the start button(scale wanted)
        screen.blit(quit_button.button, (250, 300))     #call the quit button(scale wanted)
        screen.blit(score_text,(200,400))               #call the score (scale wnted)

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:  #if mouse is clicked
            if rect_start.collidepoint(mouse.get_pos()):    #click start, start again
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):     #click quit, quit the game
                sys.exit()

        if ev.type == QUIT:
            sys.exit()

        display.update()
