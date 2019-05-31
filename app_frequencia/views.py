# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from .models import Frequencia
from django.shortcuts import render

class HomePageView(ListView):
    model = Frequencia
    template_name = 'app_frequencia/home.html'

def frequencia(request): 
    frequencias = Frequencia.objects.all()
    user = request.user
    return render(request, 'app_frequencia/frequencia.html', {'frequencia': frequencias, 'user': user})
    
