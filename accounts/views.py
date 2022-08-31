from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(ListView):
    template_name = "articles/list.html"
    model = Article


class ArticleDetailView(DetailView):
    template_name = "articles/detail.html"
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "articles/new.html"
    model = Article
    fields = ["title", "subtitle", "body", "author"]

def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    


class ArticlesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "articles/edit.html"
    model = Article
    fields = ["title", "subtitle", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticlesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "articles/delete.html"
    model = article
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



