## Exercício Prático 2
<br/>

Genótipos formam a constituição genética de um indivíduo. Os genótipos são normalmente representados usando um par de letras, como *AA*, *Aa* e *aa*. O genótipo de um descendente depende diretamente dos genótipos de ambos os pais e pode ser determinado usando o [quadro de Punnet](https://pt.wikipedia.org/wiki/Quadro_de_Punnett) (como exemplo a seguir):

|X|A|a|
|:---:|:---:|:---:|
|<b>A</b>|AA|Aa|
|<b>a</b>|Aa|aa|



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
|:---:|:---:|:---:|:---:|
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
|:---:|:---:|:---:|:---:|
|BB|BB|BB|0.04|
|BB|BB|Bb|0.00|
|BB|BB|bb|0.00|
|BB|Bb|BB|0.03|
|...|...|...|...|

<br/>

Porém, não podemos tomar esses valores como distribuições finais, pois estaríamos considerando que todos os ancestrais foram extintos d população. Os novos descendentes devem ser inseridos na população já existente. Isso é feito calculando as novas distribuições como uma média ponderada entre a distribuição antiga e a nova. Para isso, usaremos um fator de ponderação `µ` que deve estar no intervalo [0, 1].

Exemplo: assumindo µ = 0.6

>d^BB = (µ x dBB) + (1 - µ) x d'BB

>d^BB = (0.6 x 0.3) + (0.4 x 0.455)

>d^BB = 0.169

E estes serão os valores da distribuição após um ciclo de reprodução. Eles serão usados como entrada para o ciclo seguinte e assim sucessivamente.

Conforme você mesmo irá verificar no seu programa, após uma certa quantidade de gerações as distribuições tenderão a se estabilizar (não se modificarão muito mais). Para evitar que seu programa fique rodando simulações desnecessárias, usaremos um limiar `ε` que deve ser positivo e muito pequeno (p.ex. ε = 0.00001) para determinar que seu programa já pode ser parado, mesmo que as `n` gerações ainda não tenham sido simuladas.

O limiar deve ser usado da seguinte forma: seu programa deve parar de executar mais simulações a qualquer momento que a diferença entre a soma das distribuições anteriores e a soma das distribuições finais da geração atual for menor que ε. Mais formalmente, seu programa deve parar se

> |dBB - d^BB| + |dBb - d^Bb| + |dbb - d^bb| < ε:

Sendo que as barras verticais j indicam o valor absoluto (ou positivo) da diferença. Assim, seu programa deve parar em qualquer uma das duas situações: caso a diferença fique menor que o limiar ou caso todos os ciclos tenham sido simulados mesmo que a diferença ainda seja maior que o limiar.

<br/>

PROGRAMA

Seu programa deve requisitar as entradas numéricas no início:

- Número `n` de gerações que devem ser simuladas;
- Valor da distribuição inicial das plantas com genótipo BB (dBB), Bb e bb;
- Fator de ponderação `µ` da população;
- Valor limiar de parada `ε`.

Seu programa deve, obrigatoriamente, implementar pelo menos as seguintes funções (no mínimo):

- função verificaEntrada: que verifica os valores digitados, e imprime mensagem de erro nos seguintes casos: `n` menor que 0; soma das distribuições diferente de 1; `µ` fora do intervalo [0, 1]; `ε` negativo. Em qualquer um dos casos, a entrada deve ser ignorada e uma entrada nova deve ser solicitada.

- função quadroPunnet: dado os índices dos genótipos de ambos os pais e do filho, retorne a probabilidade do filho ser gerado de acordo com o quadro de Punnett. Atribuindo 0 para BB, 1 para Bb, e 2 para bb.

- função calculaProbabilidadeFilho: que recebe os índices dos genótipos de ambos os pais e do filho e as distribuições de cada genótipo e calcula a probabilidade de um filho com aquele genótipo nascer na próxima geração.

<u>Entradas e saídas:</u>

Após cada ciclo de reprodução, seu programa deve imprimir o número do ciclo em que está, seguido dos valores das três distribuições obtidas.

Segue abaixo um exemplo de uma possível execução do programa. Aqui usamos o prefixo “>” para indicar uma entrada do usuário e “#” para mensagens dadas pelo programa.

```
> Digite n: 3
> Digite d BB: 0.2
> Digite d Bb: 0.3
> Digite d bb: 0.4
> Digite mu: 0.6
> Digite epsilon: 0.00001
# Erro: soma das distribuicoes eh diferente de 1
> Digite n: 3
> Digite d BB: 0.2
> Digite d Bb: 0.3
> Digite d bb: 0.5
> Digite mu: 0.6
> Digite epsilon: 0.00001
# Ciclo 1: d BB = 0.169 -- d Bb = 0.362 -- d bb = 0.469
# Ciclo 2: d BB = 0.1504 -- d Bb = 0.3992 -- d bb = 0.4504
# Ciclo 3: d BB = 0.13924 -- d Bb = 0.42152 -- d bb = 0.43924

```

Boa sorte!
