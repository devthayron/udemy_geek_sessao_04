from django.shortcuts import render
from .forms import Contactform
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def contact(request):
    form = Contactform(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():         #retorna TRUE se não tiver erro
            nome = form.cleaned_data['nome']        #cleaned_data['nome'] onde o nome é o nome da variavel que está definido em core.forms
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print(f'''Mensagem enviada!
            nome: {nome}
            email: {email}
            assunto: {assunto}
            mensagem: {mensagem}
            ''')
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
