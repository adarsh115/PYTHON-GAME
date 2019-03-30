from pygame import mixer  # Load the required library

mixer.init()

from typing import Tuple

import pygame

import time
import random

pygame.init()

display_width =900
display_height =600

background=(127,255,0)
skyblue=(30,144,255)
violet = (148,0,211)
black = (0,0,0)
yellow = (250-250-210)
white = (255,255,255)
red = (175,0,0)
bright_red=(255,0,0)
green = (0,255,0)
blue=(0,0,175)
bright_blue=(0,0,255)
car_width = 63
pause = True
def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()


def gamequit():
    pygame.quit()
    quit()



gamedisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('FIRST GAME OF ADIZ IN PYTHON')
clock = pygame.time.Clock()

carImg = pygame.image.load('SAMEEP.png')
backgroundfile = pygame.image.load("m.png")
pygame.display.set_icon(backgroundfile)






#progress counter
def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged:"+str(count), True, black)
    gamedisplay.blit(text,(0,0))


#obstacles
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gamedisplay,color,[thingx,thingy,thingw,thingh])




def car(x,y):
    gamedisplay.blit(carImg,(x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



def  crash():
        mixer.music.load('explosion.mp3')
        mixer.music.play()
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf, TextRect)

        while True:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # gameDisplay.fill(white)

            buttons("Play Again", 150, 450, 110, 50, red, bright_red, game_loop)
            buttons("Quit", 550, 450, 100, 50, blue, bright_blue, gamequit)

            pygame.display.update()
            clock.tick(15)
#################################################BUTTONS###############################################################
def buttons(msg,x,y,w,h,iac,ac,actions=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        pygame.draw.rect(gamedisplay, ac, (x,y,w,h))
        if click[0]==1 and actions!= None:
            actions()




    else:
        pygame.draw.rect(gamedisplay, iac, (x,y,w,h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x+(w/2),y+(h/2))
    gamedisplay.blit(textSurf, textRect)

#####################################################################pause########################################################################################
def paused():
    pygame.mixer.music.pause()
    gamedisplay.fill(yellow)
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gamedisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



        buttons("Continue", 230, 450, 100, 50, red, bright_red, unpause)
        buttons("Quit", 570, 450, 100, 50, blue, bright_blue, gamequit)

        pygame.display.update()
        clock.tick(15)



    #####################################################################INTRO#####################################################################################
def game_intro():
    intro = True
    mixer.music.load('ncs.mp3')
    mixer.music.play()

    dropy = -900
    dropspeed = 10
    drop_width = 6
    drop_height = 18

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.fill(background)
        lagreText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('SAVE SAMEEP', lagreText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf, TextRect)

        pygame.draw.rect(gamedisplay, red, (230, 450, 100, 50))
        pygame.draw.rect(gamedisplay, blue, (570, 450, 100, 50))


        ##########purplerain########
        for i in range(1,500):
            dropx = random.randrange(0, display_width)
            things(dropx, dropy, drop_width, drop_height, violet)
            dropy += dropspeed

            if  dropy > display_width:
                dropy = 0-drop_height
                dropx = random.randrange(0, display_width)


        #print(mouse)

        ####################red####################
        buttons("GO!!!!!",230, 450, 100, 50,red,bright_red,game_loop)



        ####################blue##################

        buttons("QUIT!", 570, 450, 100, 50, blue, bright_blue,gamequit)







        pygame.display.update()
        clock.tick(15)


############################################################GAMELOOP####################################################################################################
def game_loop():
    global  pause
    mixer.music.load('thor.mp3')
    mixer.music.play()
    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change =0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 50
    thing_height = 50

    dodged = 0

    gameexit = False
    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                if event.key == pygame.K_RIGHT:
                    x_change = 15
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0





        x += x_change
        gamedisplay.fill(skyblue)

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, red)
        thing_starty += thing_speed

        car(x,y)

        things_dodged(dodged)



        if x> (display_width - car_width) or x<0:
            crash()

        if thing_starty > display_height :
            thing_starty = 0 - thing_height

            thing_startx = random.randrange(0, display_width)


            dodged+=1
            thing_speed
            thing_width += dodged

        if y < thing_starty + thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width< thing_startx + thing_width :
                print('x_crossover')
                crash()

        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
