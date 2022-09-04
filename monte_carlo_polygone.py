from matplotlib.pyplot import scatter, axis, show
from random import uniform
from math import pi, acos, sqrt

# Nombre de points à générer
NB_POINTS = 10000
nb=0

AIRE_TOTALE=4

X_in=[]
Y_in=[]
X_out=[]
Y_out=[]

# liste des sommets (Les sommets doivent être consécutifs + le dernier point = le premier)
#sommets=[(-1,0), (-0.25,0.25), (0,1), (1,0), (0.25,-0.1), (0,-1), (-0.75,-0.25), (-1,0)]
sommets=[(-1,0), (0,1), (1,0), (0,-1), (-1,0)]

# Test d'appartenance à un polygone
def estInterieur(x0,y0, sommets):
    """ Teste si le point (x0,y0) est intérieur au polygone
    dont les sommets sont donnés dans la liste.
    L'algorithme est basé sur le fait que la somme des angles sous lesquels on voit le côté du polygone
    depuis le point (x0,y0) est un multiple de 2pi.
    Ce multiple est impair si le point à tester est intérieur, pair si extérieur. 
    """
    angle=0
    for i in range(0,len(sommets)-1):
        scal=(sommets[i+1][0]-x0)*(sommets[i][0]-x0)+(sommets[i+1][1]-y0)*(sommets[i][1]-y0)
        normes=sqrt(((sommets[i+1][0]-x0)**2+(sommets[i+1][1]-y0)**2) * ((sommets[i][0]-x0)**2+(sommets[i][1]-y0)**2))
        vect=(sommets[i+1][1]-y0)*(sommets[i][0]-x0)-(sommets[i+1][0]-x0)*(sommets[i][1]-y0)

        if vect>0:
            angle+=acos(scal/normes)
        else:
            angle-=acos(scal/normes)

    if round(angle/2/pi, 0)%2==1:
        return True
    else:
        return False


for i in range(NB_POINTS):
    x=uniform(-1, 1)
    y=uniform(-1,1)
    if estInterieur(x,y,sommets):
        X_in.append(x)
        Y_in.append(y)
        nb+=1
    else:
        X_out.append(x)
        Y_out.append(y)

print("Approximation de l'aire bleue :", round(AIRE_TOTALE*nb/NB_POINTS,2))

scatter(X_in, Y_in, c='b', s=5, linewidth=0)
scatter(X_out, Y_out, c='r', s=5, linewidth=0)
axis("equal")
show()

