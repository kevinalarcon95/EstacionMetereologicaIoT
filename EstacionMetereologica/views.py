from django.http import HttpResponse
from django.shortcuts import render


def home_Page(request):
    return render(request, 'template.html')

def quienes_Somos(request):
    return render(request, 'quienes_somos.html')

def proyecto(request):
    return render(request, 'proyecto.html')

def producto(request):
    return render(request, 'producto.html')

def contacto(request):
    return render(request, 'contacto.html')

