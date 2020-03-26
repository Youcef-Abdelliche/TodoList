from . import views
from .models import TodoList
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name='new_item'),
    path('delete/<int:item_id>/', views.delete_todo),
]
