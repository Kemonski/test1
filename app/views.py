from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy

class homepage(TemplateView):
    template_name = 'pages/home.html'

class aboutpage(ListView):
    model = Pet
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

class lostfound(ListView):
    model = LostAndFound
    template_name = 'pages/lost_and_found.html'
    context_object_name = 'lost'

class LostAndFoundDetailView(DetailView):
    model = LostAndFound
    template_name = 'pages/lostdetail.html'  
    context_object_name = 'lost'

class LostAndFoundCreateView(CreateView):
    model = LostAndFound
    fields = ['title', 'description', 'status']
    template_name = 'pages/lostcreate.html'  

class LostAndFoundUpdateView(UpdateView):
    model = LostAndFound
    fields = ['title', 'description', 'status']
    template_name = 'pages/lostupdate.html'

class LostAndFoundDeleteView(DeleteView):
    model = LostAndFound
    template_name = 'pages/lostdelete.html'
    success_url = reverse_lazy('found')

class appli(ListView):
    model = AdoptionApplication
    template_name = 'pages/adopappli.html'
    context_object_name = 'app'

class createappli(CreateView):
    model = AdoptionApplication
    fields = ['pet', 'applicant', 'status',]
    template_name = 'pages/createappli.html'

class health(ListView):
    model = PetHealthRecord
    template_name = 'pages/health.html'
    context_object_name = 'health'

class healthcr(CreateView):
    model = PetHealthRecord
    fields = ['pet', 'checkup_date', 'notes',]
    template_name = 'pages/healthcereate.html'

class twolinks(TemplateView):
    template_name = 'pages/about_pets.html'

def lostnfound(request):
    lost_items = LostAndFound.objects.all()  
    return render(request, 'lost_and_found.html', {'lost_items': lost_items}) 

def twolinkss(request):
    some_pk_value = 1  
    return render(request, "pages/about_pets.html", {"some_pk_value": some_pk_value})
