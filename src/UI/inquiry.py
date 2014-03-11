import pygame
import json 
from pgu import gui
from time import sleep

class Inquiry:
    def __init__(self, screen, config, project):
        self.config = config
        self.project = project
        self.screen = screen
        self.app = gui.App()
        self.app.connect(gui.QUIT, self.app.quit, None)
        self.contain = gui.Container(width=self.config["screenX"],
                                     height=self.config["screenY"])
    
        self.inquiry_site = None
        self.inquiry_type = None

        self.firstDraw = True
        self.firstOptions = True
        self.firstScroll = True

    def choose_inquiry_site(self,site):
        self.inquiry_site = site
        self.inquiry_type = None
        self.firstScroll = True
        if self.contain.find("report_details"):
            self.contain.remove(self.contain.find("report_details"))

    def do_inquiry(self,inquiry_type):
        self.inquiry_type = inquiry_type
        self.firstScroll = True
        if self.contain.find("report_details"):
            self.contain.remove(self.contain.find("report_details"))

    def refresh_screen(self):
        self.app.init(self.contain)
        self.app.paint(self.screen)
        self.app.update(self.screen)

        pygame.display.flip()

    def draw_inquiry(self):
        pygame.draw.rect(self.screen, 0xFAFCA4,
                            (100,20,650,410))
        pygame.draw.line(self.screen, 0x000000, (250,20), (250,430))

        start_x = 100
        start_y = 20

        if self.firstDraw:
            self.firstDraw = False
            my_list = gui.List(width=175, height=395)
            s = ""
            for itr,site in enumerate(self.project.locations):
                l = gui.Label(site.name)
                l.connect(gui.CLICK, self.choose_inquiry_site,site)
                my_list.add(l)            
                self.contain.add(l, start_x + 5, start_y + 20 +(20* (itr+1) ))

        info_x = 250 + 5
        font = pygame.font.SysFont("Helvetica", 18)

        label = font.render( "Inquiries", 1, (0, 0, 0))
        self.screen.blit(label, (info_x + 150, 20))
        label = font.render( "Press Enter to close this window", 1, (0, 0, 0))
        self.screen.blit(label, (info_x, 400))

        if self.inquiry_site:
            y_offset = 50
            font = pygame.font.SysFont("Helvetica", 24)
            label = font.render(self.inquiry_site.name
                     , 1, (0, 0, 0))
            self.screen.blit(label, (info_x, y_offset))

            y_offset += 30
            if self.firstOptions:
                button = gui.Button('Send "are you on schedule?" email')
                button.connect(gui.CLICK, self.do_inquiry,"on_schedule")
                self.contain.add(button, info_x, y_offset)

            font = pygame.font.SysFont("Helvetica", 16)
            label = font.render("0 Working Days"
                    , 1, (0, 0, 0))
            self.screen.blit(label, (info_x + 365, y_offset))

            y_offset += 20
            if self.firstOptions:
                button = gui.Button('Send "please report status of modules" email')
                button.connect(gui.CLICK, self.do_inquiry,"status")
                self.contain.add(button, info_x, y_offset)

            label = font.render("0.1 Working Days"
                    , 1, (0, 0, 0))
            self.screen.blit(label, (info_x + 365, y_offset))

            y_offset += 20
            if self.firstOptions:
                button = gui.Button('Send "please list completed tasks" email')
                button.connect(gui.CLICK, self.do_inquiry,"list_c_tasks")
                self.contain.add(button, info_x, y_offset)

            label = font.render("0.5 Working Days"
                    , 1, (0, 0, 0))
            self.screen.blit(label, (info_x + 365, y_offset))

            y_offset += 20
            if self.firstOptions:
                button = gui.Button('Hold video conference')
                button.connect(gui.CLICK, self.do_inquiry,"video_conf")
                self.contain.add(button, info_x, y_offset)

            label = font.render("2 Working Days"
                    , 1, (0, 0, 0))
            self.screen.blit(label, (info_x + 365, y_offset))

            y_offset += 20
            if self.firstOptions:
                button = gui.Button('Make site visit')
                button.connect(gui.CLICK, self.do_inquiry,"visit")
                self.contain.add(button, info_x, y_offset)

            label = font.render("7 Working Days"
                    , 1, (0, 0, 0))
            self.screen.blit(label, (info_x + 365, y_offset))

            if self.firstOptions:
                #make sure doesnt add next time
                self.firstOptions = False


            if self.inquiry_type:
                if self.firstScroll:
                    self.firstScroll = False

                    my_list = gui.List(width=480,height=160,name="report_details")

                    my_list.add(gui.Label("Inquiry Results:"))

                    for team in self.inquiry_site.teams:
                        my_list.add(gui.Label("Team " + team.name))

                        if self.inquiry_type == "on_schedule":
                            #if onschedule s = "", else "not "
                            on_or_off = ""
                            my_list.add(gui.Label("We are " + on_or_off + "on schedule."))
                        if self.inquiry_type == "status":
                            pass
                        if self.inquiry_type == "list_c_tasks":
                            pass
                        if self.inquiry_type == "video_conf":
                            pass
                        if self.inquiry_type == "visit":
                            pass

                    self.contain.add(my_list,info_x,y_offset+50)


    def draw(self):
        ''' The parent draw function of the end game screen .'''
        self.draw_inquiry()
        self.refresh_screen()
