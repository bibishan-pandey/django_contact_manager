from django.shortcuts import render, redirect
from .models import Contact


def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'contacts/home.html', context)


def detail(request, id):
    return render(request, 'contacts/detail.html', {})


def search(request):
    return render(request, 'contacts/search.html', {})


def form(request):
    return render(request, 'contacts/form.html', {})


def delete(request, id):
    contact = Contact.objects.get(pk=id)
    contact.delete()
    return redirect('home')
