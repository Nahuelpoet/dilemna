import random

def resultat(p1, p2):
    if p1 == 0 and p2 == 0:
        return 1, 1
    elif p1 == 0 and p2 == 1:
        return 5, 0
    elif p1 == 1 and p2 == 0:
        return 0, 5
    elif p1 == 1 and p2 == 1:
        return 3, 3

pointsPlayer1 = 0
pointsPlayer2 = 0

p1 = 1
p2 = 1

to = 0

Iteration = 5

def tournoi(Iteration):
    global pointsPlayer1
    global pointsPlayer2   
    global p1
    global p2 
    global to
    for i in range(Iteration):
        pointsPlayer1 = 0
        pointsPlayer2 = 0
        tour = random.randint(50,100)
        print("Nombres de tours:",tour)
        for to in range(tour):
            p1 = AngerIssues()
            p2 = TitForTat(2)
            pointsPlayer1 = pointsPlayer1 + resultat(p1, p2)[0]
            pointsPlayer2 = pointsPlayer2 + resultat(p1, p2)[1]
        print("Points du joueur 1:",pointsPlayer1)
        print("Points du joueur 2:",pointsPlayer2)

def TitForTat(px):
    global to
    global p1
    global p2
    if px == 1:
        if p2 == 1 or to == 0:
         return 1 
        else:
            return 0
    else:
        if p1 == 1 or to == 0:
            return 1
        else:
            return 0

def AngerIssues():
    return 0

tournoi(Iteration)
