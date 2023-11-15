import time
import pygame
import test
import random
from pygame import mixer
from sys import exit
pygame.init()
Inhalte = False #Kein Crash
Objekte = True #Kein Crash
default = {
    "ticks_limit": float(360.0),
    "window_size": 1526,
}



#-- Debug --------------------------------------------------------------------------------------------------------------#
class d: #Für Debugging und Tools
    class sett:
        base = {
            "ticks_limit": float(360.0),
            "window_size": 1080,
            "opps": ["Jesus","Johnnysins"],
            "beginning_player": True, #True=Rechts/#False=Links
        }
        fenster = {
            "x":base["window_size"],
            "y":int(base["window_size"]*0.57),
            "name": "Ingame",
        }
        game = {
            "key": pygame.key.get_pressed(),
        }
    def text(text:str="empty",größe:int="10",farbe:list=[255,255,255],cordi:list=[0,0],font:int=1,AA:bool=True):        #Text erscheinen lassen
        pfad = 'assets/others/fonts/'
        alle_fonts = ['minecraft','windows','fnf','agency']
        #MC = 0,Windows = 1, FNF = 2, Agency = 3,
        schrift = pygame.font.Font(f"{pfad}{alle_fonts[font]}.ttf",größe)
        fertigtext = schrift.render(text,AA,(farbe[0],farbe[1],farbe[2]))
        fenster.blit(fertigtext,(cordi[0],cordi[1]))
    def pygame(start:bool=None,größe:list=[sett.fenster["x"],sett.fenster["y"]],name:str=sett.fenster["name"]):         #Init oder QUIT pygame (beinhaltet fenster als variable)
        global fenster
        global clock
        if start:                                                                                   #Start Pygame
            pygame.init()
            fenster = pygame.display.set_mode((größe[0],größe[1]))
            pygame.display.set_caption(f'RAPBATTLES - {name}')
            clock = pygame.time.Clock()
        elif start == False:                                                                        #Close Pygame
            pygame.quit()
        elif start == None:                                                                         #Restart Pygame
            pygame.quit()
            pygame.init()
            fenster = pygame.display.set_mode((größe[0],größe[1]))
            pygame.display.set_caption(f'RAPBATTLES - {name}')
            clock = pygame.time.Clock()
    def image_load(quelle:str="others/blank.png"):                                                                      #Quelle mit Bild laden
            return pygame.image.load(f'assets/{quelle}').convert_alpha()
    def rect(load="empty",cordi:list=[0,0],anker=1):                                                                    #Bild rect und position
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
    def draw(load="empty",rect="empty"):                                                                                #Zeichnet Quelle
        return fenster.blit(load,rect)
    def play_sound(quelle:str="empty",ton:bool=True):                                                                   #Läd und spielt ton oder musik ab
        if ton:
            geräusch = mixer.Sound(quelle)
            geräusch.play()
        else:
            mixer.music.load(quelle)
            mixer.music.play(-1)
    def random(oberer:int=0,unterer:int=10):                                                                            #Gibt eine zufällige int-zahl
        if unterer > oberer:
            return random.randint(unterer,oberer)
        elif oberer > unterer:
            return random.randint(oberer,unterer)
        else:
            print(f"Fehler in random.randint mit Input: {oberer} und {unterer}")
            return 0
    def update(FPS=70):                                                                                                 #Update Display und Event
        if "End" == "End":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        if "Updater" == "Updater":
            pygame.display.update()
            clock.tick(70)
    def warning(grund:str="E"):                                                                                         #Fehler meldung anzeigen
        missing = d.image_load(quelle='others/missing.png')
        missing = d.transform(load=missing,type=0,eingabe=[d.sett.fenster['x'],d.sett.fenster['y']])
        missing_r = d.rect(missing)
        schrift_gröse = int(d.sett.fenster["y"] * 0.1)
        d.draw(missing,missing_r)
        d.text(text=f"{grund}",größe=schrift_gröse,farbe=[0,0,0],cordi=[20,20],AA=False)
        d.update()
        while True:
            if grund=="E" and pygame.key.get_pressed()[pygame.K_e]:
                break
            d.update()
    def transform(load="empty",type:str="scale",eingabe=[sett.fenster["x"],sett.fenster["y"]]):                         #Transformt ein Bild
        #Type = None(Nur Skalieren),
        type = str(type).lower()
        optionen = {
            "resize": ["0","vergrößern","verkleinern","scale","resize","größe","change size","größe ändern"],
            "rotate": ["1","rotate","drehen","dreh"],
            "fade": ["2","fade","opacity","opazität","druckkraft","visibility"],
            "auto": ["3","auto","dnc","automatisch","automatic"],
        }
        if type in optionen["resize"] or type in optionen["auto"]: #eingabe: [Xgröße,Ygröße]
            return pygame.transform.scale(load,(eingabe[0],eingabe[1]))
        elif type in optionen["rotate"]: #eingabe: (Load,Drehung), (X??,Y??)
            return pygame.transform.rotate(load,eingabe[0])
        elif type in optionen["fade"]: #eingabe: alpha
            pass
    def cut_float(eingabe):                                                                                             #Kürzt eine float Variable zu einer Kommastelle
        eingabe = eingabe + 0.005
        eingabe = (int)(eingabe*100)
        eingabe = eingabe/100
        return eingabe
    def box(farbe=(100,100,100),größe:list=[20,20],cordi:list=[20,20],filled:bool=False):                               #Zeichnet eine Blechbüchse
        if filled:
            dicke = int(größe[0]/2)
        else:
            dicke = 2
        pygame.draw.rect(fenster, farbe, pygame.Rect(cordi[0],cordi[1],größe[0],größe[1]),dicke)
class FPS:                                                                                      #FPS anzeige
    txt_pos = {
        "x": 10,
        "y": 10,
    }
    def __init__(self):
        zahl = int(clock.get_fps())
        anzahl = str(zahl)
        if zahl < 50:
            farbe = (250,193,113)
        elif zahl > 60:
            farbe = (140,250,113)
        else:
            farbe = (255,255,255)
        d.text(anzahl, 20, farbe,(FPS.txt_pos["x"],FPS.txt_pos["y"]),2,True)
#-----------------------------------------------------------------------------------------------------------------------#



#-- Inhalte ------------------------------------------------------------------------------------------------------------#
if Inhalte:                                                                                     #Bilder, Musik, Rect ect.
    class a1: #Alles andere
        d.pygame(None,[d.sett.fenster['x'],d.sett.fenster['y'],d.sett.fenster['name']]) #Fenstergröße

        missing = d.image_load('others/missing.png')
        missing = d.transform(missing,0,[d.sett.fenster['x'],d.sett.fenster['y']])
        missing_r = d.rect(missing,[0,0],1)

        key = pygame.key.get_pressed()
    class main_menu:
        pass
#-----------------------------------------------------------------------------------------------------------------------#



#-- Loop ---------------------------------------------------------------------------------------------------------------#
if Objekte:                                                                                     #Hauptcode
    d.pygame(True,[d.sett.fenster["x"],d.sett.fenster["y"]])
    d.warning()
    quel = [
        d.transform(d.image_load("bod.png")),
        d.transform(d.image_load("gal.png")),
        d.transform(d.image_load("gugu.gif")),
        d.transform(d.image_load("only.png")),
        d.transform(d.image_load("sky.jpg")),
    ]
    quel_r = [
        d.rect(quel[0],[0,0],1),
        d.rect(quel[1],[0,0],1),
        d.rect(quel[2],[0,0],1),
        d.rect(quel[3],[0,0],1),
        d.rect(quel[4],[0,0],1),
    ]

    i = 0
    up = True
    pos = 0
    def test():
        global i,up,pos
        d.box((0,0,0),[d.sett.fenster["x"],d.sett.fenster["y"]],[0,0],True)
        
        if i > 300:
            up = False
        elif i < -45:
            up = True
            pos += 1
        
        if up:
            i += 0.5
        else:
            i -= 0.5
        
        i = d.cut_float(i)
        d.transform(quel[pos],"fade",i)
        d.draw(quel[pos],quel_r[pos])
        d.text(str(i),25,(255,255,255),[50,50],2,True)
        d.text(str(pos),25,(255,255,255),[100,100],2,True)
        while True:
            if pygame.key.get_pressed()[pygame.K_0]:
                break
            d.update()
    while True:
        test()
        
        FPS()
        d.update()
else:                                                                                           #Testcode
    pass
#-----------------------------------------------------------------------------------------------------------------------#