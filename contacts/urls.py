from django.urls import path
from .views import home, detail, search, form

urlpatterns = [
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('detail/<int:id>', detail, name='detail'),
    path('search/', search, name='search')
]
