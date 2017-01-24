from django.contrib import admin

# Register your models here.
from app.models import Livro


class LivroAdmin(admin.ModelAdmin):
    """
    Admin class for blog posts.
    """
    list_display = (
        'titulo', 'dono', 'isbn', 'autor', 'imagem', 'arquivo', 'tipo_livro', 'criado_em',
        'editado_em', 'status')
    list_filter = ('tipo_livro', 'dono', 'status')


admin.site.register(Livro, LivroAdmin)
