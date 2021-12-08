"""librogram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from rest_framework import routers
# from librogramapi.models import Reader
from librogramapi.views import register_user, login_user
from librogramapi.views import BookView, ReaderView, TagView, CommentView, UserBookView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'books', BookView, 'book')
router.register(r'readers', ReaderView, 'reader')
router.register(r'tags', TagView, 'post')
router.register(r'comments', CommentView, 'comments')
router.register(r'userbooks', UserBookView, 'userbook')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
] 