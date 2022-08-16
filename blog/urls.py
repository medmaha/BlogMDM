from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)

#from django.views import LoginView, LogoutView

page = 'blog'

urlpatterns = [

    path('', PostListView.as_view(), name='blog-home'),
    path('user/<int:pk>/', UserPostListView.as_view(), name='user_posts'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),



    path('about/', views.about, name='blog-about')

]
