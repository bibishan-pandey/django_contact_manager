from django.shortcuts import render


def home(request):
    return render(request, 'contacts/home.html', {})


def detail(request, id):
    return render(request, 'contacts/detail.html', {})


def search(request):
    return render(request, 'contacts/search.html', {})


def form(request):
    return render(request, 'contacts/form.html', {})
