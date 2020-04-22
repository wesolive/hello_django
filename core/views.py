from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('hello {} de {} anos'.format(nome, idade))
def soma(request, n1, n2):
    soma = n1 + n2
    return HttpResponse('<h1> O valor da Soma é: {}</h1>'.format(soma))
def sub(request, n1, n2):
    subtracao = n1 - n2
    return HttpResponse('<h1> O valor da Subtração é : {}</h1>'.format(subtracao))
def mult(request, n1, n2):
    multiplicacao = n1 * n2
    return HttpResponse('<h1> O valor da Multiplicação é : {}</h1>'.format(multiplicacao))
def div(request, n1, n2):
    divisao = n1 / n2
    return HttpResponse('<h1> O valor da Divisão é : {}</h1>'.format(divisao))