from django.urls import path
from pages.views import *

urlpatterns = [
    path("", HomePageView, name="home"),
    path("about/", AboutPageView, name="about"),
]