from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage.as_view(), name='home'),
    path('pets/', aboutpage.as_view(), name='about'),
    path('crud/', petcrud.as_view(), name='crud'),
    path('crud/<int:pk>', viewnewpet.as_view(), name = 'crud_detail'),
    path('crud/new', createpetcrud.as_view(), name = 'crud_new'),
    path('crud/<int:pk>/edit', updatepetcrud.as_view(), name = 'crud_update'),
    path('crud/<int:pk>/delete', deletepetcrud.as_view(), name = 'crud_delete'),
    path('laf/', lostfound.as_view(), name='found'),
    path('lost-and-found/<int:pk>/', LostAndFoundDetailView.as_view(), name='lost_and_found_detail'),
    path('lost-and-found/new/', LostAndFoundCreateView.as_view(), name='lost_and_found_create'),
    path('lost-and-found/<int:pk>/edit', LostAndFoundUpdateView.as_view(), name='lost_and_found_update'),
    path('lost-and-found/<int:pk>/delete', LostAndFoundDeleteView.as_view(), name = 'lost_and_found_delete'),
    path('application/', appli.as_view(), name='applic'),
    path('appli/new/', createappli.as_view(), name='applicreate'),
    path('health/', health.as_view(), name='healthy'),
    path('health/new/', healthcr.as_view(), name='healthcr'),
    path('two/', twolinks.as_view(), name='links'),
]
