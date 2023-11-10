from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    
    foto_perfil = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    nome = models.CharField(max_length=40,help_text="Digite seu nome aqui")
    contato = models.CharField(max_length=11,help_text="Digite seu numero aqui")
    
    class Meta:
        verbose_name="Usuarios"
        verbose_name_plural="Usuarios"
    


class Imovel(models.Model):


    TIPO_IMOVEL = [
        ("casa","Casa"),
        ("apto","Apartamento"),
        ("sitio","Sitio"),
        ("kitnet","Kitnet"),
    ]

    DISPONIBILIDADE = [
        ("disponivel","Disponivel"),
        ("indisponivel","Indisponivel"),   
    ]

    

    imagens = models.ImageField(upload_to='imoveis/', null=True, blank=True)
    tipo_imovel=models.CharField(choices=TIPO_IMOVEL,max_length=50)
    estado = models.CharField(max_length=30,help_text="Digite o estado do imóvel")
    cidade= models.CharField(max_length=30,help_text="Digite a cidade do imóvel")
    bairro= models.CharField(max_length=30,help_text="Digite o bairro do imóvel")
    rua= models.CharField(max_length=30,help_text="Digite a rua do imóvel")
    preco= models.FloatField(max_length=30,help_text="Digite o preço do imóvel")
    area= models.FloatField(max_length=30,help_text="Digite a área do imóvel")
    disponibilidade= models.CharField(choices=DISPONIBILIDADE,max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,max_length=50)
    descricao = models.TextField(max_length=500)
    class Meta:
        verbose_name="Imovel"
        verbose_name_plural="Imoveis"

    def __str__(self):
        return "Imovel "+self.rua
    