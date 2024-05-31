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
- `add event DATE_FROM DATE_TO EVENT_DESCRIPTION` - komenda przyjmuje 3 argumenty pozycyjne: datę od, datę do oraz opis wydarzenia. Daty powinny być w formacie `dd-mm-yyyy HH:MM`. Dla podanych danych tworzone jest wydarzenie po czym jest ono od razu zapisywane do pliku.
- `remove event DATE_FROM DATE_TO EVENT_DESCRIPTION` - podobnie jak wyżej, ale zamiast dodawać usuwa wydarzenie.
- `show day DATE` - przyjmuje jeden argument pozycyjny, który jest datą do wyświetlenia. Data powinna mieć format `dd-mm-yyyy`. 
- `show week DATE`- podobnie jak wyżej, ale pokazuje widok tygodnia w którym znajduje się podana w argumencie data.
- `show month MONTH_NAME YEAR` - przyjmuje 2 argumenty: nazwę miesiąca oraz rok. Należy podać nazwę miesiąca po angielsku. Wyświetla widok miesiąca dla podanych danych.
- `help`- wyświetla opis dostępnych komend
- `exit` - zamyka program i zapisuje zmiany w kalendarzu. 

# Dokumentacja
## Moduł `main`
Moduł uruchamiający program. Zawiera funkcje pomocnicze, potrzebne do uruchomienia go. 
### Publiczne funkcje
| Funkcja | Opis |
| - | - |
| `main()` | Funkcja wejściowa programu. Przetwarza argumenty powłoki oraz uruchamia główną pętlę interfejsu |
### Prywatne funkcje
| Funkcja | Opis                                                                                                                                                                                                                                          |
| - |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `__start_main_loop()` | Uruchamia nieskończoną pętlę, pobierającą od użytkownika komendy ze standardowego wyjścia i wykonującą je. Pętlę można zakończyć poprzez wydanie polecenia zamknięcia programu.                                                               |
| `_execute(command: str)` | Parsuje i wykonuje komendę podaną w łańcuchu `command`. Komendy te odnoszą się do funkcjonalności kalendarza, np. wyświetlenie widoku dnia. Jeżeli komenda nie została rozpoznana, informacja o tym jest zapisywana do standardowego wyjścia. |
| `__get_event_from_command_args(split: List[str]) -> Event` | Parsuje argumenty komendy i używa ich do stworzenia obiekty typu `Event` |  

## Klasa `Event`
Przechowuje informacje na temat wydarzenia, takie jak: data i godzina rozpoczęcia, 
data i godzina zakończenia oraz opis wydarzenia.

### Atrybuty
| Atrybut | Opis |
| --- | - |
| `date_from` | data i godzina rozpoczęcia |
| `date_to` | data i godzina zakończenia - atrybut |
| `description` | opis wydarzenia |

## Klasa `Calendar`
Klasa modelująca kalendarz. Przechowuje ona umieszczone w nim wydarzenia. 
Można po niej iterować w celu uzyskania dostępu do zawartych w kalendarzu wydarzeń. 

### Konstruktor
`__init__(self, events: List[Event])`

Przyjmuje listę wydarzeń jako jedyny argument. 

### Metody
| Metoda | Opis |
| --- | --- |
| `add_event(event)` | jako argument przyjmuje obiekt o typie `Event`. Dodaje podane wydarzenie do listy wydarzeń |
| `remove_event(event)` | jako argument przyjmuje obiek o typie `Event`. Usuwa go z listy wydarzeń. | 
### Dostęp do wydarzeń
Do wydarzeń można dostać się na dwa sposby: używając atrybutu o nazwie `events`, albo używając iteratora. Przykład z iteratorem:
```python
for event in calendar:
    print(event)
```
## Moduł `calendar_view`
Moduł jest zbiorem funkcji pomocniczych do wyświetlania kalendarza i różnych dla niego widoków: dnia, tygodnia oraz miesiąca.

### Publiczne funkcje
| Funkcja                                         | Opis                                                                                                                                     |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `print_day(calendar, date: datetime, width=80)` | Wyświetla w konsoli widok dnia. Jako argument przyjmuje kalendarz oraz datę dnia do wyświetlenia. Opcjonalnym argumentem jest szerokość. | 
| `print_week(calendar, date: datetime)`          | Wyświetla w konsoli widok tygodnia. Jako argumenty przyjmuje kalendarz i datę reprezentującą jeden z dni w docelowym tygodniu.
| `print_month(date: datetime)`                   | Wyświetla w konsoli widok miesiąca. Jako argument przyjmuje dowolny dzień z miesiąca do wyświetlenia. |

### Prywatne funkcje
| Funkcja                                                                 | Opis                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `__generate_day_lines(calendar, date: datetime, width=80) -> List[str]` | Generuje listę linijek które następnie można wypisać w konsoli. Wyświetlą one widok dnia zawierający wydarzenia z podanego kalendarza. Dzień do wyświetlenia jest podawany w argumencie `date`. Przyjmuje również opcjonalny argument ustawiający szerokość widoku. Jednostką szerokości jest liczba znaków. 
| `__generate_week_lines(calendar, date: datetime) -> List[str]`          | Podobnie jak wyżej, ale dla widoku tygodnia oraz nie przyjmuje szerokości jako argument.                                                                                                                                                                                                                     |
| `__generate_month_lines(date: datetime) -> List[str]`                   | Generuje listę linijek do wyświetlenia widoku miesiąca. Nie wyświetla wydarzeń. Jako argument przyjmuje jeden z dowolnych dni miesiąca do wyświetlenia. Dodaje znak '\|' na początek i koniec linijki. Znak ten reprezentuje lewą i prawą ramkę widoku.                                                                                                                                                      |
| `__center(text: str, width: int) -> str`                                | Funkcja pomocnicza. Wstawia tekst na środek linijki w taki sposób aby zwracana linijka miała szerokość `width`.                                                                                                                                                                                              |
| `__fill(text: str, width: int) -> str`                                  | Generuje linijkę o szerokości `width` zawierającą tekst podany w argumencie. Dodaje znak spacji w celu uzupełnienia linijki do odpowiedniej szerokości. Dodaje znak '\|' na początek i koniec linijki. Znak ten reprezentuje lewą i prawą ramkę widoku.                                                      |
| `__equalize_height(lines: List[str], desired_len: int) -> List[str]`    | Przyjmuje listę linijek oraz docelową wysokość. Jednostką wysokości jest liczba znaków. Funkcja generuje puste linijki aby osiągnąć docelową wysokość. Zwraca zmodyfikowaną listę linijek.
| `__are_days_equal(date1: datetime, date2: datetime) -> bool` | Dla danych dat typu `datetime` sprawdza czy są one tego samego dnia. |

## Moduł `utils`
Moduł zawierający funkcje pomocnicze. 
### Publiczne funkcje

| Funkcja                                        | Opis |
|------------------------------------------------| - |
| `save_calendar(calendar: Calendar, path: str)` | Zapisuje podany kalendarz do pliku o ścieżce `path`. Formatem pliku jest `csv` |
| `load_calendar(path: str) -> Calendar` | Odczytuje plik o ścieżce `path` będący w formacie stworzonym przez funkcję `save_calendar`. Zwraca obiekt kalendarza, reprezentujący kalendarz zapisany w pliku |
| `print_list(lines: List)` | Iteruje po liście wypisując po kolei jej zawartość jako linijki |
| `date_to_str(date: datetime) -> str` | Konwertuje obiekt typu `datetime` do łańcucha o formacie `%d-%m-%Y %H:%M`. | 
| `parse_date_str(date_str: str) -> datetime` | Odwraca operację wykonywaną przez funkcję `date_to_str`. Konwertuje łańcuch znaków o formacie `%d-%m-%Y %H:%M` do obiektu typu `datetime`. |
| `onvert_month_to_num(month: str) -> int` | Konwertuje nazwę angielską nazwę miesiąca do odpowiadającej mu liczbie. | 

## Klasa `DuplicateEventException`
Klasa reprezentuje wyjątek występujący gdy nastąpiła próba dodania do kalendarza wydarzenia, które jest już w nim zawarte. 
Obiekty tej klasy mają ustawioną stałą wiadomość opisującą błąd. Konstruktor nie przyjmuje żadnych argumentów.

# Autor
Patryk Mikuli

S24087