#!/usr/bin/env python

import pygame
import sys
from pgu import gui

import threading
from time import sleep
import argparse

from UI import game     #frontend mainscreen.
from engine import SimulationEngine as simeng
from games import test_game as populate
from UI import endgame

from global_config import config

def enable_vsync():
    if sys.platform != 'darwin':
        return
    try:
        import ctypes
        import ctypes.util
        ogl = ctypes.cdll.LoadLibrary(ctypes.util.find_library("OpenGL"))
        # set v to 1 to enable vsync, 0 to disable vsync
        v = ctypes.c_int(1)
        ogl.CGLSetParameter(ogl.CGLGetCurrentContext(), ctypes.c_int(222), ctypes.pointer(v))
    except:
        print "Unable to set vsync mode, using driver defaults"

class FrontEndThread(threading.Thread):
    def __init__(self, game, proj):
        threading.Thread.__init__(self)
        self.proj = proj
        self.game = game

    def run(self):
        self.game.run()

class BackEndThread(threading.Thread):
    def __init__(self, game, proj):
        threading.Thread.__init__(self)
        self.proj = proj
        self.game = game

    def run(self):
        simeng.run_engine(self.game, self.proj)

def main():
    # Parse arguments passed to game
    parser = argparse.ArgumentParser(description='Software Engineering Simulator')
    parser.add_argument('-l','--load', help='Load a saved game or default scenario', metavar='game')
    args = vars(parser.parse_args())

    enable_vsync()
    pygame.init()

    if args['load']:
        exec('from games import %s as chosen_game' % args['load'])
        project = chosen_game.load_game()
    else:
        project = populate.load_game()

    glob_game = game.Game(project, config)

    frontend = FrontEndThread(glob_game,project)
    backend = BackEndThread(glob_game,project)
    frontend.start()
    backend.start()
    backend.join()
    glob_game.endgame(project)
    glob_game.update(project)
    frontend.join()

if __name__ == "__main__":
    main()
