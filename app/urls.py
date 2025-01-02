from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage.as_view(), name='home'),
    path('about/', aboutpage.as_view(), name='about'),
    path('crud/', petcrud.as_view(), name='crud'),
    path('crud/<int:pk>', viewnewpet.as_view(), name = 'crud_detail'),
    path('crud/new', createpetcrud.as_view(), name = 'crud_new'),
    path('crud/<int:pk>/edit', updatepetcrud.as_view(), name = 'crud_update'),
    path('crud/<int:pk>/delete', deletepetcrud.as_view(), name = 'crud_delete'),
]
