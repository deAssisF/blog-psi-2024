from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=600)
    imagem = models.ImageField(blank=True)
    def __str__(self) -> str:
        return self.titulo
# Create your models here.
