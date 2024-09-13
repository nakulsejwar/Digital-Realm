from django.urls import path, include
from . import views
from .views import CommentCreateView, LikeView, CategoryView, CategoryCreateView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from contact.views import contactus
urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),

    path('', PostListView.as_view(), name="blog-home"),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),
    path('category-new/', CategoryCreateView.as_view(), name="category-new"),
    path('post/<int:pk>/comment', CommentCreateView.as_view(), name="add_comment"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete"),
    path('contactus/', contactus,name='contactus'),
    path('social-auth', include('social_django.urls', namespace='social')),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('category/<str:cats>/', CategoryView, name='category'),

]
