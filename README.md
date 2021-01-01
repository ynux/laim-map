### Resources

no code, just some notes on a openstreetmap crash course on the open data day munich, march 2020

#### umap / openstreetmap
Build an own openstreet map with layers, made simple: by [umap](https://umap.openstreetmap.de/de/)

1. Erstelle eine Karte. Sichere den Editierlink. Suche Deinen Ausschnitt der Welt, speichere Position und Zoomstufe.
2. Grenzen von Laim: Wikidata-ID von Laim finden (kein Trick, einfach suchen).
overpass-turbo.eu
```
[out:json][timeout:25];
// gather results
(
  // query part for: “boundary=administrative”
  
  relation[wikidata=Q259879];);
// print results
out body;
>;
out skel qt;
```
reinkopieren, ausführen, auf die Lupe klicken ("auf die Daten zoomen"), dann Datentab aufmachen und Inhalt rauskopieren.

In der eigenen Karte: Ebene "boundaries" hinzufügen. Daten importieren -> in die Box kopieren, Format "osm", importieren, sichern. Dann bei Eigenschaften Füllfarbe usw wählen. Speichern.

Oder:
Export -> Daten -> Rohdaten direkt von Overpass API; `http` zu `https` korrigieren
in umap füttern
```
http://overpass-api.de/api/interpreter?data=%2F*%0AThis%20has%20been%20generated%20by%20the%20overpass-turbo%20wizard.%0AThe%20original%20search%20was%3A%0A%E2%80%9Cboundary%3Dadministrative%E2%80%9D%0A*%2F%0A%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0A%2F%2F%20gather%20results%0A%28%0A%20%20%2F%2F%20query%20part%20for%3A%20%E2%80%9Cboundary%3Dadministrative%E2%80%9D%0A%20%20%0A%20%20relation%5B%22boundary%22%3D%22administrative%22%5D%5B%22admin_level%22%3D9%5D%5Bwikidata%3DQ259879%5D%2848.122158324039965%2C11.475906372070312%2C48.156409796538426%2C11.536245346069336%29%3B%0A%29%3B%0A%2F%2F%20print%20results%0Aout%20body%3B%0A%3E%3B%0Aout%20skel%20qt%3B
```

Was gibt es von der Stadt aus, oder sonst schon?

* [Geodaten Bezirksboundaries im Open Data Portal:] (https://www.opengov-muenchen.de/dataset/verwaltungseinheiten-der-landeshauptstadt-muenchen)
* [Muenchen Transparent Laim](https://www.muenchen-transparent.de/bezirksausschuss/25_Laim), auch ["Tagesordnung auf der Karte"](https://www.muenchen-transparent.de/termine/5659757)


Weitere nützliche Links:

* [Wiki von openstreetmap](https://wiki.openstreetmap.org/wiki/Elements)
* https://www.openstreetmap.org/relation/54388
* Erste Karte: [laim_ba_mvp](https://umap.openstreetmap.de/de/map/laim_ba_mvp_2644#14/48.1363/11.5047)

