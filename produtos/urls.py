from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importa o arquivo views.py do próprio app

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),  # Página de cadastro
    path('remover_produto/<int:produto_id>/', views.remover_produto, name='remover_produto'),  # Remover produto
    path('add_to_cart/<int:produto_id>/', views.add_to_cart, name='add_to_cart'),
    path('carrinho/', views.cart, name='cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('detalhe_produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]