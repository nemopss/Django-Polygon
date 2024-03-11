from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import CreateView #, DataMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


def index(request): #HttpRequest
    return render(request, 'temp/index.html')

def learn(request): #HttpRequest
    return render(request, 'temp/learn.html')

def registry(request): #HttpRequest
    return render(request, 'temp/registry.html')

def auth(request): #HttpRequest
    return render(request, 'temp/auth.html')

class RegisterUser(CreateView): #DataMixin,
    form_class = UserCreationForm
    template_name = 'temp/registry.html'
    success_url = reverse_lazy('auth')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))