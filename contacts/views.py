from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Contact


def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'contacts/home.html', context)


def search(request):
    if request.GET:
        search_term = request.GET['search']
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(info__icontains=search_term) |
            Q(phone__icontains=search_term)
        )
        context = {
            'search': search_term,
            'contacts': search_results
        }
        return render(request, 'contacts/search.html', context)
    return redirect('home')


def form(request, id=None):
    return render(request, 'contacts/form.html', {})


def delete(request, id):
    contact = Contact.objects.get(pk=id)
    contact.delete()
    return redirect('home')
