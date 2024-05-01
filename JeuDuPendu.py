import random

L=["un","deux","cinq","rouge","membre","conseil","donner","reponse","etat","son","armement","peu","apres","vacances","annonce","mercredi","evident","regime","affirmer","arme"]

def get_caractere():
    caract = input("Proposez une lettre : ")
    #print(caract)
    return caract

def get_nombre_alleatoire(min,max):
    nbr_allea = random.randint(min,max)
    #print(nbr_allea)
    return nbr_allea

def choisir_mot(list):
    mot = get_nombre_alleatoire(0,len(L)-1)
    #print(L[index])
    return L[mot]

def init_etoile(mot):
    mot_cache = []
    long = len(mot)
    for i in range(long):
        mot_cache.append("*")
    #print(mot_cache)
    return mot_cache

def test_caractere(caract,mot,mot_cache):
    if caract in mot:
        for i in range(len(mot_cache)):
            if mot[i] == caract:
                mot_cache[i] = caract
        return True
    else:
        return False

def test_gagne(mot, mot_cache):
    if mot == "".join(mot_cache):
        return True
    else:
        return False
    
rejouer = "o"

while rejouer == "o":
    print("Bienvenue dans le Jeu du Pendu")


    mot_cache = []
    coups_restant = 10
    index = get_nombre_alleatoire(0,len(L)-1)
    mot = L[index]

    #print("triche : ", mot)

    mot_cache = init_etoile(mot)
    test_g = False

    while coups_restant > 0 and test_g == False:
        caract = get_caractere()
        test_c = test_caractere(caract,mot,mot_cache)
        test_g = test_gagne(mot,mot_cache)

        if test_c == False:
            coups_restant = coups_restant - 1
            print("Il vous reste ",coups_restant," à jouer")
            print("Le mot secret est : ", "".join(mot_cache))
        else:
            print("Il vous reste ",coups_restant," à jouer")
            print("Le mot secret est : ","".join(mot_cache))

        if test_g == True:
            print ("Bravo vous avez gagné, le mot secret était : ",mot)

    if coups_restant == 0:
        print("Il vous reste 0 coups à jouer")
        print("Désolé vous avez perdu !")

    rejouer = input("Voulez-vous rejouer ? (o / n)")