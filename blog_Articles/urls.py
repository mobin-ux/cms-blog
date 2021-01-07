from django.urls import path
from .views import *



urlpatterns = [
    path('Add-Article/',add_article,name='add_article'),
    path('Edit-Article/',edit_article,name='edit_article'),
    path('Articles/',articles,name='articles'),
    path('Articles-Search/',articles_search,name='articles_search'),
]