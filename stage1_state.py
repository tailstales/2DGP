__author__ = 'YUNG BIN'

import random
import json
import os
import game_framework
import title_state
import stage2_state

from pico2d import *


name = "Stage1State"

boy = None
background = None
font = None



class Background:
    def __init__(self):
         self.image = load_image('C:/2dgp/2dproject/background/stage1.png')

    def draw(self):
        self.image.draw(400, 300)



class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, LADDER_UP, LADDER_DOWN = 0, 1, 2, 3, 4, 5

    def __init__(self):
        self.x, self.y = 780, 60
        self.frame = random.randint(0, 7)
        self.state = self.LEFT_STAND
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def handle_event(self,event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LADDER_UP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LADDER_DOWN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.LADDER_UP,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.LADDER_DOWN,):
                self.state = self.LEFT_STAND

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.state == self.RIGHT_RUN:
            self.x = min(785,self.x+5)
        elif self.state == self.LEFT_RUN:
            self.x = max(15,self.x-5)
        elif self.state == self.LADDER_UP:
            if self.y < 580:
                self.y =  self.y+5
        elif self.state == self.LADDER_DOWN:
            if self.y > 60:
                self.y = self.y-5

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def enter():
    global boy, background
    boy = Boy()
    background = Background()


def exit():
    global boy, background
    del(boy)
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    global boy, running
    running = False
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(stage2_state)
        else:
            boy.handle_event(event)


def update():
    boy.update()


def draw():

    global boy
    global running


    running = True;
    while running:
       handle_events()

       update()

       clear_canvas()
       background.draw()
       boy.draw()
       update_canvas()

       delay(0.05)
