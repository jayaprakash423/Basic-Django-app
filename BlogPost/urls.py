"""BlogPost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from blog.views import (index_view,
	create_Musician_view,
	create_Album_view,
	about_view,
	update_view,
	delete_view,
	contact_view,
	retrive_view,
	login_view,
	register_view,

	)

urlpatterns = [
    path('',index_view,name='blog-index'),
    path('amusic/',create_Musician_view,name='blog-music'),
    path('balbum/',create_Album_view,name='blog-album'),
    path('about/',about_view,name='blog-about'),
    path('update/',update_view,name='blog-update'),
    path('delete/',delete_view,name='blog-delete'),
    path('contact/',contact_view,name='blog-contact'),
    path('retrive/',retrive_view,name='blog-retrive'),
    path('login/',auth_views.LoginView.as_view(template_name='blogs/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='blogs/logout.html'),name='logout'),
    path('register/',register_view,name='blog-register'),
    path('admin/', admin.site.urls),
]
