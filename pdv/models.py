from django.db import models


# Create your models here.
class Cadastro(models.Model):
    razao_social          = models.CharField('Razão Social', max_length=100, blank=False)
    nome_fantasia         = models.CharField('Nome Fantasia', max_length=100, blank=False)
    cpf_cnpj              = models.CharField('CPF/CNPJ', max_length=14, blank=False)
    inscricao_estadual_RG = models.CharField('Inscrição Estadual/RG', max_length=30)
    telefone              = models.CharField('Telefone Fixo', max_length=10)
    telefone_celular      = models.CharField('Celular', max_length=11)
    email                 = models.CharField('E-mail', max_length=100)
    contato               = models.CharField('Contatos', max_length=40)
    limite_credito        = models.DecimalField('Limite de Crédito', decimal_places=2, max_digits=7)
    numero_inteiro        = models.IntegerField('Número qualquer')

    def __str__(self):
        return f'{self.razao_social}  -  {self.nome_fantasia}'

class Produto(models.Model):
    nome           = models.CharField('Nome', max_length=100, blank=False)
    marca          = models.CharField('Marca', max_length=100, blank=False)
    referencia     = models.CharField('EAN/GTIN', max_length=14)
    unidade_medida = models.CharField('Unidade de Medida', max_length=10)

    def __str__(self):
        #return f'{self.marca}  -  {self.nome}'
        return self.nome
