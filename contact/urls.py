from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.contact_view, name="list"),

]