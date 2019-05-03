from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET', 'POST'])
def create_and_list_todo(request):
    if request.method == 'POST':
        todo = Todo(title=request.data['title'], description=request.data['description'])
        todo.save()
        todo_serializer = TodoSerializer(todo)
        return Response(todo_serializer.data)
    todos = Todo.objects.all()
    todos_serializer = TodoSerializer(todos, many=True)
    return Response(todos_serializer.data)