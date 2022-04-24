from django.urls import path
from contact.views import *

app_name ='contact'


urlpatterns = [
    path('', ContactView.as_view(), name='contact-page'),
    path('create-port', create_contact_view, name="create_port"),
    path('update-port/<int:id>/', update_contact_view, name="update_port"),
    path('update-port/<int:id>/', delete_contact_view, name="delete_port"),
]
