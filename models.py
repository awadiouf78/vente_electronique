from django.db import models

# Create your models here.
class client(models.Model):
    nom=models.charfield(max_length=120)
    prenom=models.charfield(max_length=120)
    telephone=models.charfield(max_length=50)
    adresse=models.charfield(max_length=120)
    def_str_(self):
        return f"{self.nom} {self.prenom}"
             


class produit(models.Model):

    nom=models.charfield(max_length=120)
    category=models.charfield(max_length=40)
    prix=models.integerfield(max_length=120)
    def_str_(self):
        return f"{self.nom}{self.category} {self.prix}"
     

