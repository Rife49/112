from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
# Class-bases views
# Pascal Notation - HelloWorld - Uppercase for the first words only for classes

class HomePageView(TemplateView): # OOP - Object Oriented Programming (Inheritance)
    template_name = "home.html" # Attribute
    
    def get_context_data(self, **kwargs): # **kwargs --> keyword arguments/ single variables -> collection
        context = super().get_context_data(**kwargs)
        context["name"] = "Rife"
        context["address"] = "123 Main St"
        context["email"] = "Rife28@sdgku.com"
        return context
    
class AboutPageView(TemplateView):
    template_name = "about.html"


# Function-bases views
def contact_me(request):
    # return HttpResponse("Hello World from a Function Based View")
    contact_info = {
        "name": "Rife",
        "address": "123 Main St",
        "email": "Rife28@sdgku.com"
    }
    
    
    return render(request, "contact.html", contact_info)