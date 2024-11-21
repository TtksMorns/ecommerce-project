from django.urls import path
from . import views  # Importa o arquivo views.py do próprio app

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),  # Página de cadastro
    path('remover_produto/<int:produto_id>/', views.remover_produto, name='remover_produto'),  # Remover produto
    path('add_to_cart/<int:produto_id>/', views.add_to_cart, name='add_to_cart'),
    path('carrinho/', views.cart, name='cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]