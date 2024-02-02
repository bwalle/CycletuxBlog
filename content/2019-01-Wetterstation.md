Title: Neue Wetterstation
Date: 2019-01-01
Category: Computer
Tags: computer, wetterstation
Slug: 2019-01-wetterstation

## Motivation

Nach fast 10 Jahren ging meine alte Wetterstation ­ eine ELV USB-WDE01 mit
Kombisensor KS200 ­ kaputt. Eigentlich ging sie noch, allerdings hat die
Windmessung nicht mehr funktioniert und ich wüsste nicht wie ich das hätte
reparieren können. Insofern habe ich mich nach einem Ersatz umgesehen und wurde
bei Pearl fündig. Eine [FreeTec
PX1117](https://www.pearl.de/a-PX1117-3041.shtml) sollte es werden.

Ich verwende ja eine Seagate Dockstar um die Daten zu speichern und ins
Internet zu übertragen. Zum Einsatz kommt eine selbst geschriebene Software
[Vetero](https://github.com/bwalle/vetero). Dies sollte auch so bleiben, ich
bin einfach flexibler wie mit „fertigen“ WLAN-Stationen mit Cloud-Anbindung,
die doch sehr von der Unterstützung des Herstellers abhängig sind. Mal davon
abgesehen läuft mein WLAN nachts nicht und das soll auch so bleiben.

Insofern kam es mir durchaus gelegen, dass diese FreeTec-Station eine ganz
normale USB-Anbindung hat.

## Hardware

![]({static}/images/2019_01_wetterstation/IMG_6319-1-768x1024.jpg) <br />
_So schaut die fertig aufgebaute Station auf meinem Balkon aus_

![]({static}/images/2019_01_wetterstation/IMG_6319.jpg) <br />
_Und so innen (die Beleuchtung geht nach einiger Zeit aus)_

## Vor- und Nachteile

- Das USB-Protokoll ist bei der ELV dokumentiert.
- Die FreeTec hat eine Windrichtungsmessung.
- Von der Hardware macht die ELV einen robusteren Eindruck, vor allem gefällt
  mir der Kabelsalat bei der FreeTec nicht wirklich.
- Das Display bei der FreeTec hat einen Touchscreen (zwar nicht kapazitiv aber immerhin).
- Die FreeTec ist mit 99 € sehr günstig.

Nachdem die FreeTec-Station mit 99 € doch sehr günstig ist will ich mal nicht
meckern. Wirklich gestört hat mich nur das nicht dokumentierte USB-Protokoll.
Alternativ hätte man auch den Quellcode der Software mitliefern können. Warum
die Hersteller hier immer noch auf Closed Source setzten ist mir ein Rätsel,
schließlich wird ja nur an der Hardware verdient.

## USB-Anbindung

Wie bereits erwähnt ist das Protokoll proprietär. Zum Glück gab es bereits vor
mir findige Bastler, die sich des Protokolls angenommen haben. Das
Python-Skript auf
[GitHub](https://github.com/shaneHowearth/Dream-Link-WH1080-Weather-Station)
hat bei mir auf Anhieb funktioniert und ich konnte es in C++ in Vetero
integrieren.

## Fazit

Aufbau und Anbindung der neuen Wetterstation haben mich knapp zwei Tage
gekostet, bis jetzt läuft alles stabil. Die aktuellen Daten gibt's auf
[vetero.bwalle.de](http://vetero.bwalle.de).
