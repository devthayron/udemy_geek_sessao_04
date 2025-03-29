from django.shortcuts import render,redirect
from .forms import Contactform, ProdutoModelForm
from django.contrib import messages
from .models import Produto


def index(request):

    context = {
        'produtos' : Produto.objects.all()      #pega os dados do BD 
    }
    return render(request, 'index.html',context)


def contact(request):
    form = Contactform(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():         #retorna TRUE se não tiver erro
            form.send_mail()        #envia o email
            messages.success(request,'E-mail enviado com sucesso')
            form = Contactform()        #limpa o formulario apos tudo.
        else:
            messages.error(request,'Erro ao enviar o e-mail')
    context = {
        'formulario' : form
    }

    return render(request, 'contact.html',context)


def product(request):
    print(f'Usuario: {request.user}')   #verificar o usuario
    if str(request.user) != 'AnonymousUser':
        print(f'usuario logado')
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                
                messages.success(request,'Produto salvo com sucesso. ')
                form = ProdutoModelForm()
            else:
                messages.error(request,'Erro ao salvar o produto')
        else:
            form = ProdutoModelForm()
        context = {
                'form' : form
            }
        return render(request, 'product.html',context)

    else:
        return redirect('index')


