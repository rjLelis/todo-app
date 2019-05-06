from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('todo/', views.create_and_list_todo, name='create-or-list'),
    path('todo/<int:todo_id>', views.get_delete_update_todo, name='get-delete-update'),
    path('todo/<int:todo_id>/finish', views.finish_todo, name='finish-todo')
]