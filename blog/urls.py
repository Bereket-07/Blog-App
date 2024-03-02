from django.urls import path
from .views import HomeBlog , NewPost , DetailBlog , UpdateBlogview , DeleteBlogview
 
urlpatterns = [
    path('post/new/' , NewPost.as_view() , name='post_new'),
    path('post/<int:pk>/edit/' , UpdateBlogview.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/' , DeleteBlogview.as_view(),name='post_delete'),
    path('post/<int:pk>/' , DetailBlog.as_view() , name='post_detail'),
    path('',HomeBlog.as_view(), name='home'),
]