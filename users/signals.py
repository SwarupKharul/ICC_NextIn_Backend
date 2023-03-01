import random
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("created profile")
    if created:
        print("test")
        # Generate random rarity
        rarity = random.randint(1, 100)
        print("rarity", rarity)
        Profile.objects.create(user=instance, rarity=rarity)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
