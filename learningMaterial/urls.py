from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject, name='subject'),
    path('subjects/<str:subjectStr>/', views.subject, name='subjectPlus'),
    path('upload/', views.upload, name='upload'),
    path('new/', views.newSubject, name='newSubject'),
    path('notes/<str:noteStr>/', views.note, name='note'),
]

