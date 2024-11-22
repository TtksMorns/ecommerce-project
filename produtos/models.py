from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='media/', null=True)
    TIPO_CHOICES = [
        ('verdureira', 'Verdureira'),
        ('acougue', 'Açougue'),
        ('limpeza', 'Limpeza'),
        ('frios', 'Frios'),
        ('bebidas', 'Bebidas'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nome
    
class CartItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)
    
    def get_total_price(self):
        return self.quantidade * self.produto.preco
