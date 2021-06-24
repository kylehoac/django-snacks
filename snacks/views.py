from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Snacks
from django.urls import reverse_lazy

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

class SnacksCreateView(CreateView):
    template_name = "snacks_create.html"
    model = Snacks
    fields = ["name","purchaser","description"]

class SnacksUpdateView(UpdateView):
    template_name = "snacks_update.html"
    model = Snacks
    fields = ["name","purchaser","description"]
    
class SnacksDeleteView(DeleteView):
    template_name = "snacks_delete.html"
    model = Snacks
    success_url = reverse_lazy("snacks_list")