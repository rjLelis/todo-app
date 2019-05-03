from django.urls import path
from .views import create_and_list_todo

app_name = 'todo'

urlpatterns = [
    path('todo', create_and_list_todo, name='create-or-list')
]