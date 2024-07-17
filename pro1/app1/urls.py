from django.urls import path
from .views import *

urlpatterns = [
    path('', create_view, name='create'),
    path('/show', show_view, name='show_url'),
    path('update/<int:pk>/', update_view, name='update'),
    path('delete/<int:pk>/', delete_view, name='delete')
]
