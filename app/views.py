from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet
from django.urls import reverse_lazy

class homepage(TemplateView):
    template_name = 'pages/home.html'

class aboutpage(TemplateView):
    template_name = 'pages/about.html'

class petcrud(ListView):
    model = Pet
    template_name = 'pages/crudforpets.html'

class viewnewpet(DetailView):
    model = Pet
    context_object_name = 'viewthepet'
    template_name = 'pages/viewdetail.html'

class createpetcrud(CreateView):
    model = Pet
    fields = ['name', 'species', 'breed', 'age', 'adoption_status']
    template_name = 'pages/crudcreate.html'

class updatepetcrud(UpdateView):
    model = Pet
    fields = ['name', 'species', 'breed', 'age', 'adoption_status']
    template_name = 'pages/crudcreate.html'

class deletepetcrud(DeleteView):
    model = Pet
    template_name = 'pages/cruddelete.html'
    success_url = reverse_lazy('crud')
