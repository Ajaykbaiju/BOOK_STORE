from django.shortcuts import render

# Create your views here.
from .models import Book
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

class BookCreateView(CreateView):
    model=Book
    fields = ['title', 'price']
    template_name='home.html'
    success_url=reverse_lazy('booklist')

class Booklistview(ListView):
    model=Book
    template_name='listview.html'
    context_object_name='books'

class Bookdetailview(DetailView):
    model=Book
    template_name='detailview.html'
    context_object_name='book'

class Bookupdateview(UpdateView):
     model=Book
     fields = ['title', 'price']
     template_name='update.html'
     success_url=reverse_lazy('booklist')

class Bookdelete(DeleteView):
    model=Book
    template_name='delete.html'
    context_object_name='book'
    success_url=reverse_lazy('booklist')


     
    
