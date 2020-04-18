from django.urls import path
from multilevel_webpage import views

urlpatterns = [
    path('', views.multilevel_webpage, name='multilevel_webpage'),
]
