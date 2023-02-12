# monte-carlo
Programmation de la méthode de Monte-Carlo pour le calcul d'aires.

La méthode de Monte-Carlo est une méthode probabiliste consistant à répéter une expérience un grand nombre de fois pour en déduire des valeurs approchées d'aires.
L'idée est de choisir uniformément au hasard un grand nombre de points dans une surface d'aire connue (Le grand carré dans la figure ci-dessous) englobant la surface dont on veut calculer l'aire (la surface bleue dans la figure ci-dessous).
On doit disposer d'un test indiquant, pour chaque point, s'il appartient ou non à la surface dont on veut calculer l'aire. Le rapport entre le nombre de points appartenant à cette surface et le nombre de points total donnera une approximation de l'aire recherchée. 

![image](https://user-images.githubusercontent.com/46868436/188307064-77272333-597c-4489-b02a-b25aae09f024.png)

Dans le cas des polygones dont la surface est définie par les sommets du polygone sous forme d'une liste de points, la difficulté consiste à trouver un test indiquant si le point généré aléatoirement est intérieur ou extérieur à la surface considérée. 
L'idée retenue ici consiste à déterminer la somme des angles orientés sous lesquels sont vus deux sommets consécutifs du polygone depuis le point généré aléatoirement : 
- Si cette somme est un multiple de $2\pi$ et que ce multiple est pair alors le point est extérieur au polygone (représenté en rouge sur les figures ci-dessous) ;
- Si cette somme est un multiple de $2\pi$ et que ce multiple est impair alors le point est intérieur au polygone (représenté en bleu sur les figures ci-dessous).

![image](https://user-images.githubusercontent.com/46868436/188307241-9f0c8be1-f879-4885-8cb0-c5396e88ef4c.png)

![image](https://user-images.githubusercontent.com/46868436/188307271-082ab8d9-1e82-47a1-b9a6-638a2c064ff0.png)

Dans le même ordre d'idée, on présente aussi l'expérience de l'aiguille de Buffon qui consiste à laisser tomber et compter le nombre d'aiguilles coupant les lignes d'un plancher. Le rapport entre ce nombre et le nombre total d'aiguilles doit s'approcher de $\frac{2l}{n\pi }$ où $l$ est la longueur des aiguilles et $n$ représente l'écartement de deux lignes consécutives du plancher. 

![image](https://user-images.githubusercontent.com/46868436/189622776-1b04e473-11f2-43c7-9504-1bbff2e11304.png)

