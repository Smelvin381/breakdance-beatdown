"""Woohooo this is a lib file!"""
import os
import json
import random
import time
import pygame

#-- Setup -----------------------------------------------------------------------------------------#
for i in range(100):
    print("")

with open('config.json', 'r',encoding='utf-8') as f:
    config_data = json.load(f)

full_path = os.path.abspath(os.path.dirname(__file__))
#-- Debugging -------------------------------------------------------------------------------------#
class PyWindow:
    """Window class for pygame"""
    class Ingame:
        """Ingame window and objects"""
        def __init__(self) -> None:
            pygame.init() # pylint: disable=no-member
            self.size = config_data['ingame']['window']['width']
            # Window width set number of pixels

            self.height = int(self.size * config_data['ingame']['window']['ratio'])
            # Window height in ratio to width

            self.title = str(config_data['ingame']['window']['title'])
            pygame.display.set_caption(self.title)
            # Window title

            self.visible = False
            # Window visibility (in taskbar)

            self.obj = pygame.display.set_mode((self.size,self.height))
            # Window object

            self.closable = True
            # Window closable when tried to close via windows X button

            self.clock = pygame.time.Clock()
        def update(self,fps:int=70) -> None:
            """Window update function"""
            if True: #End
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: #pylint: disable=no-member
                        if self.closable:
                            pygame.quit() # pylint: disable=no-member
                            return False
                        else:
                            pygame.display.iconify()
            if True: #Update
                pygame.display.update()
                self.clock.tick(fps)
            return True
        def show_hide(self) -> None:
            """Toogle pygame window visibility \n
                None: change to opposite, True: Show, False: Hide"""
            self.visible = not self.visible
            pygame.display.iconify()
        def text(self,text:str="empty",größe:int=10,RGBA:list=[255,255,255,255],cordi:list=[0,0],font:int=1,AA:bool=True):
            """Display text on pygame window"""
            schrift = pygame.font.Font("assets/others/fonts/fnf.ttf",größe)
            fertigtext = schrift.render(text,AA,(RGBA[0],RGBA[1],RGBA[2],RGBA[3]))
            self.obj.blit(fertigtext,(cordi[0],cordi[1]))
        def show_fps(self) -> None:
            """You can fuck yourself"""
            zahl = int(self.clock.get_fps())
            if zahl < 50:
                farbe = (250,193,113,255)
            elif zahl > 60:
                farbe = (140,250,113,255)
            else:
                farbe = (255,255,255,255)
            self.text(text=str(zahl),größe=20,RGBA=farbe,cordi=[10,10],font=1)
        def box(self,color=(100,100,100),size:list=[20,20],cordi:list=[20,20],filled:bool=False):
            """Draw a rectangle on pygame window"""
            if filled:
                dicke = int(size[0]/2)
            else:
                dicke = 2
            pygame.draw.rect(self.obj,color,pygame.Rect(cordi[0],cordi[1],size[0],size[1]),dicke)

if __name__ == "__main__":
    e = PyWindow.Ingame()
    while e.update():
        e.box(size=[100,100],cordi=[0,0],filled=True,color=(255,255,100))
        e.show_fps()
        e.box(cordi=[250,255],size=[60,40])
    exit()


# yo domi
# Das da drunter ist das alte code welches turbo viel fps hat. das da trüber ist das neue, welches nicht so viel fps hat.
class d:
    class sett:
        class fenster:
            width = int(1920)
            height = int(width*0.57)
            title = 'RAPBATTLES - '
            obj = None

        class clock:
            obj = None
        key = pygame.key.get_pressed
        base = {
            "ticks_limit": float(360.0),
            "status": False
        }
        game = {
            "opps": ["Jesus","Johnnysins"],
            "beginning_player": True, #True=Rechts/#False=Links
        }
        pfade = {
            "fonts": "assets/others/fonts",
            "blank_img": "others/blank.png",
        }
    def pygame(                                                                                                         #Init oder QUIT pygame (beinhaltet fenster als variable)
            start:bool=None,
            größe:list=[sett.fenster.width,sett.fenster.height],
            name:str="None"):
        if start:                                                                                   #Start Pygame
            pygame.init()
            d.sett.fenster.obj = pygame.display.set_mode((größe[0],größe[1]))
            pygame.display.set_caption(f'{d.sett.fenster.title}{name}')
            d.sett.clock.obj = pygame.time.Clock()
            d.sett.base["status"] = True
        elif start == False:                                                                        #Close Pygame
            pygame.quit()
            d.sett.base["status"] = False
        elif start == None:                                                                         #Restart Pygame
            pygame.quit()
            pygame.init()
            d.sett.fenster.obj = pygame.display.set_mode((größe[0],größe[1]))
            pygame.display.set_caption(f'{d.sett.fenster.title}{name}')
            d.sett.clock.obj = pygame.time.Clock()
            d.sett.base["status"] = True
    def text(                                                                                                           #Text erscheinen lassen
            text:str="empty",
            größe:int=10,
            RGBA:list=[255,255,255,255],
            cordi:list=[0,0],
            font:int=1,
            AA:bool=True):

        alle_fonts = os.listdir(d.sett.pfade["fonts"])
        schrift = pygame.font.Font(f"{d.sett.pfade['fonts']}/{alle_fonts[font]}",größe)
        fertigtext = schrift.render(text,AA,(RGBA[0],RGBA[1],RGBA[2],RGBA[3]))
        d.sett.fenster.obj.blit(fertigtext,(cordi[0],cordi[1]))
    def image_load(                                                                                                     #Quelle mit Bild laden
            quelle:str=sett.pfade["blank_img"]):
        return pygame.image.load(f'assets/{quelle}').convert_alpha()
    def rect(                                                                                                           #Bild rect und position
            load="empty",
            cordi:list=[0,0],
            anker:int=1):
        if anker == 1:
            return load.get_rect(topleft = (cordi[0],cordi[1]))
        elif anker == 2:
            return load.get_rect(midtop = (cordi[0],cordi[1]))
        elif anker == 3:
            return load.get_rect(topright = (cordi[0],cordi[1]))
        elif anker == 4:
            return load.get_rect(midleft = (cordi[0],cordi[1]))
        elif anker == 5 or anker == 0:
            return load.get_rect(center = (cordi[0],cordi[1]))
        elif anker == 6:
            return load.get_rect(midright = (cordi[0],cordi[1]))
        elif anker == 7:
            return load.get_rect(bottomleft = (cordi[0],cordi[1]))
        elif anker == 8:
            return load.get_rect(midbottom = (cordi[0],cordi[1]))
        elif anker == 9:
            return load.get_rect(bottomright = (cordi[0],cordi[1]))
    def draw(                                                                                                           #Zeichnet Quelle
            load="empty",
            rect="empty"):
        return d.sett.fenster.obj.blit(load,rect)
    def play_sound(                                                                                                     #Läd und spielt ton oder musik ab
            quelle:str="empty",
            ton:bool=True):
        if ton:
            geräusch = pygame.mixer.Sound(quelle)
            geräusch.play()
        else:
            pygame.mixer.music.load(quelle)
            pygame.mixer.music.play(-1)
    def random(                                                                                                         #Gibt eine zufällige int-zahl
            oberer:int=0,
            unterer:int=10):
        if unterer > oberer:
            return random.randint(unterer,oberer)
        elif oberer > unterer:
            return random.randint(oberer,unterer)
        else:
            print(f"Fehler in random.randint mit Input: {oberer} und {unterer}")
            return 0
    def update(                                                                                                         #Update Display und Event
            FPS:int=70):
        if "End" == "End":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        if "Updater" == "Updater":
            pygame.display.update()
            d.sett.clock.obj.tick(FPS)
    def warning(                                                                                                        #Fehler meldung anzeigen
            grund:str="E"):
        missing = d.transform(load=d.image_load(quelle='others/missing.png'),type=0,eingabe=[d.sett.fenster.width,d.sett.fenster.height])
        missing_r = d.rect(missing)
        schrift_gröse = int(d.sett.fenster.height * 0.1)
        d.draw(missing,missing_r)
        d.text(text=f"{grund[0]}",größe=schrift_gröse,RGBA=[0,0,0,255],cordi=[20,20],AA=False)
        d.update()
        while True:
            if grund=="E" and pygame.key.get_pressed()[pygame.K_e]:
                break
            d.update()
    def transform(                                                                                                      #Transformt ein Bild
            load="empty",
            type:str="scale",
            eingabe=[sett.fenster.width,sett.fenster.height]):
        #Type = None(Nur Skalieren),
        type = str(type).lower()
        optionen = {
            "resize": ["0","vergrößern","verkleinern","scale","resize","größe","change size","größe ändern"],
            "rotate": ["1","rotate","drehen","dreh"],
            "fade": ["2","fade","opacity","Opazität","druckkraft","visibility"],
            "auto": ["3","auto","dnc","automatisch","automatic"],
        }
        if type in optionen["resize"] or type in optionen["auto"]: #eingabe: [Xgröße,Ygröße]
            return pygame.transform.scale(load,(eingabe[0],eingabe[1]))
        elif type in optionen["rotate"]: #eingabe: (Load,Drehung), (X??,Y??)
            return pygame.transform.rotate(load,eingabe[0])
        elif type in optionen["fade"]: #eingabe: alpha
            load.set_alpha(eingabe)
            return load
    def cut_float(                                                                                                      #Kürzt eine float Variable zu einer Kommastelle
            eingabe:float=0.0):
        eingabe = eingabe + 0.005
        eingabe = (int)(eingabe*100)
        eingabe = eingabe/100
        return eingabe
    def box(                                                                                                            #Zeichnet eine Blechbüchse
            farbe=(100,100,100),
            größe:list=[20,20],
            cordi:list=[20,20],
            filled:bool=False):
        if filled:
            dicke = int(größe[0]/2)
        else:
            dicke = 2
        pygame.draw.rect(d.sett.fenster.obj, farbe, pygame.Rect(cordi[0],cordi[1],größe[0],größe[1]),dicke)
#-- FPS ----------------------------------------------------------------------------------------------------------------#
class FPS:                                                                                                              #FPS anzeige
    txt = {
        "pos": [10,10]
    }
    def __init__(self) -> None:
        """You can fuck yourself"""
        zahl = int(d.sett.clock.obj.get_fps())
        if zahl < 50:
            farbe = (250,193,113,255)
        elif zahl > 60:
            farbe = (140,250,113,255)
        else:
            farbe = (255,255,255,255)
        d.text(text=str(zahl),größe=20,RGBA=farbe,cordi=[FPS.txt["pos"][0],FPS.txt["pos"][1]],font=1)

d.pygame(größe=[300,300])
while True:
    d.box(farbe=(255,255,100),größe=[300,300],cordi=[0,0],filled=True)
    FPS()
    d.update(FPS=7000)
