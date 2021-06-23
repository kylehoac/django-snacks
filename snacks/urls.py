from django.urls import path
from .views import AboutPageView, HomePageView, FAQPageView, SnacksListView,SnacksDetailView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('faq/', FAQPageView.as_view(), name='faq'),
    path('', SnacksListView.as_view(), name='snacks_list'),
    path('<int:pk>/', SnacksDetailView.as_view(), name='snacks_detail'),
]