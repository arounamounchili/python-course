"""
    Object oriented programming: Encapsulation, Abtraction, Inheritence and Polymorphism.
    Une Classe est un ensemble de variables d'instance et de méthodes associées
    qui définissent un type d'objet particulier. 
    On peut considérer une classe comme le plan ou le modèle d'un objet. 
    Les attributs sont les noms donnés aux variables qui composent une classe.

    La programmation orientée objet (POO) est un paradigme de programmation en informatique 
    qui repose sur le concept de classes et d'objets. Elle permet de structurer 
    un programme logiciel en éléments de code simples et réutilisables 
    (généralement appelés classes), qui sont utilisés pour créer des instances 
    individuelles d'objets
"""
"""Exmple basics"""
nom_proprietaire_compte1 = "Felix"
numero_compte1 = 123456789
solde_compte1 = 10000

nom_proprietaire_compte2 = "Marco"
numero_compte2 = 987654321
solde_compte2 = 5000

nom_proprietaire_compte3 = "Maximum"
numero_compte3 = 4000654321
solde_compte3 = 15000


class Comptebancaire:

    def __init__(self, nomProprietaire, numeroCompte, solde):
        """ Le constructeur est utilisé pour initialiser la classe
            Avec les attribus tels que: ...
        """
        self.nomProprietaire = nomProprietaire
        self.numeroCompte = numeroCompte
        self.solde = solde
    
    def depot(self, montant):
        """ Cette Methode permet d'éffectuer un dépôt d'un montant déterminé 
        """
        self.solde += montant

    def retrait(self, montant):
        """ Cette Methode permet d'éffectuer un retrait d'un montant spécifié.
            Retourne true si c'est possible, faux sinon. 
        """
        if(montant > self.solde):
            return False
        
        self.solde -= montant
        return True
    
    def __repr__(self):
        return f'{self.nomProprietaire} avec le numéro de compte {self.numeroCompte} dipose de {self.solde}€ dans son compte.'

compte1 = Comptebancaire("Steve", 123456789, 30000)
compte2 = Comptebancaire("Mbappe", 912345565, 10E12)
compte3 = Comptebancaire(nomProprietaire="Mounchili",solde= 1000000000,numeroCompte=54984544547383)
print(compte1.nomProprietaire)
print(compte1.numeroCompte)
print(compte1.solde)

print(compte1)
print(compte2)
print(compte3)

print()
compte1.numeroCompte = 10000000001
compte1.nomProprietaire = "Scrorpion"
print(compte1)


""" 
    Héritage: est la capacité d'une classe à hériter des méthodes 
    et/ou des caractéristiques d'une autre classe
"""
class ComptCourant(Comptebancaire):
    def __init__(self, nomProprietaire, numeroCompte, solde, maxDepense = 2000):
        super().__init__(nomProprietaire, numeroCompte, solde)
        self.maxDepense = maxDepense

class CompteEpargne(Comptebancaire):
    def __init__(self, nomProprietaire, numeroCompte, solde):
        super().__init__(nomProprietaire, numeroCompte, solde)
        self.epargne = 0.0
    
    def ajouteEpargne(self, montant):
        if montant > self.solde:
            return False
        
        self.epargne += montant
        return True


compte_courant1 = ComptCourant("Lionel", 3333333333, 1111)
print(compte_courant1.solde)
compte_courant1.depot(1000)
print(compte_courant1.solde)
compte_courant1.retrait(500)
print(compte_courant1.solde)

print(f"Votre max de depense est: {compte_courant1.maxDepense}.")

print()
compte_epargne1 = CompteEpargne("Mounchili", 5454545454, 1000)
if compte_epargne1.ajouteEpargne(1100):
    print(f"Vous venez d'epargner: {compte_epargne1.epargne}€.")
else:
    print(f"Impossible d'epargner. Votre solde est de {compte_epargne1.solde}€.")