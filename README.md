# projetSysteme
projet vcf de l'UE système

authors : BARRY Nene Djenaba, GAMEL Nicolas
version : 1.0
prérequis : python3, matplotlib
installation : pas d'installation
utilisation : 

question biologique: Nous nous interessons à un fichier VCF répertoriant plusieurs variants structuraux : délétions, insertions, substitutions...

Le but de ce script est de visualiser globalement un fichier vcf, il permet de:

- Extraire et tester l'entete du fichier;
- D'avoir une vue sur les variants par chromosome;
- de selectionner une variation particulière et afficher son nombre d'occurences;
- Séléctionner un chromosome qui nous intéresse, afficher tous variants le concernant;

contraintes:

-le fichier à l'entrée doit etre un fichier.vcf;
-le fichier en entrée ne doit pas etre vide;
-les chomosomes qui n'ont pas une alternative de type : "\s<(.*?)[:>]" ne seront pas selectionnés;



