from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)

    txt_file = models.FileField(upload_to="data/txt/")

    api_token = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class GeminiConfig(models.Model):

    api_key = models.CharField(max_length=255)
    model_name = models.CharField(
        max_length=100,
        default="gemini-2.5-flash"
    )

    active = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model_name} (Active: {self.active})"
