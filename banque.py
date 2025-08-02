import csv

class Banque:

    compteur = 1


    print()

    #utilisons notre constructeur

    def __init__(self, nom, email , mot_de_passe):

        self.compteur = Banque.compteur
        Banque.compteur += 1


        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.balance = 0
        self.type_compte = None


    def deposer(self, montant):

        if montant> 25000:

            self.balance += montant
            print()

            print(f"Nouvelle balance : {self.balance} FCFA")
            print()
        else:
            print()
            print("----Le dépôt doit être supérieur à 25000 FCFA-----")
            print()

    def choisir_compte(self):


        choix = input("Choisissez un type de compte (courant/epargne) : ").lower()

        print()
        if choix in ['courant', 'epargne'] :
            self.type_compte = choix
            print(f"---Vous avez choisi le compte : {choix}---")

        else:

            print("----Choix invalide. Veuillez réessayer----")
            print()
            self.choisir_compte()

    def retirer(self, montant):

        if montant > self.balance :

            print()
            print("---Retrait refuse . Fonds insuffisants---")

            return

        if self.balance - montant < 10000:
            print()
            print("---refus de retrait . vous devez avoir au moins 10000FCFA dans votre compte---")

            return

        if self.type_compte == 'courant' :

            if montant > 50000  :
                self.balance -= montant
                print()

                print(f"Balance restante: {self.balance} FCFA")
                print()


            else:
                print("---Retrait refusé . vous devez retirer au moins 50000FCFA---")

                print()
        elif self.type_compte == 'epargne':

                self.balance -= montant

                print()
                print(f"Retrait effectué. Balance restante: {self.balance} FCFA")

    def enregistrement_csv(self , montant_depot , montant_retrait):

        with open("banque.csv", "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                self.nom ,
                self.email ,
                self.mot_de_passe ,
                montant_depot ,
                montant_retrait ,
                self.type_compte ,
                self.balance
            ])

# --- Exécution du programme ---

nom = input("Entrez votre nom : ")
print()

email = input("Entrez votre email : ")

print()

mot_de_passe = input("Entrer votre mot de passe : ")

B1 = Banque(nom, email , mot_de_passe)

print()
montant_depot = int(input("Entrez le montant à déposer : "))
B1.deposer(montant_depot)

B1.choisir_compte()

print()
montant_retrait = int(input("Entrez le montant à retirer: "))
B1.retirer(montant_retrait)

B1.enregistrement_csv(montant_depot, montant_retrait)
