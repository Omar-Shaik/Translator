from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='translate-home'),
    path('signup/', views.sign_up, name='translate-signup'),
    path('messages/', views.view_messages, name='translate-messages'),
]
