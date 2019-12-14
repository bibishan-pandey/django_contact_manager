from django.urls import path
from .views import home, detail, search, form, delete

urlpatterns = [
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('detail/<int:id>', detail, name='detail'),
    path('delete/<int:id>', delete, name='delete'),
    path('search/', search, name='search')
]
