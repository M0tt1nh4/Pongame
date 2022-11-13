import random
import funcaopong
from graphics import *

resolucaoX = 800
resolucaoY = 600
jan = GraphWin("launcher", 800, 600)
jan.setBackground("Black")

upline = Line(Point(0, 10), Point(800, 10))
upline.setWidth(10)
upline.setFill("White")
upline.draw(jan)

resolucao = Text(Point(380, 100), "Resolução")
resolucao.setSize(36)
resolucao.setFill("White")
resolucao.draw(jan)

resolucao1 = Text(Point(380, 200), "1366 x 700")
resolucao1.setSize(18)
resolucao1.setFill("White")
resolucao1.draw(jan)

resolucao2 = Text(Point(380, 250), "1280 x 650")
resolucao2.setSize(18)
resolucao2.setFill("White")
resolucao2.draw(jan)

resolucao4 = Text(Point(380, 300), "1024 x 630")
resolucao4.setSize(18)
resolucao4.setFill("White")
resolucao4.draw(jan)

resolucao5 = Text(Point(380, 350), "800 x 600")
resolucao5.setSize(18)
resolucao5.setFill("White")
resolucao5.draw(jan)

col = 300
lin = 200
pt = Point(col, lin)
select = Circle(pt, 6)
select.setFill("white")
select.draw(jan)

loline = Line(Point(0, 590), Point(800, 590))
loline.setWidth(10)
loline.setFill("White")
loline.draw(jan)
escolher = True
while escolher:
    tecla1 = jan.checkKey()
    if tecla1 == "Up" and lin > 200:
        lin -= 50
        select.undraw()
        select = Circle(Point(300, lin), 6)
        select.setFill("White")
        select.draw(jan)
    if tecla1 == "Down" and lin < 350:
        lin += 50
        select.undraw()
        select = Circle(Point(300, lin), 6)
        select.setFill("White")
        select.draw(jan)
    if tecla1 == "Return":
        jan.close()
        if lin == 200:
            resolucaoX = 1366
            resolucaoY = 700
        elif lin == 250:
            resolucaoX = 1280
            resolucaoY = 650
        elif lin == 300:
            resolucaoX = 1024
            resolucaoY = 630
        elif lin == 350:
            resolucaoX = 800
            resolucaoY = 600
        break
lista = funcaopong.Reso.Resolucao(resolucaoX, resolucaoY)

jan = GraphWin("Game Pong", resolucaoX, resolucaoY)
jan.setBackground("Black")

cor = ["White", "Black"]
x = 0
for i in range(0, lista[10]):
    ret1 = i * 20 + 20
    ret = Rectangle(Point(resolucaoX / 2, ret1), Point(resolucaoX / 2 + 10, ret1 + 20))
    ret.setFill(cor[x])
    ret.draw(jan)
    if x == 0:
        x += 1
    elif x == 1:
        x -= 1

upline = Line(Point(0, 10), Point(resolucaoX, 10))
upline.setWidth(10)
upline.setFill("White")
upline.draw(jan)

loline = Line(Point(0, resolucaoY - 10), Point(resolucaoX, resolucaoY - 10))
loline.setWidth(10)
loline.setFill("White")
loline.draw(jan)

col = resolucaoX / 2
lin = resolucaoY / 2
raio = 10
cir = Circle(Point(col, lin), raio)
cir.setFill("White")
cir.draw(jan)

colIni = 20
linIni = resolucaoY / 2 - 35
barra = Line(Point(colIni, linIni), Point(colIni, linIni + 70))
barra.setFill("White")
barra.setWidth(10)
barra.draw(jan)

colIni1 = resolucaoX - 20
linIni1 = resolucaoY / 2 - 35
barra1 = Line(Point(colIni1, linIni), Point(colIni1, linIni + 70))
barra1.setFill("White")
barra1.setWidth(10)
barra1.draw(jan)

pts = 0
pontos = Text(Point(resolucaoX / 2 - 100, 100), str(pts))
pontos.setSize(35)
pontos.setFill("White")
pontos.draw(jan)

pts1 = 0
pontos1 = Text(Point(resolucaoX / 2 + 100, 100), str(pts1))
pontos1.setSize(35)
pontos1.setFill("White")
pontos1.draw(jan)

ret3 = Rectangle(Point(0, 0), Point(1366, 768))
ret3.setFill("Black")
ret3.draw(jan)
abertura = "BEM VINDO AO NOSSO JOGO\n\n Selecione o modo de jogo"
abr = Text(Point(lista[2], lista[3]), abertura)
abr.setSize(16)
abr.setFill("White")
abr.draw(jan)
modo = "Player 1 Vs Computador\n\n Player 1 Vs Player 2"
md1 = Text(Point(lista[0], lista[1]), modo)
md1.setSize(12)
md1.setFill("White")
md1.draw(jan)

select = Circle(Point(lista[4], 381), 6)
select.setFill("White")
select.draw(jan)

check = 0
escolher = True
while escolher:
    tecla1 = jan.checkKey()
    if tecla1 == "Up" or tecla1 == "w":
        select.undraw()
        select = Circle(Point(lista[4], 381), 6)
        select.setFill("White")
        select.draw(jan)
        check = 0
    if tecla1 == "Down" or tecla1 == "s":
        select.undraw()
        select = Circle(Point(lista[5], 416), 6)
        select.setFill("White")
        select.draw(jan)
        check = 1
    if tecla1 == "Return" and check == 0:
        abr.undraw()
        select.undraw()
        md1.undraw()
        escolher = False
    if tecla1 == "Return" and check == 1:
        abr.undraw()
        select.undraw()
        md1.undraw()
        escolher = False
    if tecla1 == "Escape":
        escolher = False
        jan.close()
start = Text(Point(lista[6], 270), "START")
start.setSize(28)
start.setFill("White")
start.draw(jan)
for z in range(4, 1, -1):
    ct = z - 1
    countdown = Text(Point(lista[7], 310), str(ct))
    countdown.setSize(28)
    countdown.setFill("White")
    countdown.draw(jan)
    time.sleep(1)
    countdown.undraw()
start.undraw()
ret3.undraw()

defi = True
continuar = True
updown = 0
count = 0
passo = 10
ciclos = 0
while continuar:
    pontos.undraw()
    pontos = Text(Point(resolucaoX / 2 - 100, 100), str(pts))
    pontos.setSize(35)
    pontos.setFill("White")
    pontos.draw(jan)
    pontos1.undraw()
    pontos1 = Text(Point(resolucaoX / 2 + 100, 100), str(pts1))
    pontos1.setSize(35)
    pontos1.setFill("White")
    pontos1.draw(jan)

    if defi:
        passo = 10
        updown = random.randint(0, 1)
        if updown < 0.5:
            updown = 5
        else:
            updown = -5
        defi = False

    if passo > 30:
        count = 0
        passo = 30
    if count == 500:
        passo = passo * 1.5
        count = 0
        ciclos += 1

    col -= passo
    lin += updown
    cir.undraw()
    cir = Circle(Point(col, lin), raio)
    cir.setFill("White")
    cir.draw(jan)

    if (lin - raio) <= 20:
        updown = -updown

    if (lin + raio) >= lista[8]:
        updown = -updown

    if col - raio<= colIni + 10 and (lin + raio) >= linIni and (lin + raio) <= (linIni + 70):
        passo = -passo
    if col + raio  >= colIni1 - 10 and (lin + raio) >= linIni1 and (lin + raio) <= (linIni1 + 70):
        passo = -passo

    if col - raio <= 0:
        pts1 += 1
        ret2 = Rectangle(Point(resolucaoX / 2 - 30, resolucaoY / 2 - 100),
                         Point(resolucaoX / 2 + 90, resolucaoY / 2 + 90))
        ret2.setFill("Black")
        funcaopong.explo.explosao(jan, col, lin)
        ret2.draw(jan)
        col = resolucaoX / 2
        lin = resolucaoY / 2
        after = Text(Point(resolucaoX / 2 - 10, resolucaoY / 2), '''         Pressione Enter para continuar
       Pressione ESC para finalizar''')
        after.setSize(16)
        after.setFill("White")
        after.draw(jan)
        continuar2 = True
        while continuar2:
            tecla2 = jan.checkKey()
            if tecla2 == "Return":
                defi = True
                after.undraw()
                ret2.undraw()
                continuar = True
                continuar2 = False
                continue
            elif tecla2 == "Escape":
                over = funcaopong.GameOver.final(jan, resolucaoX, resolucaoY, pts, pts1, check)
                continuar = False
                continuar2 = False

    if col + raio >= resolucaoX:
        pts += 1
        ret2 = Rectangle(Point(resolucaoX / 2 - 30, resolucaoY / 2 - 100),
                         Point(resolucaoX / 2 + 90, resolucaoY / 2 + 90))
        ret2.setFill("Black")
        funcaopong.explo.explosao(jan, col, lin)
        ret2.draw(jan)
        col = resolucaoX / 2
        lin = resolucaoY / 2
        after = Text(Point(resolucaoX / 2 - 10, resolucaoY / 2), '''         Pressione Enter para continuar
             Pressione ESC para finalizar''')
        after.setSize(16)
        after.setFill("White")
        after.draw(jan)
        continuar2 = True
        while continuar2:
            tecla2 = jan.checkKey()
            if tecla2 == "Return":
                defi = True
                after.undraw()
                ret2.undraw()
                continuar = True
                continuar2 = False
                continue
            elif tecla2 == "Escape":
                over = funcaopong.GameOver.final(jan, resolucaoX, resolucaoY, pts, pts1, check)
                barra1.undraw()
                barra.undraw()
                continuar = False
                continuar2 = False
    tecla = jan.checkKey()

    if tecla == "Escape":
        continuar = False
        continue
    if tecla == "Up":
        if (linIni1 - 30) > 9:
            linIni1 -= 20
        else:
            linIni1 = 20

        barra1.undraw()
        barra1 = Line(Point(colIni1, linIni1), Point(colIni1, linIni1 + 70))
        barra1.setFill("White")
        barra1.setWidth(10)
        barra1.draw(jan)

    if tecla == "Down":
        if (linIni1 + 30 + 70) < lista[9]:
            linIni1 += 20
        else:
            linIni1 = lista[9] - 20 - 70

        barra1.undraw()
        barra1 = Line(Point(colIni1, linIni1), Point(colIni1, linIni1 + 70))
        barra1.setFill("White")
        barra1.setWidth(10)
        barra1.draw(jan)

    if check == 1:
        if tecla == "w":
            if (linIni - 20) > 9:
                linIni -= 20
            else:
                linIni = 20

            barra.undraw()
            barra = Line(Point(20, linIni), Point(20, linIni + 70))
            barra.setFill("White")
            barra.setWidth(10)
            barra.draw(jan)

        if tecla == "s":
            if (linIni + 20 + 70) < lista[9]:
                linIni += 20
            else:
                linIni = lista[9] - 20 - 70

            barra.undraw()
            barra = Line(Point(20, linIni), Point(20, linIni + 70))
            barra.setFill("White")
            barra.setWidth(10)
            barra.draw(jan)

    else:
        linIni = lin
        if (linIni + 35) >= lista[8]:
            linIni = lista[8] + 30 - 70
        if (linIni - 30) <= 20:
            linIni = 50
        barra.undraw()
        barra = Line(Point(20, linIni - 30), Point(20, linIni + 70 - 30))
        barra.setFill("White")
        barra.setWidth(10)
        barra.draw(jan)
    count += 1

    time.sleep(0.07)
jan.close()
