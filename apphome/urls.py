from django.urls import path
from .views import index_home, contato, produto

urlpatterns = [
    path('', index_home, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
]







