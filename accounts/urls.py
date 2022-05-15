from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', signup, name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')
]