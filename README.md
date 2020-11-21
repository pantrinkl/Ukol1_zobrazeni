# Úkol 1 - zobrazení

Tento program slouží pro vykreslení sítí šesti projekcí a zobrazení:
Gnomonické projekce, Postelova zobrazení, Lambertova válcového zobrazení, Marionva zobrazení, Sansonova zobrazení a Ptolemaiova zobrazení.

Dále vypočítá souřadnice libovolně zvoleného bodu v daném zobrazení.

## Vstupní parametry

### Zadání zobrazení
Pro jednotlivá zobrazení zadejte zkratky:
- Gnomonická projekce: `Gn`
- Postelovo zobrazení: `Po`
- Lambertovo válcové zobrazení: `Lv`
- Marinovo zobrazení: `Ma`
- Sansonovo zobrazení: `Sa`
- Ptolemaiovo zobrazení: `Pt`

### Zadání měřítka
Zadejte měříko, ve kterém se zobrazí výkres zobrazení. Například pro měřítko 1:5000000 zadejte `5000000`. 
Doporučené měřítko pro zemi s opravdovým poloměrem je mezi 1:5 000 000 až 1:50 000 000. 

### Zadání poloměru země
Program umožňuje modifikovat poloměr země/planety. Zadejte poloměr země v kilometrech. Pokud zadáte hodnotu `O`, je brán skutečný poloměr země - tj. 6371,11 km.

### Zadání délky a šířky libovolného bodu
Délku a šířku libovolného bodu zadávejte ve stupních. Pokud vás například zajímá poloha městysu Jimramov ve zvoleném zobrazení, zadejte jako zeměpisnou délku `16.2263` a jako zeměpisnou šírku `49.6372`. 

### Zadání vzdálenosti rovnoběžek a poledníků
Program umožňuje zadat po kolika stupních se budou vykreslovat rovnoběžky a poledníky. Hodnotu zadávejte v celých stupních. Pokud je zadána hodnota `0`, tak je vykreslována síť po 10 stupních. 

## Výstup
Program vykreslí síť daného geografického zobrazení / geografické projekce pomocí modulu `turtle`. Dále vypíše hodnoty x a y pro libovolný bod v terminálu.
Pro zavření vykreslené sítě do ní stačí kliknout.

Na [stránce úkolu](https://github.com/xtompok/uvod-do-prg_20/tree/master/du01) se lze dozvědět více podrobností.
