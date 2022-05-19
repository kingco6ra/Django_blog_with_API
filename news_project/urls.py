"""news_project URL Configuration

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
from rest_framework import routers

from news_app.views import NewsViewSet, CommentsViewSet, UserViewSet, CategoryViewSet

# API
router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'cheloboti', UserViewSet)
router.register(r'categories', CategoryViewSet)
# END API

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Apps
    path('', include('news_app.urls')),
    path('', include('accounts.urls')),
    path('captcha/', include('captcha.urls')),
    # API
    path('api/', include(router.urls)),
    path('api/auth', include('rest_framework.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
