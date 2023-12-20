from django.urls import path

from .views import cadastro, index, produto

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('produto/<int:pk>', produto, name='produto'),
]
