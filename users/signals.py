from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# post_save signal is fired after an object is saved
# User is the signal sender
# receiver is receiver of signal

# Create ready apps.py -> ready()
# We want a new Profile to be made when new User is created.
# Here, post_save is a signal
# This function is a receiver
@receiver( post_save, sender = User )
def create_profile( sender, instance, created, **kwargs):
	if( created ):
		Profile.objects.create( user = instance )
		

# Saves profile		
@receiver( post_save, sender = User )
def save_profile( sender, instance, **kwargs):
	instance.profile.save()