import pygame
import lib
from game import start
pygame.init()
#-- Debug --------------------------------------------------------------------------------------------------------------#
Start = True #Kein Crash
Objekte = True #Kein Crash (False = Alternativer Code)
Inhalte = True
ingame = True #Kein Crash (False = Alternativer Code)
level_auswahl = False #Kein Crash
#-----------------------------------------------------------------------------------------------------------------------#



#-- Game.py ------------------------------------------------------------------------------------------------------------#
if Start:                                                                                                               #Hauptmenü -> Charakter Auswahl
    if start.menu():
        ausgwählt = [(start.select()),(start.select())]
else:
    ausgwählt = lib.d.sett.game["opps"]
#-----------------------------------------------------------------------------------------------------------------------#


#-- Inhalte ------------------------------------------------------------------------------------------------------------#
if Inhalte:                                                                                                             #Bilder, Sounds, Positionen ect.
    class a1: #Alles andere
        lib.d.pygame() #Fenster neustarten

        random_variable = 0
        turn = lib.d.sett.game["beginning_player"]

        ticks = 0.0
        tick_limit = 36.0


        

    class char: #Aussehen Spieler
        gr = {
            "x": int(lib.d.sett.fenster.width*0.14),
            "y": int(lib.d.sett.fenster.height*0.45),
        }

        ps_r = { #Position
            "x": int(lib.d.sett.fenster.width*0.75),
            "y": int(lib.d.sett.fenster.height*0.85),
        }
        ps_l = {
            "x": int(lib.d.sett.fenster.width*0.25),
            "y": int(lib.d.sett.fenster.height*0.85),
        }


        SRechts = [
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[0]}/{ausgwählt[0]}_0r.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[0]}/{ausgwählt[0]}_1r.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[0]}/{ausgwählt[0]}_2r.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[0]}/{ausgwählt[0]}_3r.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[0]}/{ausgwählt[0]}_4r.png'),eingabe=[gr["x"],gr["y"]]),
        ]

        SRechts_r = [
            lib.d.rect(SRechts[0],[ps_r["x"],ps_r["y"]],8),
            lib.d.rect(SRechts[1],[ps_r["x"],ps_r["y"]],8),
            lib.d.rect(SRechts[2],[ps_r["x"],ps_r["y"]],8),
            lib.d.rect(SRechts[3],[ps_r["x"],ps_r["y"]],8),
            lib.d.rect(SRechts[4],[ps_r["x"],ps_r["y"]],8),
        ]


        SLinks = [
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[1]}/{ausgwählt[1]}_0l.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[1]}/{ausgwählt[1]}_1l.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[1]}/{ausgwählt[1]}_2l.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[1]}/{ausgwählt[1]}_3l.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'char/rapper/{ausgwählt[1]}/{ausgwählt[1]}_4l.png'),eingabe=[gr["x"],gr["y"]]),
        ]

        SLinks_r = [
            lib.d.rect(SLinks[0],[ps_l["x"],ps_l["y"]],8),
            lib.d.rect(SLinks[1],[ps_l["x"],ps_l["y"]],8),
            lib.d.rect(SLinks[2],[ps_l["x"],ps_l["y"]],8),
            lib.d.rect(SLinks[3],[ps_l["x"],ps_l["y"]],8),
            lib.d.rect(SLinks[4],[ps_l["x"],ps_l["y"]],8),
        ]


    class ui_a: #arrows
        Rechts = True
        Links = False

        dic = {
            "o": 0,
            "r": 1,
            "l": 2,
            "u": 3,
        }
        ps = { #Position
            "Links": [
                int(lib.d.sett.fenster.width*0.1041+1),
                int(lib.d.sett.fenster.width*0.156+1),
                int(lib.d.sett.fenster.width*0.052+1),
                int(lib.d.sett.fenster.width*0.208+1),
            ],

            "Rechts": [
                int(lib.d.sett.fenster.width*0.843+1),
                int(lib.d.sett.fenster.width*0.895+1),
                int(lib.d.sett.fenster.width*0.791+1),
                int(lib.d.sett.fenster.width*0.947+1),
            ],
            "y": int(lib.d.sett.fenster.height*0.09259),
        }
        gr = { #Größe
            "x": int(lib.d.sett.fenster.width*0.052),
            "y": int(lib.d.sett.fenster.width*0.052),
        }


        weiß = [ #Aktiv
            lib.d.transform(load=lib.d.image_load(f'ui/up.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'ui/right.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'ui/left.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'ui/down.png'),eingabe=[gr["x"],gr["y"]]),
        ]

        grau = [ #Gedrückt
            lib.d.transform(load=lib.d.image_load(f'ui/up_p.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'ui/right_p.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'ui/left_p.png'),eingabe=[gr["x"],gr["y"]]),
            lib.d.transform(load=lib.d.image_load(f'ui/down_p.png'),eingabe=[gr["x"],gr["y"]]),
        ]

        leer = [ #Inaktiv
            lib.d.transform(load=grau[0],type="opacity",eingabe=100),
            lib.d.transform(load=grau[1],type="opacity",eingabe=100),
            lib.d.transform(load=grau[2],type="opacity",eingabe=100),
            lib.d.transform(load=grau[3],type="opacity",eingabe=100),
        ]



        weiß_r = [
            lib.d.rect(weiß[dic["o"]],cordi=[ps["Rechts"][dic["o"]],ps["y"]],anker=0),
            lib.d.rect(weiß[dic["r"]],cordi=[ps["Rechts"][dic["r"]],ps["y"]],anker=0),
            lib.d.rect(weiß[dic["l"]],cordi=[ps["Rechts"][dic["l"]],ps["y"]],anker=0),
            lib.d.rect(weiß[dic["u"]],cordi=[ps["Rechts"][dic["u"]],ps["y"]],anker=0),
        ]

        grau_r = [
            lib.d.rect(grau[dic["o"]],cordi=[ps["Rechts"][dic["o"]],ps["y"]],anker=0),
            lib.d.rect(grau[dic["r"]],cordi=[ps["Rechts"][dic["r"]],ps["y"]],anker=0),
            lib.d.rect(grau[dic["l"]],cordi=[ps["Rechts"][dic["l"]],ps["y"]],anker=0),
            lib.d.rect(grau[dic["u"]],cordi=[ps["Rechts"][dic["u"]],ps["y"]],anker=0),
        ]

        leer_r = [
            lib.d.rect(leer[dic["o"]],cordi=[ps["Rechts"][dic["o"]],ps["y"]],anker=0),
            lib.d.rect(leer[dic["r"]],cordi=[ps["Rechts"][dic["r"]],ps["y"]],anker=0),
            lib.d.rect(leer[dic["l"]],cordi=[ps["Rechts"][dic["l"]],ps["y"]],anker=0),
            lib.d.rect(leer[dic["u"]],cordi=[ps["Rechts"][dic["u"]],ps["y"]],anker=0),
        ]



        weiß_l = [
            lib.d.rect(weiß[dic["o"]],cordi=[ps["Links"][dic["o"]],ps["y"]],anker=0),
            lib.d.rect(weiß[dic["r"]],cordi=[ps["Links"][dic["r"]],ps["y"]],anker=0),
            lib.d.rect(weiß[dic["l"]],cordi=[ps["Links"][dic["l"]],ps["y"]],anker=0),
            lib.d.rect(weiß[dic["u"]],cordi=[ps["Links"][dic["u"]],ps["y"]],anker=0),
        ]

        grau_l= [
            lib.d.rect(grau[dic["o"]],cordi=[ps["Links"][dic["o"]],ps["y"]],anker=0),
            lib.d.rect(grau[dic["r"]],cordi=[ps["Links"][dic["r"]],ps["y"]],anker=0),
            lib.d.rect(grau[dic["l"]],cordi=[ps["Links"][dic["l"]],ps["y"]],anker=0),
            lib.d.rect(grau[dic["u"]],cordi=[ps["Links"][dic["u"]],ps["y"]],anker=0),
        ]

        leer_l = [
            lib.d.rect(leer[dic["o"]],cordi=[ps["Links"][dic["o"]],ps["y"]],anker=0),
            lib.d.rect(leer[dic["r"]],cordi=[ps["Links"][dic["r"]],ps["y"]],anker=0),
            lib.d.rect(leer[dic["l"]],cordi=[ps["Links"][dic["l"]],ps["y"]],anker=0),
            lib.d.rect(leer[dic["u"]],cordi=[ps["Links"][dic["u"]],ps["y"]],anker=0),
        ]


    class Lvl1: #Level1 - Hood
        behindTrain = lib.d.transform(lib.d.image_load('background/1/behindTrain.png'))
        city = lib.d.transform(lib.d.image_load('background/1/city.png'))
        sky = lib.d.transform(lib.d.image_load('background/1/sky.png'))
        street = lib.d.transform(lib.d.image_load('background/1/street.png'))

        behindTrain_r = lib.d.rect(behindTrain)
        city_r = lib.d.rect(city)
        sky_r = lib.d.rect(sky)
        street_r = lib.d.rect(street)

        class train:
            pos = -5000
            pos_limit = 40000
            speed = 50
            obj = lib.d.transform(lib.d.image_load('background/1/train.png'))

            
        class window:
            fenster_farbe = 0
            ticks = 0
            win = {
                0: lib.d.transform(lib.d.image_load('background/1/win0.png')),
                1: lib.d.transform(lib.d.image_load('background/1/win1.png')),
                2: lib.d.transform(lib.d.image_load('background/1/win2.png')),
                3: lib.d.transform(lib.d.image_load('background/1/win3.png')),
                4: lib.d.transform(lib.d.image_load('background/1/win4.png')),
            }
            win_r = {
                0: lib.d.rect(win[0]),
                1: lib.d.rect(win[1]),
                2: lib.d.rect(win[2]),
                3: lib.d.rect(win[3]),
                4: lib.d.rect(win[4]),
            }

        class play:
            y_grenze = lib.d.sett.fenster.height+400
            rate = 125
            spiel_dauer = 90
            x_timer = 200
            height = [
                lib.d.sett.fenster.height+x_timer,
            ]

            for random_variable in range(0,spiel_dauer):
                height.append(height[random_variable]+rate)


        def anim_train():
            if Lvl1.train.pos > Lvl1.train.pos_limit:
                Lvl1.train.pos = -4000
            else:
                Lvl1.train.pos += Lvl1.train.speed

            lib.d.draw(Lvl1.train.obj,lib.d.rect(load=Lvl1.train.obj,cordi=[Lvl1.train.pos,0]))


        def anim_window():
            if Lvl1.window.ticks >= lib.d.sett.base['ticks_limit']:
                Lvl1.window.ticks = 0
            else:
                Lvl1.window.ticks += 0.1
                Lvl1.window.ticks = lib.d.cut_float(Lvl1.window.ticks)

            if Lvl1.window.ticks % 5.0 == 0:
                if Lvl1.window.fenster_farbe >= (len(Lvl1.window.win)-1):
                    Lvl1.window.fenster_farbe = 0
                else:
                    Lvl1.window.fenster_farbe += 1
            return lib.d.draw(Lvl1.window.win[Lvl1.window.fenster_farbe],Lvl1.window.win_r[Lvl1.window.fenster_farbe])
    class lvl2: #Level2 - Autobahn(im Moment Bühne)
        pass
    class lvl3: #Level3 - ???
        pass

class arrow: #Für Animation Pfeile berechnung
    unter_grenze = 30
    obere_grenze = 230
    ende = -20
    def __init__(self,height:int=0,pdr:int=0):
        self.height = height

        if a1.turn:
            xpos = ui_a.ps["Rechts"][pdr]
        else:
            xpos = ui_a.ps["Links"][pdr]
    
        wrect = lib.d.rect(load=ui_a.weiß[pdr],cordi=[xpos,self.height],anker=5)
        lib.d.draw(load=ui_a.weiß[pdr],rect=wrect)
#-----------------------------------------------------------------------------------------------------------------------#



#-- Map    -------------------------------------------------------------------------------------------------------------#
class b:                                                                                                                #Starten
    level = ["hood","auto","???"]
    level = 1
#-----------------------------------------------------------------------------------------------------------------------#



#-- Loop ---------------------------------------------------------------------------------------------------------------#
if Objekte: #Hauptcode


    #Ingame
    if b.level == 1: #Level0 - Hood
        spieler = lib.d.sett.game['beginning_player']
        def anim_back():                                                                    #Animation von Hintergrund
            lib.d.draw(Lvl1.sky,Lvl1.sky_r)
            lib.d.draw(Lvl1.city,Lvl1.city_r)
            Lvl1.anim_window()
            lib.d.draw(Lvl1.behindTrain,Lvl1.behindTrain_r)
            Lvl1.anim_train()
            lib.d.draw(Lvl1.street,Lvl1.street_r)
        def anim_char():                                                                    #Animation von Spieler und weiße Pfeile
            keys = lib.d.sett.key()
            if a1.turn == True: #Animation zu input / Rechts
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]: #Rechts
                    lib.d.draw(ui_a.grau[1],ui_a.grau_r[1])
                else:
                    lib.d.draw(ui_a.weiß[1],ui_a.weiß_r[1])

                if keys[pygame.K_UP] or keys[pygame.K_w]: #Oben
                    lib.d.draw(ui_a.grau[0],ui_a.grau_r[0])
                else:
                    lib.d.draw(ui_a.weiß[0],ui_a.weiß_r[0])

                if keys[pygame.K_DOWN] or keys[pygame.K_s]: #Unten
                    lib.d.draw(ui_a.grau[3],ui_a.grau_r[3])
                else:
                    lib.d.draw(ui_a.weiß[3],ui_a.weiß_r[3])

                if keys[pygame.K_LEFT] or keys[pygame.K_a]: #Links
                    lib.d.draw(ui_a.grau[2],ui_a.grau_r[2])
                else:
                    lib.d.draw(ui_a.weiß[2],ui_a.weiß_r[2])

                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    lib.d.draw(char.SRechts[1],char.SRechts_r[1])
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    lib.d.draw(char.SRechts[2],char.SRechts_r[2])
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    lib.d.draw(char.SRechts[3],char.SRechts_r[3])
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    lib.d.draw(char.SRechts[4],char.SRechts_r[4])
                else:
                    lib.d.draw(char.SRechts[0],char.SRechts_r[0])

            else:
                lib.d.draw(ui_a.leer[0],ui_a.leer_r[0])
                lib.d.draw(ui_a.leer[1],ui_a.leer_r[1])
                lib.d.draw(ui_a.leer[2],ui_a.leer_r[2])
                lib.d.draw(ui_a.leer[3],ui_a.leer_r[3])
                lib.d.draw(char.SRechts[0],char.SRechts_r[0])


            if a1.turn == False: #Animation zu input / Links
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]: #Rechts
                    lib.d.draw(ui_a.grau[1],ui_a.grau_l[1])
                else:
                    lib.d.draw(ui_a.weiß[1],ui_a.weiß_l[1])

                if keys[pygame.K_UP] or keys[pygame.K_w]: #Oben
                    lib.d.draw(ui_a.grau[0],ui_a.grau_l[0])
                else:
                    lib.d.draw(ui_a.weiß[0],ui_a.weiß_l[0])

                if keys[pygame.K_DOWN] or keys[pygame.K_s]: #Unten
                    lib.d.draw(ui_a.grau[3],ui_a.grau_l[3])
                else:
                    lib.d.draw(ui_a.weiß[3],ui_a.weiß_l[3])

                if keys[pygame.K_LEFT] or keys[pygame.K_a]: #Links
                    lib.d.draw(ui_a.grau[2],ui_a.grau_l[2])
                else:
                    lib.d.draw(ui_a.weiß[2],ui_a.weiß_l[2])

                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    lib.d.draw(char.SLinks[1],char.SLinks_r[1])
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    lib.d.draw(char.SLinks[2],char.SLinks_r[2])
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    lib.d.draw(char.SLinks[3],char.SLinks_r[3])
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    lib.d.draw(char.SLinks[4],char.SLinks_r[4])
                else:
                    lib.d.draw(char.SLinks[0],char.SLinks_r[0])

            else:
                lib.d.draw(ui_a.leer[0],ui_a.leer_l[0])
                lib.d.draw(ui_a.leer[1],ui_a.leer_l[1])
                lib.d.draw(ui_a.leer[2],ui_a.leer_l[2])
                lib.d.draw(ui_a.leer[3],ui_a.leer_l[3])
                lib.d.draw(char.SLinks[0],char.SLinks_r[0])

        if ingame:
            while True:
                lib.d.sett.game["key"] = pygame.key.get_pressed()
                anim_back()
                anim_char()
                a1.random_variable = 0
                for temp_time in Lvl1.play.height:
                    Lvl1.play.height[a1.random_variable] -= 10
                    a1.random_variable += 1
                run = [
                    arrow.up(Lvl1.play.height[0]),
                    arrow.right(Lvl1.play.height[1]),
                    arrow.left(Lvl1.play.height[2]),
                    arrow.left(Lvl1.play.height[3]),
                    arrow.up(Lvl1.play.height[4]),
                    arrow.down(Lvl1.play.height[5]),
                    arrow.up(Lvl1.play.height[8]),
                    arrow.down(Lvl1.play.height[9]),
                    arrow.left(Lvl1.play.height[11]),
                    arrow.left(Lvl1.play.height[15]),
                    arrow.left(Lvl1.play.height[16]),
                    arrow.left(Lvl1.play.height[17]),
                    arrow.up(Lvl1.play.height[17]),
                    arrow.down(Lvl1.play.height[19]),
                    arrow.down(Lvl1.play.height[20]),
                    arrow.down(Lvl1.play.height[21]),
                    arrow.right(Lvl1.play.height[23]),
                    arrow.right(Lvl1.play.height[24]),
                    arrow.right(Lvl1.play.height[25]),
                    arrow.up(Lvl1.play.height[26]),
                    arrow.right(Lvl1.play.height[27]),
                    arrow.left(Lvl1.play.height[28]),
                    arrow.left(Lvl1.play.height[29]),
                    arrow.up(Lvl1.play.height[30]),
                    arrow.down(Lvl1.play.height[32]),
                    arrow.up(Lvl1.play.height[33]),
                    arrow.down(Lvl1.play.height[35]),
                    arrow.left(Lvl1.play.height[35]),
                    arrow.left(Lvl1.play.height[36]),
                    arrow.left(Lvl1.play.height[37]),
                    arrow.left(Lvl1.play.height[38]),
                    arrow.up(Lvl1.play.height[39]),
                    arrow.down(Lvl1.play.height[39]),
                    arrow.down(Lvl1.play.height[40]),
                    arrow.down(Lvl1.play.height[41]),
                    arrow.right(Lvl1.play.height[41]),
                    arrow.right(Lvl1.play.height[42]),
                    arrow.right(Lvl1.play.height[43]),

                ]
                lib.FPS()
                lib.d.update()
        else:
            while True:
                print("real")
                anim_back()
                anim_char()

                a1.random_variable = 0
                for temp_time in Lvl1.play.height:
                    Lvl1.play.height[a1.random_variable] -= 10
                    a1.random_variable += 1
                run = [
                    arrow(Lvl1.play.height[0],0),
                    arrow(Lvl1.play.height[1],2),
                    arrow(Lvl1.play.height[2],2),
                    arrow(Lvl1.play.height[3],2),
                    arrow(Lvl1.play.height[4],0),
                    arrow(Lvl1.play.height[5],3),
                    arrow(Lvl1.play.height[8],0),
                    arrow(Lvl1.play.height[9],3),
                    arrow(Lvl1.play.height[11],2),
                    arrow(Lvl1.play.height[15],2),
                    arrow(Lvl1.play.height[16],2),
                    arrow(Lvl1.play.height[17],2),
                    arrow(Lvl1.play.height[17],0),
                    arrow(Lvl1.play.height[19],3),
                    arrow(Lvl1.play.height[20],3),
                    arrow(Lvl1.play.height[21],3),
                    arrow(Lvl1.play.height[23],1),
                    arrow(Lvl1.play.height[24],1),
                    arrow(Lvl1.play.height[25],1),
                    arrow(Lvl1.play.height[26],0),
                    arrow(Lvl1.play.height[27],1),
                    arrow(Lvl1.play.height[28],2),
                    arrow(Lvl1.play.height[29],2),
                    arrow(Lvl1.play.height[30],0),
                    arrow(Lvl1.play.height[32],3),
                    arrow(Lvl1.play.height[33],0),
                    arrow(Lvl1.play.height[35],3),
                    arrow(Lvl1.play.height[35],2),
                    arrow(Lvl1.play.height[36],2),
                    arrow(Lvl1.play.height[37],2),
                    arrow(Lvl1.play.height[38],2),
                    arrow(Lvl1.play.height[39],0),
                    arrow(Lvl1.play.height[39],3),
                    arrow(Lvl1.play.height[40],3),
                    arrow(Lvl1.play.height[41],3),
                    arrow(Lvl1.play.height[41],1),
                    arrow(Lvl1.play.height[42],1),
                    arrow(Lvl1.play.height[43],1),

                ]





                lib.FPS()
                lib.d.update()
                if lib.d.sett.key()[pygame.K_0]:
                    a1.turn = False
                elif lib.d.sett.key()[pygame.K_1]:
                    a1.turn = True
    elif b.level == 2: #Level1 - Auto
        pass
    elif b.level == 3: #Level2 - ???
        pass

else: #Testcode
    while True:
        lib.d.box(cordi=[20,20],filled=False,farbe=(255,255,255))

        lib.d.update()
#-----------------------------------------------------------------------------------------------------------------------#