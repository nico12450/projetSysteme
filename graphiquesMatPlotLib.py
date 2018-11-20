#!/usr/bin/env python3

import projetVCF as vcf
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go

dico = vcf.dico

chromosomes = dico.keys()
print(chromosomes)
variantsParChromosome = []

for c in chromosomes:
    variantsParChromosome.append(len(dico[c]))

print(variantsParChromosome)

plt.pie(variantsParChromosome, labels=chromosomes)
plt.axis('equal')
plt.show()

plt.bar(chromosomes,variantsParChromosome)
plt.title("nombre de variants par chromosome")
plt.show()

trace = go.Pie(labels = chromosomes, values = variantsParChromosome)
py.iplot([trace], filename='basic_pie_chart')