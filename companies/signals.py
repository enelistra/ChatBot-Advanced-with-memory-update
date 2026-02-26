from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Company
from chatapp.faiss_engine import build_index

@receiver(post_save, sender=Company)
def create_vectors(sender, instance, created, **kwargs):

    if created:
        text = instance.txt_file.read().decode("utf8")
        build_index(instance.code, text)
