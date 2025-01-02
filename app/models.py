from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class AdoptionApplication(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    applicant = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.applicant.username} - {self.pet.name}"


class PetHealthRecord(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    checkup_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"Health Record for {self.pet.name}"
