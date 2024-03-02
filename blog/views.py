from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , TemplateView , DeleteView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import Post
from django.urls import reverse_lazy

class HomeBlog(ListView):
    model = Post
    template_name = 'home.html'
class NewPost(CreateView):
    model = Post
    template_name = 'postnew.html'
    fields = ['title' , 'author' , 'body']
class DetailBlog(DeleteView):
    model = Post
    template_name = 'detail_view.html'
class UpdateBlogview(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title' , 'body']
class DeleteBlogview(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("home")