from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .forms import PostForm


# Create your views here.
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post


class CreatePostView(CreateView):
    redirect_field_name = "basicapp/post_form.html"
    form_class = PostForm
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "text"]
    template_name_suffix = "_update_form"
