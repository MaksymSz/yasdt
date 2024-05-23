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
![logo](https://github.com/MaksymSz/yasdt/blob/master/parseTree.png)

## Krótki opis obsługi wraz z przykładem użycia
```console
>>> from yasdt import parse
>>> expr = parse('x*x + 2 + 3')
>>> expr
x*x+(2+3)
>>> expr.diff()
(1*x+x*1)+(0+0)
>>> expr.diff(True)
2x
````
