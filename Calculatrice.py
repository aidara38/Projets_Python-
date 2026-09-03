class Personne:
    def se_presenter(self):
        print(f"Bonjour je m'appelle {self.nom} et j'ai {self.age} ans")


P1 = Personne()
P1.nom = "Alice"
P1.age = 25
P1.se_presenter()
      