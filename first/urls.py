"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import home_view, registration_view, account_authentication, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view, name='home'),
    path('register', registration_view, name='register'),
    path('', account_authentication, name='login'),
    path('logout', logout_view, name='logout'),

    path('home/', include('home.urls', namespace='home_main')),
    path('about/', include('about.urls', namespace='about_page')),
    path('blog/', include('blog.urls', namespace="blog_page")),
    path('post/', include('post.urls', namespace="post_page")),
    path('contact/', include('contact.urls', namespace="contact_page")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
