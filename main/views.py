from django.shortcuts import render
from django.urls import reverse_lazy


from .models import Customer, Item

# Class Based Views Import
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

# Authentication Imports
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'main/index.html'


class CustomerView(LoginRequiredMixin, ListView):
    template_name = 'main/customers.html'
    model = Customer
    context_object_name = 'customers'


class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'main/customer-detail.html'
    model = Customer
    context_object_name = 'customer'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/create-customer.html'
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customers')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'main/create-customer.html'
    model = Customer
    fields = '__all__'


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'main/customer-delete.html'
    success_url = reverse_lazy('customers')


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'main/item.html'
    fields = '__all__'
    context_object_name = 'items'
    success_url = reverse_lazy('index')
