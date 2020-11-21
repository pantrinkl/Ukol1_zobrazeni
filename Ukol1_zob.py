import turtle
import math
from turtle import exitonclick, setpos, pendown, penup, speed
from math import log, cos, radians, tan, sin, cos, acos

# vypocet uzivatelova bodu v lambertove valcovem zobrazeni
def Lv_bod(d,s,R):
    delka = R*radians(d)
    sirka = R*sin(radians(s))
    return delka, sirka

# vykresleni site lambertova valcoveho zobrazeni
def Lv(pol,rov,R):
    k = range(-90,91,rov)
    l = range(-180,181,pol)
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

# vypocet uzivatelova bodu v marinove zobrazeni
def Ma_bod(d,s,R):
    delka = R*radians(d)
    sirka = R*radians(s)
    return delka, sirka

# vykresleni site lambertova valcoveho zobrazeni
def Ma(pol,rov,R):
    k = range(-90,91,rov)
    l = range(-180,181,pol)
    speed(0)
    for j in k:
        penup()
        setpos(R*radians(-180),R*radians(j))
        pendown()
        for i in l:
            setpos(R*radians(i),R*radians(j))
    for j in l:
        penup()
        setpos(R*radians(j),R*radians(-90))
        pendown()
        for i in k:
            setpos(R*radians(j),R*radians(i))

# vypocet sirky gnomonicke projekci 
def p_gn(s,R):
    c = R*tan((radians(90-s)))
    return c

# vypocet delky v gnom. projekci
def e_gn(d):
    return radians(d)

# vypocet uzivatelova bodu v gnom. projekci 
def Gn_bod(d,s,R):
    delka = p_gn(s,R)*cos(e_gn(d))
    sirka = p_gn(s,R)*sin(e_gn(d))
    return delka, sirka

# vykresleni site gnomonicke projekce
def Gn(pol,rov,R):
    k = range(10,91,rov)
    l = range(-180,181,pol)
    speed(0)
    for j in k:
        penup()
        setpos(p_gn(j,R)*cos(e_gn(-180)),p_gn(j,R)*sin(e_gn(-180)))
        pendown()
        for i in l:
            setpos(p_gn(j,R)*cos(e_gn(i)),p_gn(j,R)*sin(e_gn(i)))
    for j in l:
        penup()
        setpos(p_gn(10,R)*cos(e_gn(j)),p_gn(10,R)*sin(e_gn(j)))
        pendown()
        for i in k:
            setpos(p_gn(i,R)*cos(e_gn(j)),p_gn(i,R)*sin(e_gn(j)))

# vypocet sirky v postelove zobrazeni
def p_po(s,R):
    c = R*radians(90-s)
    return c

# vypocet delky v postelove zobrazeni
def e_po(d):
    return radians(d)

# vypocet uzivatelova bodu v postel. zobrazeni
def Po_bod(d,s,R):
    delka = p_po(s,R)*cos(e_po(d))
    sirka = p_po(s,R)*sin(e_po(d))
    return delka, sirka

# vykresleni site postelova zobrazeni
def Po(pol,rov,R):
    k = range(-90,91,rov)
    l = range(-180,181,pol)
    speed(0)
    for j in k:
        penup()
        setpos(p_po(j,R)*cos(e_po(-180)),p_po(j,R)*sin(e_po(-180)))
        pendown()
        for i in l:
            setpos(p_po(j,R)*cos(e_po(i)),p_po(j,R)*sin(e_po(i)))
    for j in l:
        penup()
        setpos(p_po(-90,R)*cos(e_po(j)),p_po(-90,R)*sin(e_po(j)))
        pendown()
        for i in k:
            setpos(p_po(i,R)*cos(e_po(j)),p_po(i,R)*sin(e_po(j)))

# vypocet sirky v ptolemaiove zobrazeni
def p_pt(s,R):
    h = R*(1/tan(radians(30)))+R*(radians(30-s))
    return h

# vypocet delky v ptolemaiove zobrazeni
def e_pt(d):
    h = radians(d)*sin(radians(30))
    return h

# vypocet uzivatelova bodu v ptolemaiove zobrazeni
def Pt_bod(d,s,R):
    delka = radians(30)-p_pt(s,R)*cos(e_pt(d))
    sirka = p_pt(s,R)*sin(e_pt(d))
    return delka, sirka

# vykresleni site ptolemaiova zobrazeni
def Pt(pol,rov,R):
    k = range(-90,91,rov)
    l = range(-180,181,pol)
    speed(0)
    for j in k:
        penup()
        setpos(radians(30)-p_pt(j,R)*cos(e_pt(-180)),p_pt(j,R)*sin(e_pt(-180)))
        pendown()
        for i in l:
            setpos(radians(30)-p_pt(j,R)*cos(e_pt(i)),p_pt(j,R)*sin(e_pt(i)))
    for j in l:
        penup()
        setpos(radians(30)-p_pt(-90,R)*cos(e_pt(j)),p_pt(-90,R)*sin(e_pt(j)))
        pendown()
        for i in k:
            setpos(radians(30)-p_pt(i,R)*cos(e_pt(j)),p_pt(i,R)*sin(e_pt(j)))

# vypocet uzivatelova bodu v sansonove zobrazeni
def Sa_bod(d,s,R):
    delka = R*radians(d)*cos(radians(s))
    sirka = R*radians(s)
    return delka, sirka

# definice sansonova zobrazeni
def Sa(pol,rov,R):
    # vykresleni site
    k = range(-90,91,rov)
    l = range(-180,181,pol)
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

# samotny program
# nacteni zobrazeni
zob = str(input("Zadej zobrazení (buď Sa, Lv, Gn, Pt, Po, Ma):"))
sezzob = {"Sa","Lv","Gn","Pt","Po","Ma"}
if zob not in sezzob:
    print("Neexistující zobrazení.")
    quit()
# nacteni meritka a uprava polomeru dle meritka
meritko = int(input("Zadej měřítko:"))
if meritko <= 0:
    print("Špatně zadané měřítko")
    quit()
# nacteni polomeru zeme
polomer = int(input("Zadej poloměr země v kilometrech. Když zadáš 0, bude počítáno se skutečným:"))
if polomer == 0:
    R = 6371.11*100000
elif polomer < 0:
    print("Špatně zadaný poloměr země.")
    quit()
else:
    R = polomer*100000
# vypocet zobrazeneho polomeru zeme dle meritka
R = R/meritko
# nacteni delky a sirky prepocitavaneho bodu
d = float(input("Zadej zeměpisnou délku ve stupních:"))
if abs(d) > 180:
    print("Tento úhel nepřipadá v úvahu.")
    quit()
s = float(input("Zadej zeměpisnou šířku ve stupních:"))
if abs(s) > 90:
    print("Tento úhel nepřipadá v úvahu.")
    quit()
# zadani po kolika polednicich se bude vykreslovat
pol = int(input("Zadej po kolika polednících se bude vykreslovat síť:"))
if pol < 0 | pol > 360:
    print("Toto vykreslení nejde.")
    quit()
elif pol == 0:
    pol = 10
# zadani po kolika rovnobezkach se bude vykreslovat
rov = int(input("Zadej po kolika rovnoběžkách se bude vykreslovat síť:"))
if rov < 0 | rov > 180:
    print("Toto vykreslení nejde.")
    quit()
elif rov > 80 and zob == "Gn":
    print("Toto vykreslení nejde.")
    quit()
elif rov == 0:
    rov = 10
# vypocet bodu a vykresleni site
if zob == "Sa":
    Sa(pol,rov,R)
    delka, sirka = Sa_bod(d,s,R)
if zob == "Lv":
    Lv(pol,rov,R)
    delka, sirka = Lv_bod(d,s,R)
if zob == "Gn":
    if s == 0:
        print("Rovník není v gnomonické projekci definován.")
        quit()
    Gn(pol,rov,R)
    delka, sirka = Gn_bod(d,s,R)
if zob == "Pt":
    Pt(pol,rov,R)
    delka, sirka = Pt_bod(d,s,R)
if zob == "Po":
    Po(pol,rov,R)
    delka, sirka = Po_bod(d,s,R)
if zob == "Ma":
    Ma(pol,rov,R)
    delka, sirka = Ma_bod(d,s,R)
print("Pro tvůj bod je souřadnice x:",delka,"a souřadnice y:",sirka)
exitonclick()
