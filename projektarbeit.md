# Projektarbeit
Visualisierung der aktuellen Corona-Ausbreitung als Gruppenarbeit 
(maximal 3-5 Teilnehmer pro Gruppe zulässig)
Die Abgabe muss bis Donnerstag dem 14.01.2021 : 15:00 Uhr erflogt sein.


## Hintergrund
Speichern Sie die aktuellen Zahlen der letzten 7 Tage (täglich) der Corona Fälle, um Aussagen über die Verbreitung treffen zu können. In der Corona-API https://api.covid19api.com finden Sie eine Schnittstelle für JSON Daten, die via Requests abgerufen werden können. 
Weitere Information zu der API: https://covid19api.com/
Die Einwohnerzahl kann als Konstante angesehen werden. Deutschland (83 149 300 Einwohner)
                                                                        

## Userstory I (Prio 1)
Der Arzt Dr. Petersen möchte die Entwicklung von Deuschland im Blick behalten. Zeigen Sie ihm in einer Applikationsansicht die Zahlen der letzten 7 Tage für Deutschland an. (aktuell infiziert, bestätigte Fälle, Aktive Fälle, genesene Fälle, verstorbene Fälle)


## Userstory II (Prio 2)
Ermitteln Sie den Zuwachs der aktuellen Fälle in Prozent der jeweiligen Tage und fügen Sie diesen der Ansicht hinzu.


## Userstory III (Prio 2)
Geben Sie an wieviel Prozent der Bevölkerung des Landes zum aktuellen Zeitpunkt genesen sind. 


## Userstory IV (Prio 2)
Geben Sie eine Warnung aus, wenn mehr als 0,01% Prozent des Landes aktuell infiziert sind.


## Userstory V  (Prio 3)
Über einen Aktualisierungsbutton sollen die Daten neu über die API abgeholt werden. 
Die bisherigen Daten sollen gespeichert werden und einer CSV-Datei oder SQLite-Tabelle angehangen werden.


## Userstory VI (Prio 2)
Über eine Auswahl (Buttons oder Menüpunkt) kann das Land (IT/AT/ES) gewechselt werden.


## Tipp
Für eine vollständige Lösung der Aufgaben sind folgende Libraries hilfreich:
- tkinter  
- requests
- json
- csv
- sqlite3
- unittest






















## Bewertungskritieren
- Struktur und Organisation des Quellcodes
- Auslagerung in Module/Klassen
- Robustheit der Klassen: Unit Test, Try/Except 
- Anwendung von Design Patttern: Decorator, MVC
- Dokumentation/Kommentare Quellcode
- Erfüllung der jeweilgen Userstory
- Gestaltung des Userinterface (GUI):
- Anordnung von Fensterkomponenten 
- Fenstergröße
- Buttonposition 
- Font-Size, Font-Farbe












