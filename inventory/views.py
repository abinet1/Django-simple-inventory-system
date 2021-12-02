from django.views.generic import ListView
from django.views.generic.base import TemplateView
# Create your views here.

class Home(TemplateView ):
    template_name = "Inventory/Home.html"

#
