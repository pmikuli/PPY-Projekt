# Czym jest `pycal`?
`pycal` jest prostą aplikacją kalendarza, w której można przechowywać informacja na temat wydarzeń.
Można w nim zapisać kiedy wydarzenie ma miejsce oraz króki opis tego wydarzenia. 
# Użycie
`pycal` przyjmuje tylko jeden opcjonalny argument: ściezkę do pliku kalendarza. 
W przypadku pominięcia argumentu plik kalendarza będzie zapisywany w katalogu użytkownika.

## Komendy
Po uruchomieniu aplikacja poprosi użytkownika o podanie komendy do wykonania.
Dostępne komendy to:
- `show today` - wyświetla widok dnia dla dzisiejszego dnia, wypisujący wydarzenia na dany dzień. 
- `show this month` - wyświetla widok miesiąca dla dzisiejszego dnia
- `show this week` - wyświetla widok tygodnia dla dzisiejszego dnia. W widoku tygodnia wyświetlane są wszystkie wydarzenia mające miejsce w danym tygodniu. Data dzisiejsza jest oznaczona kolorem fioletowym. 
- `add event DATE_FROM DATE_TO EVENT_NAME` - komenda przyjmuje 3 argumenty pozycyjne: datę od, datę do oraz nazwę wydarzenia. Daty powinny być w formacie `dd-mm-yyyy HH:MM`. Dla podanych danych tworzone jest wydarzenie po czym jest ono od razu zapisywane do pliku.
- `remove event DATE_FROM DATE_TO EVENT_NAME` - podobnie jak wyżej, ale zamiast dodawać usuwa wydarzenie.
- `show day DATE` - przyjmuje jeden argument pozycyjny, który jest datą do wyświetlenia. Data powinna mieć format `dd-mm-yyyy`. 
- `show week DATE`- podobnie jak wyżej, ale pokazuje widok tygodnia w którym znajduje się podana w argumencie data.
- `show month MONTH_NAME YEAR` - przyjmuje 2 argumenty: nazwę miesiąca oraz rok. Należy podać nazwę miesiąca po angielsku. Wyświetla widok miesiąca dla podanych danych.
- `help`- wyświetla opis dostępnych komend
- `exit` - zamyka program i zapisuje zmiany w kalendarzu. 

# Autor
Patryk Mikuli

S24087