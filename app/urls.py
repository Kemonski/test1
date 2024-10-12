from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage.as_view(), name='home'),
    path('about/', aboutpage.as_view(), name='about'),
]
