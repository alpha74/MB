from django.apps import AppConfig

class UsersConfig(AppConfig):
	name = 'users'
	
	# Used for sending signals: This functionality is used for creating new Profile when new User is created.
	# See signals.py
	def ready( self ):
		import users.signals