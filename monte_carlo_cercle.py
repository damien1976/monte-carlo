from matplotlib.pyplot import scatter, axis, show
from random import uniform

NB_POINTS = 10000
nb=0

AIRE_TOTALE=4

X_in=[]
Y_in=[]
X_out=[]
Y_out=[]

for i in range(NB_POINTS):
    x=uniform(-1, 1)
    y=uniform(-1,1)
    if x**2+y**2<=1:
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
    
