from django.urls import path
from .views import search, delete, HomePageView, ContactFormView, ContactUpdateView, SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', ContactFormView.as_view(), name='create'),
    path('edit/<int:pk>/', ContactUpdateView.as_view(), name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('search/', search, name='search'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
