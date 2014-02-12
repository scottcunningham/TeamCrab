import pygame, os
from pgu import gui
from time import sleep

glob_game = None

this_dir = os.path.dirname(__file__)
root_dir = os.path.join(this_dir, '../..')

def pauseClick(self):
    print("Pause Clicked!")

class Game:
    def __init__(self, project_data, game_config):
        glob_game = self
        self.project_data = project_data
        self.config = game_config
        self.firstDraw = True

        # Screen setup.
        # TODO: This should be passed in the constructor rather than
        # being created in here.
        self.screen = pygame.display.set_mode((self.config["screenX"],
            self.config["screenY"]))
        self.app = gui.App()
        self.app.connect(gui.QUIT,self.app.quit,None)
        self.contain = gui.Container(width = self.config["screenX"],
            height = self.config["screenY"])

    ''' Handles all input events and goes to sleep.
    '''
    def run(self):
        self.draw()
        while True:
            sleep(self.config["sleep_duration"])
            # Handle all events.
            for event in pygame.event.get():
                # Tell PGU about all events.
                self.app.event(event)
                # Handle quitting.
                if event.type == pygame.QUIT:
                    os._exit(1)

    ''' Retrieves updated information from the backend and redraws the screen.
    '''
    def update(self,project):
        self.project_data = project
        self.draw()

    ''' Draws the world map onscreen.
    '''
    def draw_world_map(self):
        worldMap = pygame.image.load(self.config["map_path"])
        self.screen.blit(worldMap, (0, 0))

    ''' Draws bottom bar, taking screen geometry from global config file.
    Draws statistics about progress, balance, etc on the bottom bar.
    '''
    def draw_bottom_bar(self, font):
        # TODO: Info to be retrieved from backend, currently dummy data.
        bar_height = self.config["bottom_bar_height"]
        x = self.config["screenX"]
        y = self.config["screenY"]

        # Draw empty bottom bar.
        pygame.draw.rect(self.screen, self.config["bar_colour"],
                (0, y - bar_height, 850, bar_height))

        # Overlay balance & statistics on bottom bar.
        label_pos = y - bar_height
        label = font.render("-$" + str(int(self.project_data.locations[0].teams[0].task.progress)), 1, (255, 0, 0))
        self.screen.blit(label, (20, label_pos))
        label = font.render("Jul 21st 14:00 GMT", 1, (0, 0, 0))
        self.screen.blit(label, (200, label_pos))
        label = font.render("10 Items Needing Review", 1, (238, 255, 53))
        self.screen.blit(label, (400, label_pos))

    ''' Draws dots showing sites around the world map.
    '''
    def draw_sites(self):
        # TODO: Info to be retrieved from backend, currently dummy data.
        for x in range (5):
            pygame.draw.circle(self.screen, self.config["site_colour"],
                    (x*10, x*10), 7)

    ''' Draws detailed info about the currently selected site.
    '''
    def draw_detailed_site_info(self, font):
        # TODO: Info to b retrieved from backend, currently dummy data.
        y = 320

        # Draw plain background.
        pygame.draw.rect(self.screen, self.config["background_colour"],
                (0, y, 200, 140))

        # Draw icons and accompanying text.
        workerIcon = pygame.image.load(self.config["man_icon_path"])
        self.screen.blit(workerIcon, (1, 325))
        label = font.render("2 Teams", 1, (0, 0, 0))
        self.screen.blit(label, (40, y + 15))

        cogIcon = pygame.image.load(self.config["cog_icon_path"])
        self.screen.blit(cogIcon, (1, 360))
        label = font.render("75% Efficiency", 1, (0, 0, 0))
        self.screen.blit(label, (40, y + 50))

        clockIcon = pygame.image.load(self.config["clock_icon_path"])
        self.screen.blit(clockIcon, (1, 395))
        label = font.render("127 Days", 1, (0, 0, 0))
        self.screen.blit(label, (40, y + 85))

        targetIcon = pygame.image.load(self.config["target_icon_path"])
        self.screen.blit(targetIcon, (1, 430))
        label = font.render("On Schedule", 1, (0,0,0))
        self.screen.blit(label, (40, y + 115))

    ''' Draws the "menu" pause button over the bottom bar.
    '''
    def draw_pause_button(self):
        # TODO: Real implementation for button action, currently dummy action.
        button = gui.Button("Menu")
        button.connect(gui.CLICK, pauseClick, None)

        self.contain.add(button, self.config["menuX"], self.config["menuY"])
        self.app.init(self.contain)
        self.app.paint(self.screen)

    ''' Updates the screen - but only the updated portion of it so we save on
    refreshing the entire screen.
    '''
    def refresh_screen(self):
        if self.firstDraw:
            pygame.display.flip()
            self.firstDraw = False
        else:
            pygame.display.update((0, 460, 850, 20))    #bottom bar
            pygame.display.update((0, 320, 200, 140))    #grey box

    ''' Redraws all of the map screen.
    '''
    def draw(self):
        font = pygame.font.SysFont("Helvetica", 15)
        self.draw_world_map()
        self.draw_bottom_bar(font)
        self.draw_sites()
        self.draw_detailed_site_info(font)
        self.draw_pause_button()
        self.refresh_screen()
