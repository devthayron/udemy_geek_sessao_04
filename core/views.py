from django.shortcuts import render
from .forms import Contactform
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


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
    return render(request, 'product.html')
