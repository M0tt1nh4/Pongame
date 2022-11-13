from tabnanny import check
from graphics import *
import random

class Reso:
    def Resolucao(resolucaoX, resolucaoY):
        if resolucaoX == 1366 and resolucaoY == 700:
            resolucao_mod1 = 670
            resolucao_mod2 = 400
            resolucao_abr1 = 660
            resolucao_abr2 = 100
            resolucao_crl1 = 575
            resolucao_crl2 = 593
            resolucao_start1 = 680
            resolucao_count1 = 680
            resolucao_barradown = 680
            resolucao_barrax1 = 691
            y = 33
        if resolucaoX == 1280 and resolucaoY == 650:
            resolucao_mod1 = 600
            resolucao_mod2 = 400
            resolucao_abr1 = 590
            resolucao_abr2 = 100
            resolucao_crl1 = 505
            resolucao_crl2 = 523
            resolucao_start1 = 610
            resolucao_count1 = 610
            resolucao_barradown = 630
            resolucao_barrax1 = 641
            y = 31
        if resolucaoX == 1024 and resolucaoY == 630:
            resolucao_mod1 = 500
            resolucao_mod2 = 400
            resolucao_abr1 = 490
            resolucao_abr2 = 100
            resolucao_crl1 = 405
            resolucao_crl2 = 423
            resolucao_start1 = 510
            resolucao_count1 = 510
            resolucao_barradown = 610
            resolucao_barrax1 = 626
            y = 30
        if resolucaoX == 800 and resolucaoY == 600:
            resolucao_mod1 = 390
            resolucao_mod2 = 400
            resolucao_abr1 = 380
            resolucao_abr2 = 100
            resolucao_crl1 = 295
            resolucao_crl2 = 313
            resolucao_start1 = 400
            resolucao_count1 = 400
            resolucao_barradown = 580
            resolucao_barrax1 = 591
            y = 28
        return [resolucao_mod1, resolucao_mod2, resolucao_abr1, resolucao_abr2, resolucao_crl1, resolucao_crl2, resolucao_start1, resolucao_count1, resolucao_barradown, resolucao_barrax1, y]

class explo:
    def explosao(jan, col, lin):
        for i in range (0, 201, 4):
            circle2 = Circle(Point(col, lin), i)
            circle2.draw(jan)
            circle2.setWidth(8)
            circle2.setOutline("Red")
            time.sleep(0.03)
            circle2.undraw()
        return

class GameOver:
    def final(win, resolucaoX, resolucaoY, pts, pts1, check):
        if check == 0:
            ret4 = Rectangle(Point(0, 0), Point(resolucaoX, resolucaoY))
            ret4.setFill('Black')
            ret4.draw(win)
            on = True
            count = 0
            if pts >= pts1:
                while on:
                    cor = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    go = Text(Point(resolucaoX/2, resolucaoY/2), 'GAME OVER')
                    go.setSize(30)
                    go.setFill(cor)
                    go.draw(win)
                    time.sleep(0.04)
                    count += 1
                    if count == 100:
                        on = False
            elif pts1 >= pts:
                while on:
                    cor = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    go = Text(Point(resolucaoX/2, resolucaoY/2), 'FREAK MONSTER WINS')
                    go.setSize(30)
                    go.setFill(cor)
                    go.draw(win)
                    time.sleep(0.04)
                    count += 1
                    if count == 100:
                        on = False
        else:
            ret4 = Rectangle(Point(0, 0), Point(resolucaoX, resolucaoY))
            ret4.setFill('Black')
            ret4.draw(win)
            on = True
            count = 0
            if pts >= pts1:
                while on:
                    cor = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    go = Text(Point(resolucaoX/2, resolucaoY/2), 'PLAYER 1 WINS')
                    go.setSize(30)
                    go.setFill(cor)
                    go.draw(win)
                    time.sleep(0.04)
                    count += 1
                    if count == 100:
                        on = False
            elif pts1 >= pts:
                while on:
                    cor = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    go = Text(Point(resolucaoX/2, resolucaoY/2), 'PLAYER 2 WINS')
                    go.setSize(30)
                    go.setFill(cor)
                    go.draw(win)
                    time.sleep(0.04)
                    count += 1
                    if count == 100:
                        on = False
        return
