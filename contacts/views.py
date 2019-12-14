from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Contact


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'contacts/home.html'
    model = Contact
    context_object_name = 'contacts'

    # querying contact list that is added by logged in user only
    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)


@login_required()
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
            'contacts': search_results.filter(manager=request.user)
        }
        return render(request, 'contacts/search.html', context)
    return redirect('home')


@login_required()
def delete(request, id):
    contact = Contact.objects.get(pk=id)
    if contact in Contact.objects.filter(manager=request.user):
        contact.delete()
    messages.success(request, 'Contact have been successfully deleted!')
    return redirect('home')


class ContactFormView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'contacts/create.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'Contact have been successfully created!')
        return redirect('home')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'contacts/edit.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'Contact have been successfully updated!')
        return redirect('home')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'Account have been successfully registered!')
        return redirect('home')
