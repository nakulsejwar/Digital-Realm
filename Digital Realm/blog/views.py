from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category , Comment
from .forms import BlogForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
       post.likes.add(request.user)
       liked = True
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})

def CategoryView(request, cats):
     category_posts = Post.objects.filter(category=cats.replace('-', ' '))
     return render(request, 'blog/categori.html', {'cats':cats.title(), 'category_posts':category_posts})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context["liked"] = liked
        return context
 
 


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = BlogForm
    template_name = 'blog/post_form.html'
    #fields = ['title', 'content', 'header_image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url='/'  



class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    #form_class = BlogForm
    
    template_name = 'blog/category_form.html'
    fields = '__all__'
    success_url='http://127.0.0.1:8000/post-new/' 
    

    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = BlogForm
    template_name = 'blog/post_form.html'
    #fields = ['title', 'content', 'header_image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
