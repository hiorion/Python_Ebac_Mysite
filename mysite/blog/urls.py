from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.post_list, name='home'),  # home listando posts
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
