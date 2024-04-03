# repo2/main.py

from repo1.physique.loi import fonction_physique_1, fonction_physique_2
from repo2.utiles import fonction_utile_1

# Appels de fonctions depuis différents modules
resultat_physique_1 = fonction_physique_1()
resultat_physique_2 = fonction_physique_2()
resultat_utile_1 = fonction_utile_1()

print("Résultat physique 1:", resultat_physique_1)
print("Résultat physique 2:", resultat_physique_2)
print("Résultat fonction utile 1:", resultat_utile_1)
