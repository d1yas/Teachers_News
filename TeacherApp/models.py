from django.db import models

class TeachersModel(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)  
    middle_name = models.CharField(max_length=50, blank=True, null=True)  
    date_of_birth = models.DateField() 
    gender_choices = [
        ("male", "Erkak"),
        ("female", "Ayol"),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="teachers/photos/", blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}"