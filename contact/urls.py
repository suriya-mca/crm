from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.contact_list, name='contact_list'),
]