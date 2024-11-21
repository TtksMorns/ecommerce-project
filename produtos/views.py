from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def index(request):
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
    produtos = Produto.objects.all()

    if query:
        produtos = produtos.filter(
            models.Q(nome__icontains=query) | models.Q(tipo__icontains=query)
        )
    
    return render(request, 'lista_produto.html', {'produtos': produtos})