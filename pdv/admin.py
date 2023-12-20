from django.contrib import admin

# Register your models here.
from .models import Cadastro, Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'referencia')

class CadastroAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'nome_fantasia', 'telefone_celular', 'email')    

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cadastro, CadastroAdmin)