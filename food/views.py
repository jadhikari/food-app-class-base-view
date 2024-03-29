from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#models loaader
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class IndexClassView(ListView):
    model = Item 
    template_name = 'food/index.html'
    context_object_name = 'item_list'

@method_decorator(login_required, name='dispatch')
class FoodDetail(DetailView):
    model= Item
    template_name='food/detail.html'

@method_decorator(login_required, name='dispatch')
class CreateItem(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')  

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        response = super().form_valid(form)
        # You can perform additional actions after the form is successfully validated and saved here
        return response

@method_decorator(login_required, name='dispatch')
class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')  

    def form_valid(self, form):
        response = super().form_valid(form)
        # You can perform additional actions after the form is successfully validated and saved here
        return response

@method_decorator(login_required, name='dispatch')   
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'food/delete-item.html'
    success_url = reverse_lazy('food:index')  

    def get_object(self, queryset=None):
        # Retrieve the object to be deleted using 'pk' from the URL
        item_pk = self.kwargs['pk']
        return get_object_or_404(Item, pk=item_pk)
