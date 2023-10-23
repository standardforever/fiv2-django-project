from django.urls import path
from .views import Signup, Login, Logout, HomePage, AboutPage, room


urlpatterns = [
    path('register/', Signup, name='signup'),
    path('login/', Login, name='login'),
    path('logout', Logout, name='logout'),
    path('', HomePage, name='home'),
    path('about/', AboutPage, name='about'),
    path('room/', room, name='order')
]