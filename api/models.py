from django.db import models

# Create your models here.

cf = models.CharField

class Usuario(models.Model):

    choicesType = [
        ('LOCADOR', 'Locador'),
        ('LOCATARIO','Locatário')
    ]
    nome = cf(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefone = cf(max_length=20)
    tipo = cf(max_length=20, choices=choicesType)

    def __str__(self):
        return self.nome, self.email, self.telefone, self.tipo
    
class Imovel(models.Model):
    titulo = cf(max_length=100)
    tipo = cf(max_length=100)
    valorAluguel = models.DecimalField(max_digits=10, decimal_places=7)
    status = cf(max_length=20)

    locador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="imoveis")

    def __str__(self):
        return self.titulo
    

class Contrato(models.Model):
    datainicio = models.DateField()