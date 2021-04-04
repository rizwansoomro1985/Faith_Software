from django.urls import path

from . import views
from .views import *

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('', Index.as_view(), name='index'),
    path('customers/', CustomerView.as_view(), name='customers'),
    path('customer-detail/<int:pk>/',
         CustomerDetailView.as_view(), name='customer-detail'),
    path('create-customer/', CustomerCreateView.as_view(), name='create-customer'),
    path('customer-update/<int:pk>/',
         CustomerUpdateView.as_view(), name='customer-update'),
    path('customer-delete/<int:pk>/',
         CustomerDeleteView.as_view(), name='customer-delete'),
    #path('items/', ItemCreateView.as_view(), name='items'),

]
