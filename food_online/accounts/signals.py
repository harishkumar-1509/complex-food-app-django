from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender,instance,created,**kwargs):
    # created -> this will be true if the object was created and false otherwise
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            # When the user profile profile is updated
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print("User is updated")
        except:
            # create a new profile if not exists
            UserProfile.objects.create(user=instance)

# The below is a non decorator way of implementation
# post_save.connect(post_save_create_profile_receiver, sender=User)