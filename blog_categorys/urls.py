from django.urls import path
from .views import *

app_name = 'Categorys'

urlpatterns = [
    path('Add-Categorys/',add_categorys,name='add_categorys')
]