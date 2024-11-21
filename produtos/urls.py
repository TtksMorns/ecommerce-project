from django.urls import path
from . import views  # Importa o arquivo views.py do próprio app

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),  # Página de cadastro
    path('remover_produto/<int:produto_id>/', views.remover_produto, name='remover_produto'),  # Remover produto
]