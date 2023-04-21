from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

# User Registration
class UserRegisterForm( UserCreationForm ):
	email = forms.EmailField()		# default: required = true
	
	class Meta:
		model = User
		fields = [ 'username', 'email', 'password1', 'password2' ]


# User update information. This is User model not Profile model
# Allows to update username and email
class UserUpdateForm( forms.ModelForm ):
	email = forms.EmailField()		# default: required = true
	
	class Meta:
		model = User
		fields = [ 'username', 'email' ]
	

# User Profile update
# Allows to update bio and image(fields created by developer)
class ProfileUpdateForm( forms.ModelForm ):
	class Meta:
		model = Profile
		fields = [ 'bio', 'image' ]