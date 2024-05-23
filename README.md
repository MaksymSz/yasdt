# YASDT - Yet Another Symbolic Differentiation Tool

<details><summary>Dane kontaktowe</summary>
<ul>
    <li>szemermaksym@student.agh.edu.pl</li> 
</ul>
</details>

## Krótki opis projektu

Celem projektu jest umożliwienie przekształcania wyrażeń zapisanych w
formie tekstowej na obiekty Python, na których można wykonywać różnorodne operacje,
w tym różniczkowanie.

Działanie projektu jest inspirowane działaniem biblioteki [SymPy](https://www.sympy.org/).
Moduł **yasdt** umożliwia przetwarzanie symboliczne równań matematycznych zapisanych w postaci łańcucha
znaków do postaci obiektów w języku Python, na których to można wykonywać dalsze operacje, między innymi różniczkownie.
Wejściowy ciąg jest skanowany, a następnie parsowany, po czym następuje generowanie kodu w języku Python,
w którym to następuje wykonanie obliczeń symbolicznych implementowanych jako drzewo.
Wyrażenia mogą zostać uproszczone w celu pozbycia się redundantnych elementów, na przykład: `1*2x + 0*3 - 0` → `2x`

> **_Uwaga:_**  Różniczkowanie symboliczne oraz upraszczanie zostały zaimplementowane od zera, do przetwarzania wyrażeń
> projekt wykorzystuje tylko moduły dostępne w bibliotece standardowej Pythona

* ogólne cele programu: Głównym celem programu jest przetwarzanie wyrażeń symbolicznych w celu ich różniczkowania,
  uproszczenia oraz wykonywania na nich operacji matematycznych. Wyrażenia te mogą być następnie analizowane,
  uproszczone i używane do generowania wykresów.
* język implementacji: Projekt został zaimplementowany w języku **[Python](https://www.python.org/)**, co zapewnia dużą
  elastyczność i dostępność bogatej biblioteki narzędzi oraz bibliotek do obliczeń matematycznych i wizualizacji danych.
* sposób realizacji parsera: Parser został zrealizowany za pomocą narzędzia **[ANTLR4](https://github.com/antlr/antlr4)
  **
  **, które umożliwia tworzenie analizatorów składniowych dla różnych języków. ANTLR4 pozwala na definiowanie gramatyk
  oraz generowanie kodu parsera w wybranym języku programowania.
* wykorzystywane zewnętrzne moduły: Do generowania wykresów zostały użyte
  biblioteki **[matplotlib](https://matplotlib.org)** oraz **[NumPy](https://numpy.org/)**

## Główne etapy przetwarzania wyrażeń obejmują:

1. Skanowanie - analizowanie ciągu wejściowego.
2. Parsowanie - przekształcenie skanowanego tekstu w strukturę danych.
3. Generowanie kodu Python - tworzenie kodu, który wykonuje obliczenia symboliczne za pomocą drzewa wyrażeń.

## Gramatyka formatu

Opis formatu gramatyki oraz spis tokenów został wykonany w notacji wykorzystywanej przez narzędzie ANTLR4.
Odpowiednie pliku znajdują się w repozytorium, poniżej znajdują się odpowiednie odnośniki:

* [spis tokenów](https://github.com/MaksymSz/yasdt/blob/master/grammar/ExpressionGrammarLexer.g4)
* [opis gramatyki](https://github.com/MaksymSz/yasdt/blob/master/grammar/ExpressionGrammarParser.g4)

> **_Uwaga:_** Pewne produkcje mogą wydawać się niepotrzebne, jednak zostały one dostosowane w taki sposób aby
> gramatyka była klasy $LL(k)$, ponieważ takie gramatyki obsługuje ANTLR4

Poniżej znajduje się drzewo wyprowadzenie przykładowego wyrażenia $sin(2x) + 2x$
![parse_tree](https://github.com/MaksymSz/yasdt/blob/master/parseTree.png)

## Krótki opis obsługi wraz z przykładem użycia

1. **Prosty przykład parsowania wyrażenia**

   Projekt umożliwia parsowanie wyrażeń matematycznych oraz wyznaczanie ich pochodnych. Pochodna jest wyznaczana zgodnie
   z regułą łańcuchową, co może prowadzić do powstawania redundantnych wyrażeń, takich jak mnożenie przez 0 lub 1.
   Uproszczenie wyrażenia można osiągnąć poprzez wywołanie metody simplify(), lub bezpośrednio podczas różniczkowania
   przekazując parametr True do metody diff().

```console
>>> from yasdt import parse
... expr = parse('x*x + 2 + 3')
... expr
x*x+(2+3)
>>> expr.diff()
(1*x+x*1)+(0+0)
>>> expr.diff(True)
2x
````

2. **Obsługa operacji elementarnych**
   W module została zaimplementowana obsługa elementarnych operatorów na przetworzonych wyrażeniach.

```console
>>> from yasdt import parse
... expr0, expr1, expr2 = parse('2x + 2'), parse('-3x'), parse('sin(e^{2x})')
... expr0 + expr1
(2x+2)-3x
>>> expr1 * expr2
-3x*sin(e^2x)
```

3. **Generowanie wykresów**
   Każde obsługiwane wyrażenie w module ma możliwość ewaluacji dla podanego argumentu, rozumianego jako
   podstawienie wartości skalarnej pod `x`, przy pomocy metody `eval()`.
   Ponadto istnieje możliwość wygenerowania wykresu dla wyrażeń poprzez funkcję `yasdt.utils.plot()`,
   która wykorzystuje w swojej implementacji bibliotekę matplotlib.

```console
>>> from yasdt import parse
... expr = parse('2x + 2)
... expr.eval(2)
6
>>> from yasdt.utils import plot
... raw_expressions = ['2+3', 'x+x*x', 'sin(x) + cos(x + 3.14/2)', 'e^{sin(2x) + ln(x+3)}']
... parsed = [parse(e) for e in raw_expressions]
... plot(parsed, -2, 2, True)
```

![plot](https://github.com/MaksymSz/yasdt/blob/master/plot_demo.png)

4. **Złożony przykład**
   Poniżej przedstawiono bardziej zaawansowany przykład, w którym wyznaczane są pochodne wyrażeń, wykonywane są na nich
   operacje, a następnie generowany jest wykres.

```python
from yasdt import parse
from yasdt.utils import plot

raw_expressions = ['2+3x', 'sin(x)+x*x', 'sin(x) + cos(x)', 'e^{sin(2x) + ln(x+3)}']
parsed = [parse(e) for e in raw_expressions]
derivatives = [e.diff(True) for e in parsed]
e0 = derivatives[0] + derivatives[2]
e1 = parsed[3] * derivatives[0]
e2 = (e0.diff(True) + e1).simplify
plot((e2, e2.diff(True)), -2, 2, True, linestyle=':')
```

![plot](https://github.com/MaksymSz/yasdt/blob/master/plot_adv.png)

## Więcej przykładów

Poniżej znajduje się tabela zawierająca wejściowy łańcuch w celu jego przetworzenia oraz pochodną tego wyrażenia po
uproszczeniu. **YASDT** pozbywa się z wyrażeń nie tylko zbędnych mnożeń przez `1` oraz mnożeń i dzieleń przez `0`, lecz
także upraszcza wyrażenia do postaci która jest przejrzystsza dla człowieka, np. `2sin(x) + 3sin(x)` zostaje uproszczone
do `5sin(x)`.

|    |        Wyrażenie do sparsowania        |     Wyznaczona pochodna po uproszczeniu      |
|:--:|:--------------------------------------:|:--------------------------------------------:|
| 1  |                  2+3                   |                      0                       |
| 2  |                 2+2*2                  |                      0                       |
| 3  |               x + x * x                |                     1+2x                     |
| 4  |             x * x + x * x              |                      4x                      |
| 5  |            sin(x) + cos(2x)            |               -2sin(2x)+cos(x)               |
| 6  |       12.3*sin(x) + 12.3*sin(x)        |                  24.6cos(x)                  |
| 7  |         sin(e^x) * ln(x - 2x)          |     e^x*cos(e^x)*ln(-x)+sin(e^x)*(-1/-x)     |
| 8  | (x + 2x) * sin(-4x + e^3) + cos(x * x) | cos(-4x+e^3)*-12x+3sin(-4x+e^3)+-sin(x*x)*2x |
| 9  |       e^{sin(2 * x)} + 3x^2 - 5        |           2cos(2*x)*e^sin(2*x)+6x            |
| 10 |          (-12.3*e^x + 7) / x           |          (-12.3e^x*x-7+12.3e^x)/x^2          |
| 12 |     2x + 3 - 2x + sin(x) - sin(x)      |                      0                       |

## Podsumowanie

Moduł **YASDT** to zaawansowane narzędzie do symbolicznego przetwarzania i różniczkowania wyrażeń matematycznych. Dzięki
wykorzystaniu ANTLR4 do parsowania oraz Pythona do implementacji obliczeń symbolicznych, narzędzie to oferuje szerokie
możliwości analizy i wizualizacji wyrażeń matematycznych. Umożliwia nie tylko wyznaczanie pochodnych i uproszczanie
wyrażeń, ale również generowanie wykresów, co czyni go wszechstronnym narzędziem do pracy z wyrażeniami matematycznymi.