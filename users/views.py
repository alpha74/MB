from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Profile

# Use this to madate login required
@login_required
def profile( request ):

	if( request.method == 'POST' ):
		u_form = UserUpdateForm( request.POST, instance = request.user )
		p_form = ProfileUpdateForm( request.POST, request.FILES, instance = request.user.profile )
		
		# Check if form data is valid
		if( u_form.is_valid() and p_form.is_valid() ):
			username = u_form.cleaned_data.get( "username" )
			u_form.save()
			
			bio = p_form.cleaned_data.get( "bio" )
			p_form.save()
			
			# uses an fstring
			messages.success( request, f"Your account is updated!" )
			
			# redirect user to home page
			return redirect( "profile" )
			
		
	else:
		u_form = UserUpdateForm( instance = request.user )
		p_form = ProfileUpdateForm( instance = request.user.profile )
		
	context =	{
					'u_form' : u_form,
					'p_form' : p_form,
				}
	
	return render( request, 'users/profile.html', context )


# Registration
def register( request ):
		
	if( request.method == 'POST' ):
		form = UserRegisterForm( request.POST )
		
		if( form.is_valid() ):
			username = form.cleaned_data.get( 'username' )
			# Save user
			form.save()
			
			# uses an fstring
			messages.success( request, f"Your account has been created! Login now" )
			
			# redirect user to home page
			return redirect( "login" )
		
		else:
			print( "\n Errors: " + str( form.errors ) )
		
			return render( request, 'users/register.html', { 'form' : form } )


	else:
		form = UserRegisterForm()
		
	return render( request, 'users/register.html', { 'form' : form } )

