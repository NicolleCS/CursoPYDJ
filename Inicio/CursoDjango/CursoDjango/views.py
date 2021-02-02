from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse("O ano enviado foi " + str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Roberta', 'idade': 22},
        {'nome': 'Silvia', 'idade': 27}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    if(result['idade'] > 0):
        return HttpResponse("A "+str(result['nome'])+' tem '+str(result['idade'])+' anos.')
    else:
        return HttpResponse('A pessoa não foi encontrada!')

def fname2(request, nome):
    banco = lerDoBanco(nome)
    nome = banco['nome']
    idade = banco['idade']
    return render(request, 'pessoa.html', {'v_idade': idade}, {'v_nome': nome})