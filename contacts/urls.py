from django.urls import path
from .views import home, search, form, delete

urlpatterns = [
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('edit/<int:id>', form, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
    path('search/', search, name='search')
]
