from django.urls import path
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('search', views.search, name='search')
]
