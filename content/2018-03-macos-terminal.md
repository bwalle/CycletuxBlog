Title: Bildlauftasten im Terminal von Mac OS vernünftig verwenden
Date: 2018-01-03
Category: Computer
Tags: computer, apple
Slug: 2018-03-macos-terminal

Ich hatte früher unter Mac OS immer _iTerm_ verwendet, da mir einige Funktionen
im mitgelieferten Terminal gefehlt haben. Mittlerweile ist es aber eher anders
herum: _iTerm_ bekommt immer mehr Funktionalität, am besten soll man sich noch
Erweiterungen für die Shell installieren (wenn man viel auf anderen Rechnern
per SSH arbeitet eher unpraktikabel) und _Terminal_ hat ein paar Funktionen
spendiert bekommen, so dass ich jetzt auf die mitgelieferte Variante gewechselt
habe.

Allerdings gefällt man das Verhalten der Bildlauftasten nicht, da diese direkt
scrollen ohne an die Shell weitergegeben zu werden. Ich persönlich habe meine
ZSH so konfiguriert dass in den Befehlen geblättert wird, so wie in der
SUSE-Standardkonfiguration der Bash seit jeher vorkonfiguriert. Zum Scrollen
verwende ich dann die Umschalttaste und die Bildlauftasten. Letztlich arbeite
ich viel unter Linux und will dass die Bildlauftasten sowie Pos1/Ende genauso
funktionieren wie am PC.

Man  kann man hierfür die Tastaturbefehle anpassen. Dazu wählt man _Terminal_ →
_Einstellungen_ → _Profile_ → _Tastatur_  und fügt die in der Tabelle dargestellten
Einträge hinzu. Zu beachten: Die Sequenz `\033` erzeugt man über die
Escape-Taste.

| Taste              | Sondertasten     | Aktion                 |
| ------------------ | ---------------- | ---------------------- |
| ↖ Start            | Ohne             | Text senden: `\033[H`  |
| ↘ Ende             | Ohne             | Text senden: `\033[F`  |
| ⇞ Seite nach oben  | Ohne             | Text senden: `\033[5~` |
| ⇟ Seite nach unten | Ohne             | Text senden: `\033[6~` |
| ⇞ Seite nach oben  | ⇧ Umschalttaste  | Seite nach oben        |
| ⇟ Seite nach unten | ⇧ Umschalttaste  | Seite nach unten       |
