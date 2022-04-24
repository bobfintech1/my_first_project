from django.urls import path
from about.views import *

app_name = 'about'


urlpatterns = [
    path('', AboutView.as_view(), name='about_page'),
    path('create-port', create_about_view, name="create_port"),
    path('update-port/<int:id>/', update_about_view, name="update_port"),
    path('update-port/<int:id>/', delete_about_view, name="delete_port"),
]