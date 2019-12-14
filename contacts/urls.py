from django.urls import path
from .views import home, search, delete, ContactFormView, ContactUpdateView

urlpatterns = [
    path('', home, name='home'),
    path('form/', ContactFormView.as_view(), name='form'),
    path('edit/<int:pk>', ContactUpdateView.as_view(), name='edit'),
    path('delete/<int:id>', delete, name='delete'),
    path('search/', search, name='search')
]
