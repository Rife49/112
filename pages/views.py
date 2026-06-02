from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
# Class-bases views
# Pascal Notation - HelloWorld - Uppercase for the first words only for classes

class HomePageView(TemplateView): # OOP - Object Oriented Programming (Inheritance)
    template_name = "home.html" # Attribute
    
class AboutPageView(TemplateView):
    template_name = "about.html"


# Function-bases views
def contact_me(request):
    # return HttpResponse("Hello World from a Function Based View")
    return render(request, "contact.html")