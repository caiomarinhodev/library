from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Auditavel(models.Model):
    class Meta:
        abstract = True

    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


# class Genero(Auditavel):
#     nome = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = "Genero"
#         verbose_name_plural = "Generos"
#         ordering = ("nome",)


TIPO = (
    ('FISICO', 'FISICO'),
    ('EBOOK', 'EBOOK')
)


class Livro(Auditavel):
    titulo = models.CharField(max_length=300)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=100, blank=True, null=True, verbose_name='ISBN')
    autor = models.CharField(max_length=100, blank=True, null=True)
    imagem = models.URLField(blank=True, null=True)
    arquivo = models.URLField()
    tipo_livro = models.CharField(max_length=100, choices=TIPO, verbose_name='Tipo do Livro')

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ("titulo",)
