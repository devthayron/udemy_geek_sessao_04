from django import forms

class Contactform(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)    #max_length ou min_length (maximo de caractere e o minimo)
    email = forms.EmailField(label='E-mail',max_length=100)
    assunto = forms.CharField(label='Assunto',max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())   #caixa de texto com varias linhas