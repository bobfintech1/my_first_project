from django.urls import path
from post.views import *

app_name ='post'


urlpatterns = [
    path('', PostView.as_view(), name='post-blog'),
    path('create-port', create_post_view, name="create_port"),
    path('update-port/<int:id>/', update_post_view, name="update_port"),
    path('update-port/<int:id>/', delete_post_view, name="delete_port"),
]
