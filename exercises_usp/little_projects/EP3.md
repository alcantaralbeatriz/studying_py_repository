## Exercício Prático 3

A espectrometria de massas de proteínas é um importante método para a caracterização de proteínas. Uma medida usada para caracterizar a massa de um elemento é a massa monoisotópica, que corresonde à soma das massas dos átomos do isótopo mais abundante de uma molécula.

Proteinas podem ser escritas como uma sequência de aminoácidos[[1](https://en.wikipedia.org/wiki/Protein)]. Entre os aminoácidos, existem 20 deles que são considerados os mais comumente encontrados, sendo cada um usualmente representado por uma letra do alfabeto. Assim, uma proteina poderia ser representada, por exemplo, pela seguinte string: `AQGHECH`. A massa monoisotópica de cada um dos aminoácidos principais é conhecida e pode ser vista na tabela 1.

Para obter a massa de uma proteína, basta somar a massa de seus aminoácidos. Desta forma, temos que a massa monoisotópica de `AQGHECH` é 762,283.

Crie um programa capaz de ler um arquivo de entrada no formato FASTA contendo diversas proteínas, calcular suas respectivas masas monoisotópicas e, ao final, imprimir os resultados obtidos em ordem crescente de massas.

Saída do seu programa:
```
Digite o nome do arquivo: proteinas.fasta
tamanho - proteina - sequência
```

Formato FASTA
Fasta é um formato bastante usado para representar sequências em bioinformática. Ele consiste de uma ou mais sequências onde cada uma é representada da seuinte forma: uma linha antes da sequência apresenta um rótulo ou descrição da sequência, que por sua vez vem apresentada na linha a seguir. A linha de descrição sempre começa com o caracter ```>```. A seguir mostramos um exemplo de um arquivo FASTA:

```
>Proteina_1
AQGHECH
>Proteina_2
AHGGHRHNSYWVVV
>Proteina_3
CEHG
```

Tabela de massas monoisotópicas dos principais aminoácidos. [Site de origem](http://education.expasy.org/student_projects/isotopident/htdocs/aa-list.html)

Aminoácido|Símbolo|Massa monoisotópica
---|---|---
Alanina|A|71.037
Arginina|R|156.101
Asparigina|N|114.042
Ácido aspártico|D|115.026
Cisteína|C|103.009
Ácido glutâmico|E|129.042
Glutamina|Q|128.058
Glicina|G|57.021
Histidina|H|137.058
Isoleucina|I|113.084
Leucina|L|113.084
Lisina|K|128.094
Metionina|M|131.040
Fenilalanina|F|147.068
Prolina|P|97.052
Serina|S|87.032
Treonina|T|101.047
Triptofano|W|186.079
Tirosina|Y|163.063
Valina|V|99.068

