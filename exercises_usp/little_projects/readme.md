# Pequenos projetos

São exercícios práticos realizados durante a disciplina MAC0119 (Introdução à Computação) no período do mestrado em 2019. A disciplina era focada em ensinar linguagem de programação Python. :vulcan_salute:
---

### Primeiro Exercício Prático

Um grupo de cientistas está estudando uma população de insetos que vive em uma floresta tropical. Esses cientistas sabem que existe uma população máxima que o ambiente comporta destes animais, e eles podem estimar a população atual através de uma amostra. Com base nisso, eles conseguem a proporção de animais em relação à população máxima.
Durante o acompanhamento destes insetos por um ano, os cientistas descobriram um padrão que permitiu que eles formulassem um modelo para a forma como a reprodução destes animais evolui no tempo. A análise foi feita mensalmente, e a proporção da população em relação à população máxima para o próximo instante de tempo, definida como `xt+1`, era dada por:
    
>xt + 1 = rm * xt * (1 - xt)

Onde *rm* é o coeficiente associado à taxa de reprodução e escassez de alimento para o mês *m*. Além disso, eles tabelaram esses coeficientes, que mudam segundo as estações do ano, e são representados na tabela abaixo.

Estação|Verão|Inverno|Primavera e Outono
---|---|---|---
Meses|Dez, Jan, Fev|Jun, Jul, Ago|Demais meses
r*m*|3.65|3.3|3.5

Para auxiliar a equipe, que necessita de previsões futuras da população de insetos, você deve desenvolver um programa que, dada a condição atual da florestas, diga qual a proporção da população em relação à população máxima após *n* meses. 

A entrada e saída do seu programa deve ser como indicado abaixo:

```
Entre com a proporcao atual: 0.63
Entre com o mes atual: 7
Entre com o numero de meses no futuro: 87
```

Sendo que seu programa deve responder da seguinte forma.

````
A proporcao apos 87 meses e: 0.55
```

Plus: Este modelo foi diculgado por m biólogo chamado Robert May, e está relacionado com mapas logísticos e teoria do caos. Mais informações podem ser enconradas neste [link](https://en.wikipedia.org/wiki/Logistic_map).

---

### Segundo Exercício Prático

