from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject, name='subject'),
    path('subjects/<str:subjectStr>/', views.subject, name='subjectPlus'),
    path('upload/', views.upload, name='upload'),
]

