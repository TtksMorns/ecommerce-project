from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, CartItem
from django.db.models import Q
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('/lista_produto')
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def cadastro_produto(request):
    return render(request, 'cadastro_produto.html')

def cadastro_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        tipo = request.POST['tipo']
        imagem = request.FILES.get('imagem')

        # Cria o produto no banco de dados
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco, tipo=tipo, imagem=imagem)

        # Redireciona para a página inicial
        return redirect('index')

    return render(request, 'cadastro_produto.html')

def remover_produto(request, produto_id):
    if request.method == 'POST':
        produto = get_object_or_404(Produto, id=produto_id)
        produto.delete()
        return redirect('index')


def lista_produto(request):
    query = request.GET.get('q')
    cart_items = CartItem.objects.all()
    produtos = Produto.objects.all()

    if query:
        produtos = produtos.filter(
            Q(nome__icontains=query) | Q(tipo__icontains=query)
        )
    
    return render(request, 'index.html', {'produtos': produtos, 'cart_items': cart_items})

def add_to_cart(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    cart_item, created = CartItem.objects.get_or_create(produto=produto)
    cart_item.quantidade += 1
    cart_item.save()
    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.get_total_price() for item in cart_items)
    return render(request, 'carrinho.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, cart_item_id):
     if request.method == 'GET':
        item = get_object_or_404(CartItem, id=cart_item_id)
        if item.quantidade == 1: 
            item.delete()
            return redirect('cart')
        else:
            item.quantidade -= 1
            item.save()
            return redirect('cart') 
    