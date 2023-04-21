from django.db import models

from django.contrib.auth.models import User
from PIL import Image

# Profile extends User
class Profile( models.Model ):
	user = models.OneToOneField( User, on_delete=models.CASCADE )
	
	bio = models.TextField()
	image = models.ImageField( default = "default_profile_pic.jpg", upload_to = "profile_pics" )
	
	def __str__( self ):
		return f"{ self.user.username } Profile"

	# Overriding save method. Runs after model is saved.
	def save( self, *args, **kwargs ):
		
		# Running save() of parent class
		super().save( *args, **kwargs )
		
		# Image resizing using Pillow
		img = Image.open( self.image.path )
		
		if( img.height > 400 or img.width > 400 ):
			output_size = ( 400, 400 )
			img.thumbnail( output_size )
			img.save( self.image.path )