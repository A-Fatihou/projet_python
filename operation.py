

def addition(a, b):
    return a + b

def multiplication3(a):
    return 3*a

def oper():
    # l'objectif est de prendre un entier l'additionner avec un autre et le multiplier par 3
    
    entier1 = int(input("Entrez un entier : "))
    entier2 =  int(input("Entrez un autre entier : "))
    return addition(entier1, entier2), multiplication3(entier1)
resultat, resultat2 = oper()
print("Le résultat de add est :", resultat )
print("Le résultat de mutl est :", resultat2 )