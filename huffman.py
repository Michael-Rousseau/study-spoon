"""
Created on Wed Jan 26 10:15:29 2022

@author: Michael and Julian
"""

import pickle


class Arbre:

    """création d'un arbre binaire avec une classe"""

    def __init__(self, val, g=None, d=None):
        self.val = val
        self.g = g
        self.d = d

    def ssag(self):
        # recuperer le sous arbre gauche
        return self.g

    def ssad(self):
        #recuperer le sous arbre droit
        return self.d

    def valeur(self):
        # tete de l'arbre
        return self.val

    def insertg(self, ssag):
        # inserer à gauche 
        self.g = ssag

    def insertd(self, ssad):
        #inserer à droite
        self.d = ssad

    def divise(self):
        #divise le tuple (arbre, priorité)
        return self[0], self[1]


class FAP:

    """création d'une classe file a priorité """

    def __init__(self):

        self.liste = []

    def est_vide(self):
        #savoir si FAP est vide
        if self.liste == []:
            return True
        return False

    def rest_1(self):
        #true si il reste un élement"""
        if len(self.liste) == 1:
            return True
        return False

    def enfiler(self, elt):
        #par dichotomie car la FAP est triée
        taille = len(self.liste) 
        if taille == 0:
            self.liste += [elt]
        else:
            borne_gauche = 0
            borne_droite = taille
            while True:
                self.liste.sort(key = lambda x: x[1], reverse = True)
                x = (borne_droite + borne_gauche) // 2
                if elt[1] == self.liste[x][1]:
                    self.liste.insert(x, elt)
                    return 
                elif elt[1] > self.liste[x][1]:
                    # gauche
                    borne_droite = x
                    if borne_gauche == 0:
                        self.liste.insert(x, elt)
                        return
                else:
                    # droite
                    if borne_droite - borne_gauche <= 1:
                        self.liste.insert(x + 1, elt)
                        return
                    borne_gauche = x
        


    def defiler(self):
        #recuperer le dernier element de la liste 
        return self.liste.pop()

    def __str__(self):
        #méthode str
        ch = ""
        for x in self.liste:
            ch += str(x) + ""
        return ch

    def vide_liste(self):
        #permet de verifier si la liste est vide
        for x in self.liste:
            self.liste.pop()


def creer_table_o(chaine_cara, table_occurence={}):
    
    """ renvoie un dictionnaire listant les occurences de chaque caractère dans le texte"""
    
    print("making occurence table...")
    for caractere in chaine_cara:
        if caractere not in table_occurence:
            table_occurence[caractere] = 1
        else:
            table_occurence[caractere] = table_occurence[caractere] + 1
    print("made")
    return table_occurence


def trans(table_occurence):
    
    """permet de transformer les elements du dictionnaire en tuples pour enfiler les tuples correspondants"""
    
    l = FAP()
    for x, y in table_occurence.items():
        l.enfiler((Arbre(x), y))
    return l


def creer_arbre(l):
    
    """ crée l'arbre en défilant 2 tuples pour les assembler et enfiler à gauche, tant qu'il n'en reste pas qu'un seul dans la file"""
    
    print("making tree...")
    while not l.rest_1():
        a, b = l.defiler(), l.defiler()
        c = (Arbre(str(a[0].val) + str(b[0].val), a[0], b[0]), a[1] + b[1])
        l.enfiler(c)
    print("made")
    return l.defiler()


def convertir(abr):
    #permet de récuperer l'arbre dans le tuple, la priorité n'étant plus utile
    if type(abr) == tuple:
        abr = abr[0]
    return abr


def afficher(abr, niv=0):
    #methode pour afficher l'arbre ( servie pour les tests)
    if convertir(abr) is not None:
        afficher(convertir(abr).d, niv=niv + 1)
        print("     " * niv, convertir(abr).val)
        afficher(convertir(abr).g, niv=niv + 1)



def parcours_branche(arbre, A="", table_codage={}):
    
    """ crée la table de codage à partir de l'arbre final """
    
    if convertir(arbre).g is None and convertir(arbre).d is None:
        #test si l'arbre est vide, cas de base
        table_codage[convertir(arbre).val] = A
    else:
        gauche = convertir(arbre).g
        droite = convertir(arbre).d
        #appels du parcour de l'arbre
        parcours_branche(gauche, A + "0", table_codage)
        parcours_branche(droite, A + "1", table_codage)
    return table_codage

def Encoder_(contenu):

    """renvoyer deux fichiers, un le fichier codé et l'autre la table d'occurence"""
    print("making files...")
    table_occ = creer_table_o(contenu)
    table_codage = parcours_branche(creer_arbre(trans(table_occ)))
    with open('fichier_pickle', "wb") as f:
        pickle.dump(table_occ, f)
    with open('fichier_encode.txt', "w+") as f:
        for ch in contenu:
            a_ecrire = table_codage[ch]
            f.write(a_ecrire)
    print("Done")



def decoder_avec_arbre(arbre, ch, i=0):
    
    """ parcours l'arbre avec le fichier_encode (la suite de bites) et renvoie les caractères """

    racine = convertir(arbre)
    with open("Fichier_final_decode.txt", "w+") as f:
        while i < len(ch) - 1:
            while not convertir(arbre).g is None:
                if ch[i] == "0":
                    arbre = convertir(arbre).g
                    i += 1
                elif ch[i] == "1":
                    arbre = convertir(arbre).d
                    i += 1
            new = convertir(arbre).val
            f.write(new)
            arbre = racine


def decoder(fichier_pickle, fichier_encode):
    
    """application de la méthode decoder_avec_arbre sur les fichiers selectionner dans le fichier test"""
    print("decoding...")
    arbre = creer_arbre(trans(fichier_pickle))
    decoder_avec_arbre(arbre, fichier_encode)
    print("decoded")