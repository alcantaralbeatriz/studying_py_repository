import matplotlib.pyplot as plt
import random


random.seed(5)
notas = []
for i in range(10):
    notas.append(random.randrange(11))
print(notas)
