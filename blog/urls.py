from django.urls import path
from . import views
from .models import Post

urlpatterns = [
    path('',views.main,name='main'),
    path('post/<int:pk>',views.home,name='home'),
    path('post/<int:pk>',views.upload,name='upload'),
    path('post/<int:pk>',views.feedback,name='feedback'),
]