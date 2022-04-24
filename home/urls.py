from django.urls import path
from home.views import *

app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home_main'),
    path('create-port', create_home_view, name="create_port"),
    path('update-port/<int:id>/', update_home_view, name="update_port"),
    path('update-port/<int:id>/', delete_home_view, name="delete_port"),
]