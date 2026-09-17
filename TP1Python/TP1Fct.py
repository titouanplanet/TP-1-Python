#--------------------------------------------------------------------
#
#Nom : [PLANET Titouan]
#Date : [17-09-26]
#To DO : []
#
#--------------------------------------------------------------------

def calendrier(annee):
    """Fonction qui détermine si une année est bissextile ou non."""
    #entrée : annee (int) : l'année à vérifier
    #sortie : Valrent (bool) : True si l'année est bissextile, False sinon
    Valrent=0
    if (annee%4==0) and (annee%100==0):
        Valrent=True
    else :
        Valrent=False
    return Valrent

def nombre_jours_mois(mois, annee):
    """Fonction qui retourne le nombre de jours dans un mois donné d'une année donnée."""
    #entrée : mois (int), annee (int) : le mois et l'année à vérifier
    #sortie : Valrent (int) : le nombre de jours dans le mois
    if mois in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mois in (4, 6, 9, 11):
        return 30
    elif mois == 2:
        if calendrier(annee)==True:
            return 29
        else:
            return 28
    else:
        raise ValueError("Le mois doit être compris entre 1 et 12.")

def verifie_date(jour, mois, annee):
    """Fonction qui vérifie si une date est valide."""
    #entrée : jour (int), mois (int), annee (int) : le jour, le mois et l'année à vérifier
    #sortie : Valrent (bool) : True si la date est valide, False sinon
    if mois < 1 or mois > 12:
        return False
    if jour < 1 or jour > nombre_jours_mois(mois, annee):
        return False
    return True

def saisie_date():
    """Fonction qui demande à l'utilisateur de saisir une date et vérifie sa validité."""
    #entrée : aucune
    #sortie : print : affiche si la date est valide ou non
    jour = int(input("Entrez le jour : "))
    mois = int(input("Entrez le mois : "))
    annee = int(input("Entrez l'année : "))
    if verifie_date(jour, mois, annee):
        print(f"La date {jour}/{mois}/{annee} est valide.")
    else:
        print(f"La date {jour}/{mois}/{annee} n'est pas valide.")