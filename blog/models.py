from django.db import models


class Article(models.Model):

    designation= models.CharField(max_length=50)
    prix =models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    image=models.ImageField()



    def __str__(self) :
        return self.designation
    

class Commande(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_commande = models.DateTimeField(auto_now_add=True)
    estLivrer = models.BooleanField(default=False)

    def __str__(self):
        return f"Commande de {self.quantite} {self.article.nom}(s)"