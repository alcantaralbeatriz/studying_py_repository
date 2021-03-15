## Exercício Prático 2
<br/>
<body align=justify>
Genótipos formam a constituição genética de um indivíduo. Os genótipos são normalmente representados usando um par de letras, como *AA*, *Aa* e *aa*. O genótipo de um descendente depende diretamente dos genótipos de ambos os pais e pode ser determinado usando o quadro de Punnet (como exemplo a seguir):

X|A|a
---|---|---
<b>A</b>|AA|Aa
<b>a</b>|Aa|aa



De acordo com a tabela, o descendente teria então 25% de chance de possuir o genótipo *AA*, 25% para *aa* e 50% para *Aa*.

<br/>

Um produtor e cientista descobriu que um acidente químico recente em suas terras pode ter causado a mutação de um alelo B em sua plantação. Ele sabe que esta mutação danifica suas plantas e gostaria de saber se existe o risco desse genótipo se espalhar entre as demais após alguns ciclos de reprodução. Para isso, ele contratou competentes programadores (você s2) para desenvolver um programa que simule o que ocorrerá com a composição genética da plantação atual, caso a mutação se espalhe, ou mantê-la, se ela estiver controlada.

Seu programa deve ser capaz de receber a distribuição dos genótipos da plantação e determinar o que ocorrerá após *n* ciclos de reprodução. Para tanto seu programa deve executar n vezes o modelo de atualização das distribuições explicado a seguir.

A distribuição dos genótipos é dada a partir de três valores: `dBB`, `dBb`, `dbb`; onde representam a distribuição dos genótipos BB, Bb, e bb, respectivamente. Sendo que os valores estão no intervalo [0, 1] e a soma dos três deve ser 1.
A partir dos valores iniciais de `dBB`, `dBb`, e `dbb`, o modelo deve assumir cruzamentos aleatórios e independentes entre todas as plantas e determinar como as distribuições ficarão na próxima geração.

Como existem 3 genótipos diferentes, existem 9 possibilidades de cruzamentos possíveis. Assumindo que os cruzamentos são aleatórios e independentes, a probabilidade de cada um ocorrer é dada pela multiplicação das distribuições de cada progenitor.

<br/>

Exemplo:

Distribuições: dBB = 0.2; dBb = 0.3; dbb = 0.5

<br/>

<u>Tabela de probabilidade de cada cruzamento</u>

Pai|Mãe|Probabilidade|p
|---|---|---|---|
|BB|BB|0.2 x 0.2|0.04|
|BB|Bb|0.2 x 0.3|0.06|
|BB|bb|0.2 x 0.5|0.10|
|Bb|BB|0.3 x 0.2|0.06|
|Bb|Bb|0.3 x 0.3|0.09|
|Bb|bb|0.3 x 0.5|0.15|
|bb|BB|0.5 x 0.2|0.10|
|bb|Bb|0.5 x 0.3|0.15|
|bb|bb|0.5 x 0.5|0.25|

<br/>

Com a probabilidade de cada casal pode-se definir a probabilidade para cada tipo de descendente a partir de cada um dos possíveis casais.

<u>Para um cruzamento Bb x Bb:</u>

d'BB = 0.25 x 0.09 = 0.0225

d'Bb = 0.50 x 0.09 = 0.0450

d'bb = 0.25 x 0.09 = 0.0225

<u>(Parte da) Nova distribuição para todos os possíveis casais:</u>

|Pai|Mãe|Filho|Probabilidade|
|---|---|---|---|
|BB|BB|BB|0.04|
|BB|BB|Bb|0.00|
|BB|BB|bb|0.00|
|BB|Bb|BB|0.03|
|...|...|...|...|


Porém, não podemos tomar esses valores como distribuições finais, pois estaríamos considerando que todos os ancestrais foram extintos d população. Os novos descendentes devem ser inseridos na população já existente. Isso é feito calculando as novas distribuições como uma média ponderada entre a distribuição antiga e a nova. Para isso, usaremos um fator de ponderação `µ` que deve estar no intervalo [0, 1].

Exemplo: assumindo µ = 0.6

dfBB = (µ x dBB) + (1 - µ) x d'BB
dfBB = (0.6 x 0.3) + (0.4 x 0.455)
dfBB = 0.169

E estes serão os valores da distribuiçõ após um ciclo de reprodução. Eles serão usados como entrada para o ciclo seguinte e assim sucessivamente.

Conforme você mesmo irá verificar no seu programa, após uma certa quantidade de gerações as distribuições tenderão a se estabilizar (não se modificarão muito mais). Para evitar que seu programa fique rodando simulações desnecessárias, usaremos um limiar `ε` que deve ser positivo e muito pequeno (p.ex. ε = 0.00001) para determinar que seu programa já pode ser parado, mesmo que as `n` gerações ainda não tenham sido simuladas.




