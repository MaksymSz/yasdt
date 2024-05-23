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

* ogólne cele programu: przetwarzanie wyrażeń symbolicznych
* język implementacji: **[Python](https://www.python.org/)**
* sposób realizacji parsera: **[ANTLR4](https://github.com/antlr/antlr4)**


## Gramatyka formatu
Opis formatu gramatyki oraz spis tokenów został wykonany w notacji wykorzystywanej przez narzędzie ANTLR4.
Odpowiednie pliku znajdują się w repozytorium, poniżej znajdują się odpowiednie odnośniki:
* [spis tokenów](https://github.com/MaksymSz/yasdt/blob/master/grammar/ExpressionGrammarLexer.g4)
* [opis gramatyki](https://github.com/MaksymSz/yasdt/blob/master/grammar/ExpressionGrammarParser.g4)

Poniżej znajduje się drzewo wyprowadzenie przykładowego wyrażenia $sin(2x) + 2x$


## Informacje o stosowanych generatorach parserów, pakiety zewnętrzne


## Krótki opis obsługi

## Przykład użycia
```console
> from yasdt import parse
> expr = parse(
```
