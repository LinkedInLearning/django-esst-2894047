from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
#from django.contrib.auth.decorators import login_required #sirve para las funciones pero no en clases se pone como decorador
from django.contrib.auth.mixins import LoginRequiredMixin #sirve para las clases y se pone dentro de los parametros de la clase OJO antes de templateView
from django.views.generic import TemplateView #to class-based view

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

#@login_required(login_url='/admin')
#def authorized(request):
#    return render(request,'home/authorized.html',{})