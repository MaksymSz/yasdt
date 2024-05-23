# Yet Another Symbolic Differentiation Tool

<details><summary>Dane kontaktowe</summary>
<ul>
    <li>szemermaksym@student.agh.edu.pl</li> 
</ul>
</details>

## Krótki opis projektu
Działanie projektu jest inspirowane działaniem biblioteki [sympy](https://www.sympy.org/).
Moduł **yasdt** umożliwia przetwarzanie symboliczne równań matematycznych zapisanych w postaci łańcucha znaków do postaci obiektów w języku Python, na których to można wykonywać dalsze operacje, między innymi różniczkownie.
Wejściowy ciąg jest skanowany, a następnie parsowany, po czym następuje generowanie kodu w języku Python, w którym to następuje wykonanie obliczeń symbolicznych implementowanych jako drzewo.
Wyrażenia mogą zostać uproszczone w celu pozbycia się redundantnych elementów, na przykład: `1*2x + 0*3 - 0` → `2x`

* ogólne cele programu: przetwarzanie wyrażeń symbolicznych
* język implementacji: **[Python](https://www.python.org/)**
* sposób realizacji parsera: **[ANTLR4](https://github.com/antlr/antlr4)**


## Gramatyka formatu
Opis formatu gramatyki oraz spis tokenów został wykonany w notacji wykorzystywanej przez narzędzie ANTLR4.
Odpowiednie pliku znajdują się w repozytorium, poniżej znajdują się odpowiednie odnośniki:
* [spis tokenów](https://github.com/MaksymSz/yasdt/blob/master/grammar/ExpressionGrammarLexer.g4)
* [opis gramatyki](https://github.com/MaksymSz/yasdt/blob/master/grammar/ExpressionGrammarParser.g4)

Poniżej znajduje się drzewo wyprowadzenie przykładowego wyrażenia $sin(2x) + 2x$
![parse_tree](https://github.com/MaksymSz/yasdt/blob/master/parseTree.png)

## Krótki opis obsługi wraz z przykładem użycia
1. **Prosty przykład parsowania wyrażenia**
    
   Wyrażenie najpierw zostaje sparsowane, następnie zostaje wyznaczona pochodna. Należy zauważyć że pochodna jest wyznaczana zgodnie z regułą łańcuchową, zatem powstają redundantne wyrażenie pokroju mnożenia przez **0** lub **1**.
    Wyrażenie może zostać poprzez wywołanie metody `simplify()`, bądź bezpośrednio w trakcie różniczkowania poprzez przekazanie parametru `True` do metody `diff()`.
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
   Każde obsługiwane wyrażenie w module ma możliwość ewaluacji dla podanego argumentu, rozumianego jako podstawienie wartości skalarnej pod `x`, przy pomocy metody `eval()`.
   Ponadto istnieje możliwość wygenerowania wykresu dla wyrażeń.
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
```console
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