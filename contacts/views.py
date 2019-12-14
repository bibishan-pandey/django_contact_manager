from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
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
            'contacts': search_results
        }
        return render(request, 'contacts/search.html', context)
    return redirect('home')


def delete(request, id):
    contact = Contact.objects.get(pk=id)
    contact.delete()
    return redirect('home')


class ContactFormView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'contacts/form.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        return redirect('home')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'contacts/form.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    success_url = '/'

    # def form_valid(self, form):
    #     instance = form.save()
    #     return redirect('edit', instance.pk)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
