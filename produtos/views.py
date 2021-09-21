from django.shortcuts import render


def pagina_produtos(request):
    idade = 19
    classificacao = ''

    if idade < 12:
        classificacao = "Criança"
    elif idade >= 12 and idade <= 18:
        classificacao = "Adolescente"
    else:
        classificacao = "Adulto"

    context = {
        'nome' : 'Fabrício Herpich',
        'ultimo_acesso' : '16/09/2021',
        'idade' : 11,
        'classificacao' : classificacao,
        'produtos': [
            {'nome': 'Notebook Acer', 'preco' : '5.750,00'},
            {'nome': 'iPhone', 'preco': '4.000,00'},
            {'nome' : 'Headset', 'preco':'200'},
            {'nome': 'Caneta', 'preco': '10'},
        ]
    }
    return render(request, 'index.html', context)


def celulares(request):
    return render(request, 'celulares.html')

def moveis(request):
    return render(request,'moveis.html')