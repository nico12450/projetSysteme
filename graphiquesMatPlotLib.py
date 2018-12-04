#!/usr/bin/env python3

import projetVCF as vcf
import matplotlib.pyplot as plt


dico = vcf.dico
dicoAlt = vcf.dicoAlt

print(dico)

chromosomes = dico.keys()
print(chromosomes)
variantsParChromosome = []

for c in chromosomes:
    variantsParChromosome.append(len(dico[c]))

alternatives = dicoAlt.keys()
variantsParAlternatives = []

for a in alternatives:
	variantsParAlternatives.append(dicoAlt[a])


print(variantsParChromosome)

plt.pie(variantsParChromosome, labels=chromosomes)
plt.axis('equal')
plt.show()

plt.bar(chromosomes,variantsParChromosome)
plt.title("nombre de variants par chromosome")
plt.show()

plt.pie(variantsParAlternatives, labels=alternatives)
plt.axis('equal')
plt.show()

#print(dicoAlt)
#afficher le nombre de variants pour le chromosome 4
print(len(dico["4"]))

#afficher les variants du chromosome 5
print(dico["5"])
