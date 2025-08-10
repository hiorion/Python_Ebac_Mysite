from django.urls import path
from .views import PostView

urlpatterns = [
    path('post/', PostView.as_view(), name='nome'),  # 'nome' se conecta ao reverse() do teste
]
