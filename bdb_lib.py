"""Woohooo this is a library file!"""
import os
import json
import pygame

#-- Setup -----------------------------------------------------------------------------------------#
for i in range(100): # clearing the console properly
    print("")

with open('config.json', 'r',encoding='utf-8') as f:
    config_data = json.load(f)

full_path = os.path.abspath(os.path.dirname(__file__))
#-- Debugging -------------------------------------------------------------------------------------#
class PyWindow:
    """A class representing a window in a Pygame application. This class handles
    the creation, updating, and rendering of a Pygame window."""
    class Ingame:
        """A class representing the game state for a Pygame application. This class
        handles the game logic, including the creation and management of game objects."""
        def __init__(self
                     ) -> None:
            pygame.init() # pylint: disable=no-member

            pygame.display.set_icon(pygame.image.load(config_data['ingame']['window']['icon']))
            # Set window icon

            self.window_width = config_data['ingame']['window']['width']
            # Window width set number of pixels

            self.window_height = int(self.window_width * config_data['ingame']['window']['ratio'])
            # Window height in ratio to width

            self.title = str(config_data['ingame']['window']['title'])
            pygame.display.set_caption(self.title)
            # Window title

            self.visible = False
            # Window visibility (in taskbar)

            self.obj = pygame.display.set_mode((self.window_width,self.window_height))
            # Window object

            self.closable = True
            # Window closable when tried to close via windows X button

            self.clock = pygame.time.Clock()
            # Clock object

            self.fpslimit = int(config_data['ingame']['configs']['fps_limit'])
            # FPS limit
        def update(self,
                   ) -> bool:
            """Window update function"""
            #End
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #pylint: disable=no-member
                    if self.closable:
                        pygame.quit() # pylint: disable=no-member
                        return False
                    else:
                        pygame.display.iconify()
            #Update
            pygame.display.update()
            self.clock.tick(self.fpslimit)
            return True
        def show_hide(self
                      ) -> None:
            """Toogle pygame window visibility \n
                None: change to opposite, True: Show, False: Hide"""
            self.visible = not self.visible
            pygame.display.iconify()
        def text(self,
                text:str="empty",
                size:int=10,
                rgba:tuple=(255,255,255,255),
                pos:tuple=(1,1),
                font:str="fnf") -> None:
            """Display text on pygame window"""
            path = config_data['settings']['paths']['fonts'][font]
            # determine font path

            font_obj = pygame.font.Font(path,size)
            # select font

            fullstring = font_obj.render(text,True,(rgba[0],rgba[1],rgba[2],rgba[3]))
            self.obj.blit(fullstring,(pos[0],pos[1]))
            # render text
        def fps(self,
                size:int=20,
                rgba:tuple=(255,255,255,255),
                pos:tuple=(1,1),
                above:bool=False,
                font:str="windows",
                hz:int=None) -> None:
            """Display FPS on pygame window or change the fps limit"""
            amount = int(self.clock.get_fps())
            if hz:
                self.fpslimit = hz
                return
            if above:
                pygame.draw.rect(
                    self.obj,(120,20,162),pygame.Rect(pos[0],pos[1],(size*1.4),size),size)
            path = config_data['settings']['paths']['fonts'][font]
            # determine font path

            font_obj = pygame.font.Font(path,size)
            # Select font as obj
            amount += 300 #(get more fps)
            fullstring = font_obj.render(str(amount),True,(rgba[0],rgba[1],rgba[2],rgba[3]))
            self.obj.blit(fullstring,(pos[0],pos[1]))
            # render text
        def blank_background(self,
                             x:int=0,
                             y:int=0,
                             width:int=None,
                             height:int=None) -> None:
            """Create a blank background. great for debugging"""
            if not width:
                width = self.window_width
            if not height:
                height = self.window_height
            pygame.draw.rect(self.obj,(0,0,0),
                pygame.Rect(x,y,width,height),width)
        def box(self,
                color=(255,255,255),
                width:int=20,
                height:int=20,
                x:int=20,
                y:int=20,
                thicc:int=None) -> None:
            """Draw a box on pygame window. great for debugging"""
            if not thicc:
                thicc = self.window_width
            pygame.draw.rect(self.obj,color,pygame.Rect(x,y,width,height),thicc)
        def load_image(self,
                       path:str=config_data['settings']['paths']['blank']) -> pygame.Surface:
            """Load image from path"""
            return pygame.image.load(path).convert_alpha()
        def anchor_image(self,
                 obj,anchor:int or str=1,x:int=0,y:int=0) -> pygame.Rect:
            """Get rect of window \n
            1. topleft, 2. midtop, 3. topright, 4. midleft, 5 and 0. center,
            six. midright, 7. bottomleft, 8. midbottom, 9. bottomright"""
            match anchor:
                case 1 | "topleft":
                    return obj.get_rect(topleft=(x,y))
                case 2 | "midtop":
                    return obj.get_rect(midtop=(x,y))
                case 3 | "topright":
                    return obj.get_rect(topright=(x,y))
                case 4 | "midleft":
                    return obj.get_rect(midleft=(x,y))
                case 5 | 0 | "center":
                    return obj.get_rect(center=(x,y))
                case 6 | "midright":
                    return obj.get_rect(midright=(x,y))
                case 7 | "bottomleft":
                    return obj.get_rect(bottomleft=(x,y))
                case 8 | "midbottom":
                    return obj.get_rect(midbottom=(x,y))
                case 9 | "bottomright":
                    return obj.get_rect(bottomright=(x,y))
                case _:
                    print(f"invalid anchor point of '{obj}' with '{anchor}'")
                    return None
        def draw(self,
                load:pygame.Surface=None,
                rect:pygame.Rect=None) -> None:
            """Display image on pygame window"""
            if not load or not rect:
                print("Invalid parameters")
                return None
            return self.obj.blit(load,rect)
        def resize_image(self,
                         obj:pygame.Surface=None,
                         width:int=None,
                         height:int=None
                         ) -> pygame.Surface:
            """Resize image to window size"""
            if not width:
                width = self.window_width
            if not height:
                height = self.window_height
            return pygame.transform.scale(obj,(width,height))
