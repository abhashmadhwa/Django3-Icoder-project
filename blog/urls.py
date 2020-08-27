from . import views
from django.urls import path, include

urlpatterns = [
    path('postComment',views.postComment,name="postComment"),
    path('',views.blogHome,name='bloghome'),
    path('<str:slug>',views.blogPost,name='blogpost'),
]
