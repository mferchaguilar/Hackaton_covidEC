from django.urls import path
from aislarteweb import views

urlpatterns = [
    path('', views.aislarteweb, name='aislarteweb'),
]
