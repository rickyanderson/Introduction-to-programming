from pygame import *        #import pygame
from pygame.sprite import * #import pygame sprite

class Jet(Sprite):          #class jet
    """initialize the jet"""

    def __init__(self, screen):
        Sprite.__init__(self)
        """initialize the Jet"""
        self.image = image.load("battlejet.png")    #load battlejet image
        self.image = pygame.transform.scale(self.image, (90, 50))   #set the size of the jet image
        self.rect = self.image.get_rect()   #the image is rectangle
        self.rect.x = 10
        self.rect.y = 50
        self.screen = screen        #initiate screen
        self.move_speed = 6         #movement speed for the jet
        """bullet"""
        self.firerates = 2          #firerate for the jet

    def moveleft(self):
        self.rect.x -= self.move_speed  #so that the jet can move to the left
        display.flip()

    def moveright(self):
        self.rect.x += self.move_speed  #so that the jet can move to the right
        display.flip()

    def moveup(self):
        self.rect.y -= self.move_speed  #so that the jet can move upwards
        display.flip()

    def movedown(self):
        self.rect.y += self.move_speed  #so that the jet can move downwards
        display.flip()





class Star_bg:          #class Star_bg
    #resourse of the backgound setting
    def __init__(self,background):
        self.background=image.load(background)  #load the background image
        self.background=pygame.transform.scale(self.background,(800,600))   #set the background size
        self.background_size=self.background.get_size() #get the size for the background image
        self.background_rect=self.background.get_rect()
        self.width,self.height=self.background_size #the width and the height is the same as the size of the background
    def draw(self,screen,x,y):
        screen.blit(self.background,(x,y))  #to show it on the screen, appear in the game

class Bullet(Sprite):
    def __init__(self,screen, startx, starty):
        Sprite. __init__(self)  #super class for sprite
        self.startx = startx
        self.starty = starty

        self.speedx = 20        #the speed to move horizontally

        self.image = pygame.image.load("bullets.png")       #load the bullets.png
        self.image = pygame.transform.scale(self.image,(40,40)) #to set the size of the bullets
        self.rect=self.image.get_rect()     #to set the image
        self.rect.left = startx
        self.rect.top = starty
        self.rect.center = (startx,starty)
        self.screen = screen                #initiate screen
    def movement(self):
        self.screen.blit(self.image,[self.startx,self.starty])      #bullet starts on the ship
        self.rect.left += self.speedx       #moves the bullet to the right

class Asteroid(Sprite):
    """initialize the Asteroid"""
    def __init__(self, screen, width, height, speedx, startx, starty):
        Sprite.__init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = speedx    #the movement speed of the asteroid

        self.image = pygame.image.load("meteor.png")        #image of the meteor, load it in the game
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()   #to set the image rect
        self.rect.left = startx
        self.rect.top = starty
        self.screen = screen                #initiate screen

    def movement(self):
        """method to move the Asteoid"""
        self.rect.left -= self.speedx       #move the asteroid to the left


class Button(Sprite):
    """initialize the button"""
    def __init__(self,image):
        Sprite. __init__(self)
        self.button=pygame.image.load(image)        #load the image button
        self.button=pygame.transform.scale(self.button,(300,150))   #set the size of the image for the button
