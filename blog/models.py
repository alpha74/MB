from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


""" View SQL command

	python manage.py sqlmigrate blog 0001
"""

# Post
class Post( models.Model ):
	title = models.CharField( max_length=100)
	content = models.TextField()

	# Use auto_now for last modified
	# USe auto_now_add for adding date when the object is created. But we cannot update this field later
	# Here, timezone.new is a function which is not called but passed.
	date_posted = models.DateTimeField( default = timezone.now )
	
	# If user is deleted, all posts are deleted of user.
	author = models.ForeignKey( User, on_delete = models.CASCADE )

	# What is to be returned when using Interative Shell
	# On using: Post.objects.all() : title is shown 
	def __str__(self):
		return self.title

	# Called when new post is created. PostCreateView in views.py
	def get_absolute_url( self ):
		return reverse( 'post-detail', kwargs = { 'pk' : self.pk } )