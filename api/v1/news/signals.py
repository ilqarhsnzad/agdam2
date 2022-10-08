from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from details.models import Light

User = get_user_model()

@receiver(post_save, sender = User)
def create_light(sender, instance, created, **kwargs):
    if created:
        Light.objects.create(light_user = instance)

