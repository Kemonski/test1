from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Pet)
admin.site.register(LostAndFound)
admin.site.register(AdoptionApplication)
admin.site.register(PetHealthRecord)
