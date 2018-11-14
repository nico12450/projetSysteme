#!/usr/bin/env python3

import projetVCF as vcf
import matplotlib.pyplot as plt

dico = vcf.dico

chromosomes = dico.keys()
variantsParChromosome = []

for c in chromosomes:
    variantsParChromosome.append(len(dico[c]))

print(variantsParChromosome)

plt.pie(variantsParChromosome, labels=chromosomes)
plt.axis('equal')
plt.show()