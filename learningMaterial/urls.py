from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject, name='subject')
]