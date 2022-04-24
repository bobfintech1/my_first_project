from django.urls import path
from blog.views import *

app_name ='blog'


urlpatterns = [
    path('', BlogView.as_view(), name='blog-page'),
    path('create-port', create_blog_view, name="create_port"),
    path('update-port/<int:id>/', update_blog_view, name="update_port"),
    path('update-port/<int:id>/', delete_blog_view, name="delete_port"),
]
