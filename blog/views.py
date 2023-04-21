from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (
 ListView, DetailView, CreateView, UpdateView, DeleteView )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Function views

# index page
# don't need this now. replaced by PostListView.
def home( request ):
	posts = Post.objects.all()

	context = 	{
					'posts' : posts,
				}
	return render( request, 'blog/home.html', context )
	
# about page	
def about( request ):
	return render( request, 'blog/about.html', { 'title' : 'About' } )
	
	
# Class Views

# All posts
class PostListView( ListView ):
	
	# model tells what model to query to generate the list
	model = Post
	
	# Default convention : <app>/<model>_<viewtype>.html ( EG: blog/post_view.html ). Here, we are not using default.
	template_name = 'blog/home.html'
	
	# Naming it as in home(), as it used in template home.html
	context_object_name = 'posts'
	
	# inverse: 'date_posted'
	ordering = [ '-date_posted' ]
	
	# pagination
	paginate_by = 3


# All posts of a user
class UserPostListView( ListView ):
	
	# model tells what model to query to generate the list
	model = Post
	
	# Default convention : <app>/<model>_<viewtype>.html ( EG: blog/post_view.html ). Here, we are not using default.
	template_name = 'blog/user_posts.html'
	
	# Naming it as in home(), as it used in template home.html
	context_object_name = 'posts'
		
	# pagination
	paginate_by = 3
	
	# Filter user posts by overrinding
	def get_queryset( self ):
		# If user exists
		user = get_object_or_404( User, username=self.kwargs.get( 'username' ) )
		return Post.objects.filter( author = user ).order_by( '-date_posted' )

	
# Individual Post	
class PostDetailView( DetailView ):
	
	# model tells what model to query to generate the list
	model = Post
	
	# It will looking for blog/post_detail.html
	context_object_name = 'post'
	
	
# Post create view
# LoginRequiredMixin makes login necessary to create new post. It should be written to far left.
class PostCreateView( LoginRequiredMixin, CreateView ):
	model = Post
	
	fields = [ 'title', 'content' ]
	
	# Override form_valid() to add current logged in user
	def form_valid( self, form ):
		form.instance.author = self.request.user
		return super().form_valid( form )


# Update post
# LoginRequiredMixin makes login necessary to create new post. It should be written to far left.
# UserPassesTestMixin ensures that author can only edit the post.
class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
	model = Post
	
	fields = [ 'title', 'content' ]
	
	# Override form_valid() to add current logged in user
	def form_valid( self, form ):
		form.instance.author = self.request.user
		return super().form_valid( form )
		
	
	# This function is called to validate the author as current user
	def test_func( self ):
		post = self.get_object() # Get current post
		
		# User check
		if( self.request.user == post.author ):
			return True
		else:
			return False 
			
			
# Delete View			
# Post is not deleted on failure
class PostDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView ):
	
	# model tells what model to query to generate the list
	model = Post
	success_url = '/'
	
	# It will looking for blog/post_detail.html
	context_object_name = 'post'
	
	# This function is called to validate the author as current user
	def test_func( self ):
		post = self.get_object() # Get current post
		
		# User check
		if( self.request.user == post.author ):
			return True
		else:
			return False 
	
	