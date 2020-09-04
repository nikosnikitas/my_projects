#urls to route the users in our app

from django.urls import path #path to reroute the users
from . import views #what the users will see

urlpatterns = [
	
	path("",views.index, name="index")
	
	]