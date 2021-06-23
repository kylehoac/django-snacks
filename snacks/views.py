from django.views.generic import TemplateView, ListView, DetailView
from .models import Snacks
 
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class FAQPageView(TemplateView):
    template_name = "faq.html"

class SnacksListView(ListView):
    template_name = "snacks_list.html"
    model = Snacks

class SnacksDetailView(DetailView):
    template_name = "snacks_detail.html"
    model = Snacks