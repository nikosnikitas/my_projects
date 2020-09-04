#---	This is a web application that checks if the day is Sunday
#---	Author: Nikos-Nikitas, GitHub: nikosnikitas
#---	- - - >	Made with Python, datetime and Django, HTML, CSS < - - - 
#--- 						- - - > Server Side < - - - 

from django.shortcuts import render
from django.http import HttpResponse #to respond to http requests
from datetime import date #getting the date

# Create your views here.

# Checks if today is Sunday after getting the date and weekday
# Returns the html template with the variables
def index(request):
	
	day_is_Sunday = False
	
	now = date.today()
	
	if now.weekday() == 6: # weekdays are in numbers from 0 to 6.
		day_is_Sunday = True
	
	return render(request, "isitapp/index.html",{'day_is_Sunday':day_is_Sunday,'now':now})