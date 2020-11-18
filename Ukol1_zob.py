import turtle
import math
from turtle import exitonclick, setpos, pendown, penup, speed
from math import log, cos, radians, tan, sin, cos, acos
# definice funkce lambertova valcoveho zobrazeni
def Lv(m,n,R):
    # spocteni uzivatelova bodu
    delka = R*radians(m)
    sirka = R*sin(radians(n))
    # vykresleni site
    k = range(-90,100,10)
    l = range(-180,190,10)
    speed(0)
    for j in k:
        penup()
        setpos(R*radians(-180),R*sin(radians(j)))
        pendown()
        for i in l:
            setpos(R*radians(i),R*sin(radians(j)))
    for j in l:
        penup()
        setpos(R*radians(j),R*sin(radians(-90)))
        pendown()
        for i in k:
            setpos(R*radians(j),R*sin(radians(i)))
    exitonclick()
    return delka, sirka
# definice funkce gnomonicke projekce
def Gn(m,n,R):
    # vypocteni bodu uzivatele
    def p(j):
        c = R*tan((radians(90-j)))
        return c
    def e(j):
        return radians(j)
    delka = p(n)*cos(e(m))
    sirka = p(n)*sin(e(m))
    # vykresleni site
    k = range(10,100,10)
    l = range(-180,190,10)
    speed(0)
    for j in k:
        penup()
        setpos(p(j)*cos(e(-180)),p(j)*sin(e(-180)))
        pendown()
        for i in l:
            setpos(p(j)*cos(e(i)),p(j)*sin(e(i)))
    for j in l:
        penup()
        setpos(p(10)*cos(e(j)),p(10)*sin(e(j)))
        pendown()
        for i in k:
            setpos(p(i)*cos(e(j)),p(i)*sin(e(j)))
    exitonclick()
    return delka, sirka
# definice funkce ptolemaiova zobrazeni
def Pt(m,n,R):
    # spocteni bodu uzivatele
    def p(j):
        h = R*(1/tan(radians(30)))+R*(radians(30-j))
        return h
    def e(j):
        h = radians(j)*sin(radians(30))
        return h
    delka = radians(30)-p(n)*cos(e(m))
    sirka = p(n)*sin(e(m))
    # vykresleni site
    k = range(-90,100,10)
    l = range(-180,190,10)
    speed(0)
    for j in k:
        penup()
        setpos(radians(30)-p(j)*cos(e(-180)),p(j)*sin(e(-180)))
        pendown()
        for i in l:
            setpos(radians(30)-p(j)*cos(e(i)),p(j)*sin(e(i)))
    for j in l:
        penup()
        setpos(radians(30)-p(-90)*cos(e(j)),p(-90)*sin(e(j)))
        pendown()
        for i in k:
            setpos(radians(30)-p(i)*cos(e(j)),p(i)*sin(e(j)))
    exitonclick()
    return delka, sirka
# definice sansonova zobrazeni
def Sa(m,n,R):
    # vypocteni bodu uzivatele
    delka = R*radians(m)*cos(radians(n))
    sirka = R*radians(m)
    # vykresleni site
    k = range(-90,100,10)
    l = range(-180,190,10)
    speed(0)
    for j in k:
        penup()
        setpos(R*radians(-180)*cos(radians(j)),R*radians(j))
        pendown()
        for i in l:
            setpos(R*radians(i)*cos(radians(j)),R*radians(j))
    for j in l:
        penup()
        setpos(R*radians(j)*cos(radians(-90)),R*radians(-90))
        pendown()
        for i in k:
            setpos(R*radians(j)*cos(radians(i)),R*radians(i))
    exitonclick()
    return delka, sirka
# nacteni zobrazeni
zob = str(input("Zadej zobrazení (buď Sa, Lv, Gn, Pt):"))
sezzob = {"Sa","Lv","Gn","Pt"}
if zob not in sezzob:
    print("Neexistující zobrazení.")
    quit()
# nacteni meritka a uprava polomeru dle meritka
meritko = int(input("Zadej měřítko:"))
R = 6371100/0.0003
R = R/meritko
# nacteni delky a sirky prepocitavaneho bodu
m = float(input("Zadej zeměpisnou délku ve stupních:"))
if abs(m) > 180:
    print("Tento úhel nepřipadá v úvahu.")
    quit()
n = float(input("Zadej zeměpisnou šířku ve stupních:"))
if abs(n) > 90:
    print("Tento úhel nepřipadá v úvahu.")
    quit()
# vypocet bodu a vykresleni site
if zob == "Sa":
    delka, sirka = Sa(m,n,R)
if zob == "Lv":
    delka, sirka = Lv(m,n,R)
if zob == "Gn":
    if n == 0:
        print("Rovník není v gnomonické projekci definován.")
        quit()
    delka, sirka = Gn(m,n,R)
if zob == "Pt":
    delka, sirka = Pt(m,n,R)
print("Pro tvůj bod je souřadnice x:",delka,"a souřadnice y:",sirka)