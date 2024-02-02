Title: Wetterstation: die Dritte
Date: 2022-10-01
Category: Computer
Tags: computer, wetterstation
Slug: 2022-10-wetterstation

Tja, eigentlich ist meine [Wetterstation]({filename}/2019-01-Wetterstation.md)
noch nicht so alt gewesen. Ich war allerdings nie so richtig mit dem Teil
zufrieden. Messtechnisch okay aber die Hardware war ziemlich „windig“. Die
vielen Kabel hässlich. Und bei nem Sturm im August ging das Windrad kaputt.
Ersatzteile sind keine erhältlich.

Anfang dieses Jahres kaufte ich für meinen Vater die [ELV WiFi-Wetterstation
WS980WiFi](https://de.elv.com/elv-wifi-wetterstation-ws980wifi-inkl-funk-aussensensor-868-mhz-app-pc-auswertesoftware-250408) und war ziemlich zufrieden damit.

Die Hardware ist sehr robust und besteht aus einem einzigen Block, der nur noch
auf einen Masten besfestigt werden muss. Ersatzteile sind verfügbar und
zumindest bei meiner ersten Wetterstation von ELV waren die es auch noch sehr
lange nachdem das Produkt nicht mehr verkauft wurde.

Als ich dann zufällig sah, dass die Station Ende September im Sonderangebot für 115 € war,
griff ich spontan zu. Zwei Tage später war die Wetterstation dann auch bei mir zu Hause.


![]({static}/images/2022_10_wetterstation/aussen.jpg) <br />
_So schaut die fertig aufgebaute Station auf meinem Balkon aus_

![]({static}/images/2022_10_wetterstation/display.jpg) <br />
_Und so das WLAN-Display_

## Vor- und Nachteile

### Pro

Hier mal aus meiner Sicht die Pluspunkte dieser Station:

- robuste Hardware
- Verfügbarkeit von Ersatzteilen
- Stromversorgung per Solarzelle mit Stützbatterie
- viele Messdaten
    - Temperatur
    - Luftfeuchtigkeit
    - Luftdruck
    - Taupunkt (zwar errechnet aber direkt am Display angezeigt)
    - Niederschlag
    - Windrichtung und -geschwindigkeit mit Windböen
    - Sonnenstrahlung (W/m²) und UV-Index
- Display mit WLAN, Daten werden in verschiedene Wetter-Clouds (beispielsweise [Weather Underground](http://wunderground.com)) geladen, die man konfigurieren kann
- Protokoll im Internet verfügbar, lokale Abfrage im LAN möglich (dazu später mehr)

### Contra

- App ziemlich schlecht gemacht
- PC-Software noch schlechter
- es gibt schönere Displays

**Fazit:** wer auf die mitgelieferte Software Wert legt oder das Display für mehr als nur das Anzeigen der aktuellen Werte verwenden möchte, findet sicher bessere Produkte. Darum ging's mir aber nicht.

## Ersteinrichtung

Die Einrichtung funktioniert folgendermaßen:

1. Man verbindet sein Smartphone zu dem WLAN-Hotspot, welche die Wetterstation bereitstellt.
2. Man konifguriert in der App [WS View](https://www.google.com/search?client=safari&rls=en&q=ws+view&ie=UTF-8&oe=UTF-8) die Daten zum WLAN-Netzwerk, also SSID und Passwort. Eigentlich sollte man dafür [WS Tool](https://apps.apple.com/de/app/ws-tool/id1125344077) verwenden, die funktioniert aber nicht.
3. Daraufhin verschwindet der Hotspot wieder, die Wetterstation verbindet sich zum WLAN und die Einrichtung ist erstmal abgeschlossen.
4. In der App kann man die Zugangsdaten zu Wetter-Clouds konfigurieren damit die Wetterdaten dann hochgeladen werden.

Man sollte noch den Luftdruck kalibrieren. Entweder man verwendet die Daten von Wetterseiten und sucht sich eine Station in der Nähe oder eine entsprechende Smartphone-App wie [Barometer & Altimeter Pro für iOS](https://apps.apple.com/de/app/barometer-altimeter-pro/id923043780), die über GPS die Höhe kennen und über die [Barometrische Höhenformel](https://de.wikipedia.org/wiki/Barometrische_Höhenformel) den _relativen Luftdruck auf Meereshöhe_ (nur der ist für das Wetter von Belang) direkt berechnen.


## Wetter-Clouds

Mittlerweile gibt's eine ganze Reihe von Clouds, wo man eigene Messdaten
hochladen kann, die die Daten dann aufbereiten und wo jeder sie zur Verfügung
gestellt bekommt. Ich lade meine Daten zu [Weather
Underground](http://wunderground.com), im wesentlichen weil ich da mit
[myPWS](https://apps.apple.com/app/mypws/id1467639867?l=en&ls=1) eine sehr
gute, wenn auch teilweise kostenpflichtige, App für iOS gefunden habe.

Um die Daten bei der _WS980WiFi_ dort hochzuladen konfiguriert man 

## Lokale Abfrage

Glücklicherweise kann man die Wetterdaten auch direkt im LAN abfragen, was die
PC-Software macht.  Dadurch konnte ich die Station sehr einfach in meine
[eigene Software „vetero“](https://github.com/bwalle/vetero) integrieren, mit
der ich die Daten seit 10 Jahren erfasse und aufbereite.

Die Protokollbeschreibung gibt's nicht vom Hersteller, man findet sie aber
in einem [Thread im ELV-Forum](https://de.elv.com/forum/protokolldefinition-zum-datenaustausch-ws980-zum-pc-6430?p=2) wenn man nach _WS980_protokoll.docx_ sucht.

Dadurch ist man auch unabhängig von den Cloudanbietern und von Software vom
Hersteller. Lediglich für die Erstkonfiguration des WLANs benötigt man zwingend
die App vom Hersteller.

Recht verbreitet ist im übrigen die OpenSource-Software
[WeeWX](https://www.weewx.com), die die Station ebenfalls unterstützt und
ebenfalls eine lokale Abfrage vornimmt.


## Meine Wetterdaten

Die gibt's [hier](http://vetero.bwalle.de). Schaut alles ziemlich altbacken
aus, besteht aus statischen HTML-Seiten die generiert werden aber ich komme
damit eigentlich deutlich besser klar wie mit den Alternativen, die ich so
gefunden habe. Macht der Gewohnheit.
