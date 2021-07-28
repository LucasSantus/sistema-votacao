from django.shortcuts import render
from django.utils import timezone
from votacao.models import Votacao
from usuarios.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from votacao.models import *

def base(request):
    data = timezone.now()
    context = { 
        'data': data.year
    }
    return context

# Validar se o usuário está cadastrado.
def validate_user(request):
    user = request.GET.get('username', None)
    data = {
        'is_user': Usuario.objects.filter(email__iexact=user).exists(),
    }
    if not data['is_user']:
        data['error_message'] = 'Este e-mail não está cadastrado!'
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_email': Usuario.objects.filter(email__iexact=email).exists(),
    }
    if data['is_email']:
        data['error_message'] = 'Este e-mail já está cadastrado!'
    return JsonResponse(data)

def validate_email_registered(request):
    email = request.GET.get('email', None)
    data = {
        'is_email_registered': Usuario.objects.filter(email__iexact=email).exists(),
    }
    print(data["is_email_registered"])
    if not data['is_email_registered']:
        data['error_message'] = 'Este e-mail não está cadastrado no sistema!'
    return JsonResponse(data)

def validate_group(request):
    print("hihihh")
    group = request.GET.get('sala', None)
    data = {
        'is_group': SalaVotacao.objects.filter(codigo__iexact=group).exists(),
    }
    if not data['is_group']:
        data['error_message'] = 'Este sala não está cadastrado!'
    return JsonResponse(data)

@login_required
def index(request):
    user = request.user
    list_salas = SalaVotacao.objects.filter(usuarios=user)
    if not list_salas:
        messages.info(request,"Não existem salas registrados!")

    if request.GET: 
        pesquisa = request.GET.get("pesquisa", False)
        print(pesquisa)
        try:
            list_salas = SalaVotacao.objects.filter(titulo__icontains=pesquisa, usuarios=user).order_by("-data_registrado")
            if not list_salas:
                list_salas = SalaVotacao.objects.filter(codigo__icontains=pesquisa, usuarios=user).order_by("-data_registrado")
                if not list_salas:
                    messages.error(request, "sala não encontrado.")
        except:
            messages.error(request, "sala não encontrado.")

    context = {
        "salas": list_salas,
    }

    return render(request, "home/index.html", context)

def votacoes(request):
    votacoes = Votacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now())
    
    if not votacoes:
        messages.info(request,"No momento não existem votações disponiveis")

    context = {
        "votacoes": votacoes,
    }
    return render(request, "home/index.html", context)
