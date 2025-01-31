from django.db import models
from django.conf import settings
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    adoption_status = models.CharField(max_length=20, default='Available')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("crud_detail", kwargs={"pk": self.pk})


class LostAndFound(models.Model):
    title = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("lost_and_found_detail", kwargs={"pk": self.pk})


class AdoptionApplication(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.applicant.username} - {self.pet.name}"
    
    def get_absolute_url(self):
        return reverse("applic", kwargs={"pk": self.pk})


class PetHealthRecord(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    checkup_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"Health Record for {self.pet.name}"
    
    def get_absolute_url(self):
        return reverse("healthy", kwargs={"pk": self.pk})
