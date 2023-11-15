Debugging = True
import time
import pygame
import random
from pygame import mixer
from sys import exit
pygame.init()

if Debugging:
    if "cos" == "cos":                                                                                      #custom functions
        def d_pygame(start:bool,breite:list,name:str):                                                          #Init oder QUIT pygame
            global fenster
            global clock
            if start: #Start Pygame
                pygame.init()
                fenster = pygame.display.set_mode((breite[0],breite[1]))
                pygame.display.set_caption(f'RAPBATTLES OF HISTORY - {name}')
            elif start == False: #Close Pygame
                pygame.quit()
            elif start == None: #Restart Pygame
                pygame.quit()
                pygame.init()
                fenster = pygame.display.set_mode((breite[0],breite[1]))
                pygame.display.set_caption(f'RAPBATTLES OF HISTORY - {name}')
            clock = pygame.time.Clock()
        def d_text(text:str,größe:int,farbe:list,cordi:list,font:int,AA:bool):                                  #Text erscheinen lassen
            all_fonts = ['assets/fonts/minecraft.ttf','assets/fonts/windows.ttf','assets/fonts/fnf.ttf'] #MC = 0,Windows = 1, FNF = 2
            schrift = pygame.font.Font(all_fonts[font],größe)
            fertigtext = schrift.render(text,AA,(farbe[0],farbe[1],farbe[2]))
            fenster.blit(fertigtext,(cordi[0],cordi[1]))
        def d_load(quelle):                                                                                     #Bild laden und zurückgeben
            return pygame.image.load(quelle).convert_alpha()
        def d_rect(quelle:str,welches:int,cordi:list):                                                          #Läd und gibt rect von Bild
            if welches == 1: #Topleft
                return d_load(quelle).get_rect(topleft = (cordi[0],cordi[1]))
            elif welches == 2: #Midtop
                return d_load(quelle).get_rect(midtop = (cordi[0],cordi[1]))
            elif welches == 3: #Topright
                return d_load(quelle).get_rect(topright = (cordi[0],cordi[1]))
            elif welches == 4: #Midleft
                return d_load(quelle).get_rect(midleft = (cordi[0],cordi[1]))
            elif welches == 5 or welches == 0: #Center
                return d_load(quelle).get_rect(center = (cordi[0],cordi[1]))
            elif welches == 6: #Midright
                return d_load(quelle).get_rect(midright = (cordi[0],cordi[1]))
            elif welches == 7: #Bottomleft
                return d_load(quelle).get_rect(bottomleft = (cordi[0],cordi[1]))
            elif welches == 8: #Midbottom
                return d_load(quelle).get_rect(midbottom = (cordi[0],cordi[1]))
            elif welches == 9: #Bottomright
                return d_load(quelle).get_rect(bottomright = (cordi[0],cordi[1]))
        def d_draw(quelle:str,cordi:list,rect:int):                                                             #Zeichnet und gibt ein Bild
            return fenster.blit(d_load(quelle),d_rect(quelle,rect,cordi))
        def d_update(FPS:int):                                                                                  #Update Display und Event
            if "End" == "End": #Wenn Fenster geschlossen wird, schließen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            if "Updater" == "Updater":
                pygame.display.update()
                clock.tick(FPS)
        def d_play_sound(quelle:str,ton:bool):                                                                  #Läd und spielt ton oder musik ab
            if ton: #Spielt einziges Ton
                geräusch = mixer.Sound(quelle)
                geräusch.play()
            else: #Spielt Musik bis Fenster geschlossen wird.
                mixer.music.load(quelle)
                mixer.music.play(-1)
        def d_random(upper:int,lower:int):                                                                      #Gibt Zahl zufällige int-zahl
            if lower > upper:
                return random.randint(lower,upper)
            elif upper > lower:
                return random.randint(upper,lower)
            else:
                print(f"Fehler in random.randint mit Input: {upper} und {lower}")
                return 0
    
    class beg: #beginn
        def d_appear(text:str,cordi:list,farbe:list,größe:int): #Lässt Text erscheinen
            container = text
            i = 0
            awn = ""
            while i < len(container):
                awn += container[i]
                i += 1
                d_text(f'{awn}',größe,[farbe[0],farbe[1],farbe[2]],[cordi[0],cordi[1]],2,True)
                d_update(60)
                time.sleep(0.05)
        def d_draw(quelle:str,cordi:list,rect:int):                                                             #Zeichnet und gibt ein Bild
            return fenster.blit(d_load(quelle),d_rect(quelle,rect,cordi))
    
    class start: #Startet Oberflächen
        def console():                                                                                          #Öffnet Konsole
            d_pygame(None,[1440,720],'Console') #Fenster öffnen Konsole
            d_draw('assets/bigblack.png',[0,0],1) #Fenster Hintergrund
            text = ["","","","","",""]
            i = 0
            loc = 50
            while True:
                d_update(60)
                keys = pygame.key.get_pressed()
                d_text('_ _ _ _ _',100,[255,255,255],[loc,50],1,False)
                if keys[pygame.K_a]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "a"
                    i += 1
                    loc += 50
                elif keys[pygame.K_b]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "b"
                    i += 1
                    loc += 50
                elif keys[pygame.K_c]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "c"
                    i += 1
                    loc += 50
                elif keys[pygame.K_d]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "d"
                    i += 1
                    loc += 50
                elif keys[pygame.K_e]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "e"
                    i += 1
                    loc += 50
                elif keys[pygame.K_f]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "f"
                    i += 1
                elif keys[pygame.K_g]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "g"
                    i += 1
                elif keys[pygame.K_h]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "h"
                    i += 1
                elif keys[pygame.K_i]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "i"
                    i += 1
                elif keys[pygame.K_j]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "j"
                    i += 1
                elif keys[pygame.K_k]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "k"
                    i += 1
                elif keys[pygame.K_l]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "l"
                    i += 1
                elif keys[pygame.K_m]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "m"
                    i += 1
                elif keys[pygame.K_n]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "n"
                    i += 1
                elif keys[pygame.K_o]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "o"
                    i += 1
                elif keys[pygame.K_p]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "p"
                    i += 1
                elif keys[pygame.K_q]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "q"
                    i += 1
                elif keys[pygame.K_r]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "r"
                    i += 1
                elif keys[pygame.K_s]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "s"
                    i += 1
                elif keys[pygame.K_t]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "t"
                    i += 1
                elif keys[pygame.K_u]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "u"
                    i += 1
                elif keys[pygame.K_v]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "v"
                    i += 1
                elif keys[pygame.K_w]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "w"
                    i += 1
                elif keys[pygame.K_x]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "x"
                    i += 1
                elif keys[pygame.K_y]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "y"
                    i += 1
                elif keys[pygame.K_z]:
                    d_draw('assets/blank.png',[loc,100],5)
                    text[i] = "z"
                    i += 1



        def menu():                                                                                             #Öffnet Menü
            #Beim Öffnen von Hauptmenü
            d_pygame(None,[1440,720],"Main Menu")
            #d_play_sound('assets/main_menu/music.ogg',False) #Menü Musik abspielen
            d_draw('assets/main_menu/menu.png',[720,360],0) #Hintergrund einfügen
            beg.d_appear("Rapbattles",[1050,100],[255,255,255],50) #Animation zum erscheinen von Text
            beg.d_appear("by Smelvin",[1200,150],[155,155,155],25) #Animation zum erscheinen von Test
            time.sleep(0.5) #Freez für Glatte Animation
            d_draw('assets/main_menu/1.png',[100,250],0) #Ausgewählte Option Pfeil
            beg.d_appear("START",[125,210],[255,255,255],70) #Option 1 Text mit Animation
            beg.d_appear("Options",[125,310],[155,155,155],50) #Option 2 Text mit Animation
            beg.d_appear("Quit",[125,410],[155,155,155],50) #Option 3 Text mit Animation
            
            def temp_menu():                                                                    #Hintergrund und credits zeichnen (ohne Animation)
                d_draw('assets/main_menu/menu.png',[720,360],0)
                d_text("Rapbattles",50,[255,255,255],[1050,100],2,True)
                d_text("by Smelvin",25,[155,155,155],[1200,150],2,True)
            
            pos = 1 #Aufgewählte Option (1=Start,2=Options,3=Quit)
            while True:                                                                         #Menu mit Animation und Input
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    if pos == 1:    	                                                        #Von "Start" zu "Quit"
                        y = 0 #Position vom Pfeil
                        g = 0 #Extra größe von ausgwählter Option
                        while y < 200: #Animation zu Pfeil (Oben nach Unten)
                            y += 40
                            if y%10==0: #Animation zu extra Größe
                                g += 2
                            #Zeichnet Hintergrund
                            temp_menu()
                            d_text("Start",50,[155,155,155],[125,210],2,True)
                            d_text("Options",50,[155,155,155],[125,310],2,True)
                            d_text("QUIT",(50+g),[255,255,255],[125,410],2,True)
                            d_draw(f'assets/main_menu/1.png',[100,(240+y)],0)
                            d_update(60)
                            pos = 3 #Wählt QUIT als Option aus
                    elif pos == 2:                                                              #Von "Options" zu "Start"
                        y = 0
                        g = 0
                        while y < 90:
                            y += 15
                            if g <= 25:
                                g += 4
                            temp_menu()
                            d_text("START",(50+g),[255,255,255],[125,210],2,True)
                            d_text("Options",50,[155,155,155],[125,310],2,True)
                            d_text("Quit",50,[155,155,155],[125,410],2,True)
                            d_draw(f'assets/main_menu/1.png',[100,(340-y)],0)
                            d_update(60)
                            pos = 1
                    elif pos == 3:                                                              #Von "Quit" zu "Options"
                        y = 0
                        g = 0
                        while y < 100:
                            y += 20
                            if y%5==0:
                                g += 1
                            temp_menu()
                            d_text("Start",50,[155,155,155],[125,210],2,True)
                            d_text("OPTIONS",(50+g),[255,255,255],[125,310],2,True)
                            d_text("Quit",50,[155,155,155],[125,410],2,True)
                            d_draw(f'assets/main_menu/1.png',[100,(440-y)],0)
                            d_update(60)
                            pos = 2
                d_update(60)
                if keys[pygame.K_RETURN]:
                    if pos == 1: 
                        d_play_sound('assets/main_menu/select.ogg',True)
                        temp_menu()
                        d_text("START",70,[255,255,255],[125,210],2,True)
                        d_text("Options",50,[155,155,155],[125,310],2,True)
                        d_text("Quit",50,[155,155,155],[125,410],2,True)
                        d_update(60)
                        beg.d_appear("START",[125,210],[255,0,255],70)
                        time.sleep(0.1)
                        beg.d_appear("START",[125,210],[145,255,0],70)
                        time.sleep(0.1)
                        beg.d_appear("START",[125,210],[0,217,255],70)
                        time.sleep(0.1)
                        beg.d_appear("START",[125,210],[153,0,255],70)
                        time.sleep(0.1)
                        return True
                    elif pos == 2:
                        d_play_sound('assets/main_menu/select.ogg',True)
                        d_pygame(None,[1440,720],"Debugging")
                        start.console()
                        return True
                    elif pos == 3:
                        d_play_sound('assets/main_menu/select.ogg',True)
                        time.sleep(0.3)
                        exit()
                d_update(60)



        def select():
            npcs = ["Jesus","Eminem","JohnnySins","Santa","Alzheimer","Lean"] #Liste aller Spielbaren Charakter
            farben = [(255,191,0),(224,215,186),(64,204,255),(252,63,63),(0,255,0),(255,0,255)] #Textfarben von Charaktern
            d_pygame(True,[1440,720],'Champ Select')
            d_update(60)
            d_draw(f'assets/select/login/{npcs[0]}.png',[720,360],0) #Zeichnet Bild von Jesus
            beg.d_appear("Select your champ",[465,75],[255,255,255],50) #Start Text mit Animation

            def temp_char():                                                                    #GUI in Charakterauswahl
                d_draw('assets/select/left.png',[125,360],0)
                d_draw('assets/select/right.png',[1315,360],0)
                d_text("Select your champ",50,[255,255,255],[465,75],2,True)
            i = 0 #Ausgewählter Charakter (0=Jesus,1=Eminem usw.)
            while True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT] or keys[pygame.K_a]:
                    d_play_sound('assets/select/scroll.ogg',True)
                    if (i+1) >= len(npcs):
                        i = 0
                    else:
                        i += 1
                    d_update(60)
                    d_draw(f'assets/select/login/{npcs[i]}.png',[720,360],0)
                    d_text("Select your champ",50,[255,255,255],[465,75],2,True)
                    d_draw('assets/select/right_pressed.png',[1315,360],0)
                    beg.d_appear(f'feat.  {npcs[i]}',[465,125],farben[i],25)
                    d_update(60)
                    time.sleep(0.2)
                elif keys[pygame.K_LEFT] or keys[pygame.K_d]:
                    d_play_sound('assets/select/scroll.ogg',True)
                    if i <= 0:
                        i = len(npcs)-1
                    else:
                        i -= 1
                    d_update(60)
                    d_draw(f'assets/select/login/{npcs[i]}.png',[720,360],0)
                    d_text("Select your champ",50,[255,255,255],[465,75],2,True)
                    d_draw('assets/select/left_pressed.png',[125,360],0)
                    beg.d_appear(f'feat.  {npcs[i]}',[465,125],farben[i],25)
                    d_update(60)
                    time.sleep(0.2)
                d_draw(f'assets/select/login/{npcs[i]}.png',[720,360],0)
                d_text(f"feat.  {npcs[i]}",25,farben[i],[465,125],2,True)
                temp_char()
                d_update(60)
                if keys[pygame.K_RETURN]:
                    d_play_sound('assets/main_menu/select.ogg',True) #Spielt Musik
                    return npcs[i]
