from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('',views.home,name='home'),
]