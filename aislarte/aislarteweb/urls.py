from django.urls import path
from aislarteweb import views

urlpatterns = [
    path('', views.aislarteweb, name='aislarteweb'),
    path('music/', views.music, name='music'),
]
