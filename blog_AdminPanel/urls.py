from django.urls import path,include
from .views import *

app_name = 'AdminPanel'
urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/',include('blog_Articles.urls')),
]