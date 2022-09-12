import matplotlib.pyplot as plt
from random import uniform
from math import pi, cos, sin, floor
from numpy import where, empty

# Nombre de lignes du plancher
n=5

# Longueur de l'aiguille
l=1

# Précision
epsilon = 1e-3

# Création des axes verticaux
plt.axis('square')
plt.xlim(0,n)
plt.ylim(0,n)

# Création des lignes du plancher (lignes verticale à 1, 2, ,3 ...
for i in range(1,n):
    plt.axvline(x=i)

# Teste si l'aiguille coupe une ligne du plancher
# L'aiguille ne coupe pas une ligne du plancher si :
# l'abscisse du milieu et celle de la pointe droite ont la même partie entière
# et l'abscisse du milieu et celle de la pointe gauche ont la même partie entière
def teste(x, theta):
    if floor(x+l/2*cos(theta))==floor(x) and floor(x-l/2*cos(theta))==floor(x):
        return False    # Ne coupe pas
    else :
        return True     #coupe

def genere_et_teste_aiguille():
    """
    On génère aléatoirement l'abscisse et l'ordonnée du milieu
    ainsi que l'inclinaison de l'aiguille
    On calcule abscisses et ordonnées des extrémités
    et on dessine le segment correspondant.
    La fonction renvoie False si l'aiguille ne coupe pas sinon elle renvoie True
    """
    
    x=uniform(l/2+epsilon, n-l/2-epsilon)
    y=uniform(l/2+epsilon, n-l/2-epsilon)
    theta=uniform(-90, 90)

    X=[x-l/2*cos(theta), x+l/2*cos(theta)]
    Y=[y-l/2*sin(theta), y+l/2*sin(theta)]
    plt.plot(X,Y, 'r', linewidth=0.5)
    X, Y = [], []

    return teste(x, theta)

# Nombre d'aiguilles à lancer
nb_aiguilles = 20

# Compte les aiguilles qui coupent les lignes du plancher
cpt = 0

for i in range(nb_aiguilles):
    coupe = genere_et_teste_aiguille()
    if  coupe:
        cpt +=1

print("Nombre d'aiguilles qui coupent :", cpt)
print("Proba correspondante :", round(cpt / nb_aiguilles,2))
plt.show()
    

    
