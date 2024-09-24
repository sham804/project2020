from django.db import models

class ApplicationForm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)
    experience = models.TextField()
    place = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    marketing_module = models.JSONField(default=list)


