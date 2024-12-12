from django.db import models

class Section(models.Model):
    designation = models.CharField(max_length=50)
    
    class Meta:
        ordering=('designation',)
    
    def __str__(self):
        return self.designation

class Departement(models.Model):
    designation = models.CharField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
        ordering = ("designation",)

    def __str__(self):
        return self.designation

class Promotion(models.Model):
    designation = models.CharField(max_length=50)
    actif = models.BooleanField(default=True)

    class Meta:
        ordering=("designation",)
    def __str__(self):
        return self.designation

class Etudiant(models.Model):
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True)
    sexe = models.CharField(max_length=50, choices=[("M", "Masculin"), ("F", "Feminin")])
    telephone = models.CharField(max_length=15, unique=True)
    departement=models.ForeignKey(Departement, on_delete=models.CASCADE)
    promotion=models.ForeignKey(Promotion, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.nom}-{self.postnom}-{self.prenom}-{self.promotion}-{self.departement}"


class Qualite(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom}"

class Beneficiere(models.Model):
    qualite = models.ManyToManyField(Qualite)
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True)
    sexe = models.CharField(
        max_length=50, choices=[("M", "Masculin"), ("F", "Feminin")]
    )

    def __str__(self):
        return f"{self.nom}-{self.postnom}-{self.prenom}"