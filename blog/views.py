from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import reverse

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Post
from blog.models import Comment, ReplyPostComments
from users.forms import CommentForm
from django.views import View
from django.contrib import auth, messages


# generic views (class base view)
class PostListView(View):
    def get(self, request,):
        post = Post.objects.order_by('-date_posted')

        context =  {
            'post': post,
        }
        return render(request, 'blog/home.html', context)

class UserPostListView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        posts = Post.objects.filter(author=user)
        username = user.username.upper()
        
        context = {
            'posts': posts,
            'username': username,
        }
        return render(request, 'blog/user_posts.html', context)

    # model = Post
    # template_name = 'blog/user_posts.html'
    # context_object_name = 'post'
    # paginate_by = 3

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     #user = self.kwargs.get['username']
    #     return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(View):
    def get(self, request, pk, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        all_comments = Comment.objects.filter(post=post).order_by('-created')
        context = {
            'all_comments': all_comments,
            'form': form,
            'post': post,
        }
        return render(request, 'blog/post_detail.html', context)

    def post(self, request, pk, **kwargs):
        post = Post.objects.get(pk=pk)
        author = request.user
        form = CommentForm(request.POST)


        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = author
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', pk=pk)

            #return HttpResponseRedirect(reverse('post_detail', kwargs[pk]))

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):

    return render(request, 'blog/about.html', {'title': 'about'})
