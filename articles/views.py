from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.urls import reverse_lazy
from .models import Articles


class ArticleListView(ListView):
    template_name = "Articles/list.html"
    model = Article


class PostDetailView(DetailView):
    template_name = "Articles/detail.html"
    model = Article


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "Articles/new.html"
    model = Article
    fields = ["title", "subtitle", "body", "author"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    


class ArticleUpdateView(
    LoginRequiredMixin, 
    UserPassesTestMixin, 
    UpdateView
):
    template_name = "Articles/edit.html"
    model = Article
    fields = ["title", "subtitle", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(
    LoginRequiredMixin, 
    UserPassesTestMixin, 
    DeleteView
):
    template_name = "Articles/delete.html"
    model = Article
    success_url = reverse_lazy("Article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



