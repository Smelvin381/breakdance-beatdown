"""Woohoo! You found the source code!"""
from bdb_lib import PyWindow, config_data

#-- Resources -------------------------------------------------------------------------------------#
if config_data['ingame']['configs']['debugging']['resources']:
    class Stage1(PyWindow.Ingame):
        """Images and objects for stage 1"""
        def __init__(self) -> None:
            super().__init__()
            self.train_enabled = config_data['ingame']['configs']['train']['enabled']
            self.window_enabled = config_data['ingame']['configs']['windows']['enabled']

            path = config_data['settings']['paths']['surface']['ingame']
            # Determine path

            if self.train_enabled:
                train_width = self.window_width*8
                train_height = self.window_height*1.7
                # image size in relation to window

                self.train_x_limit = (-25000,25000)
                # x position limit of train from left to right

                self.train_y = self.window_height*0.50
                # y position on window

                self.train_load = self.load_image(path=f"{path}stages\\1\\train.png")
                self.train_load = self.resize_image(
                    self.train_load,width=train_width,height=train_height)
                # load and resize train image

                self.train_x = self.train_x_limit[0]
                # current position of

                self.train_speed = config_data['ingame']['configs']['train']['speed']
                # speed of train
            if self.window_enabled:
                self.win_l = [
                    self.load_image(path=f"{path}stages\\1\\win0.png"),
                    self.load_image(path=f"{path}stages\\1\\win1.png"),
                    self.load_image(path=f"{path}stages\\1\\win2.png"),
                    self.load_image(path=f"{path}stages\\1\\win3.png"),
                    self.load_image(path=f"{path}stages\\1\\win4.png")
                ]
                # load window images

                for index, load in enumerate(self.win_l):
                    self.win_l[index] = self.resize_image(load)
                # resize images to window size

                self.win_r = [
                    self.anchor_image(self.win_l[0]),
                    self.anchor_image(self.win_l[1]),
                    self.anchor_image(self.win_l[2]),
                    self.anchor_image(self.win_l[3]),
                    self.anchor_image(self.win_l[4])
                ]
                # anchor

                self.win_tick = 0.00
                self.win_tick_limit = 4.00
                self.win_tick_speed = config_data['ingame']['configs']['windows']['speed']
                # rate of window color change

            bg_path = config_data['settings']['paths']['surface']['ingame']+"stages\\1\\"

            self.street_l = self.load_image(path=f"{bg_path}street.png")
            self.street_l = self.resize_image(self.street_l)
            self.street_r = self.anchor_image(self.street_l)

            self.behind_train_l = self.load_image(path=f"{bg_path}behindTrain.png")
            self.behind_train_l = self.resize_image(self.behind_train_l)
            self.behind_train_r = self.anchor_image(self.behind_train_l)

            self.city_l = self.load_image(path=f"{bg_path}city.png")
            self.city_l = self.resize_image(self.city_l)
            self.city_r = self.anchor_image(self.city_l)

            self.sky_l = self.load_image(path=f"{bg_path}sky.png")
            self.sky_l = self.resize_image(self.sky_l)
            self.sky_r = self.anchor_image(self.sky_l)
        def drive_train(self) -> None:
            """Calculate and draw train"""
            if not config_data['ingame']['configs']['train']['enabled']:
                return None

            self.train_x += self.train_speed
            if self.train_x > self.train_x_limit[1]:
                self.train_x = self.train_x_limit[0]
            self.draw(
                self.train_load,self.anchor_image(self.train_load,5,self.train_x,self.train_y))
        def display_windows(self) -> None:
            """Calculate and draw windows in the background"""
            if not config_data['ingame']['configs']['windows']['enabled']:
                return None

            self.win_tick += self.win_tick_speed
            if self.win_tick > self.win_tick_limit:
                self.win_tick = 0.00
            self.draw(self.win_l[int(self.win_tick)],self.win_r[int(self.win_tick)])
        def display_bg(self) -> None:
            """Render full background automatically"""
            self.draw(self.sky_l,self.sky_r)
            self.draw(self.city_l,self.city_r)
            if self.window_enabled:
                self.display_windows()
            self.draw(self.behind_train_l,self.behind_train_r)
            if self.train_enabled:
                self.drive_train()
            self.draw(self.street_l,self.street_r)

    game = PyWindow.Ingame()
    new = Stage1()
#-- Mainloop --------------------------------------------------------------------------------------#
if config_data['ingame']['configs']['debugging']['main_loop']:
    while game.update():
        new.display_bg()
        # keys=pygame.key.get_pressed()
        # print(keys.index())
        game.fps()
