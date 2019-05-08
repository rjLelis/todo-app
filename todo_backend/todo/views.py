from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET', 'POST'])
def create_and_list_todo(request):
    if request.method == 'POST':
        title = request.data['title']
        description = request.data['description']
        done = request.data['done']
        todo = Todo(title=title, description=description, done=done)
        todo.save()
        todo_serializer = TodoSerializer(todo)
        return Response(todo_serializer.data, status=status.HTTP_201_CREATED)
    todos = Todo.objects.all()
    todos_serializer = TodoSerializer(todos, many=True)
    return Response(todos_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return Response({'message': f'Todo not found with id {todo_id}'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        todo_serializer = TodoSerializer(todo)
        return Response(todo_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        message = f'The todo "{todo.title}" has been deleted'
        todo.delete()
        return Response(data={'message': message}, status=status.HTTP_204_NO_CONTENT)
    else:
        try:
            todo.title = request.data['title']
            todo.description = request.data['description']
            todo.done = request.data['done']
            todo.save()
            todo_serializer = TodoSerializer(todo)
            return Response(todo_serializer.data, status=status.HTTP_200_OK)
        except KeyError:
            return Response({'message': 'All parameters of the todo must be sent in order to update the todo'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def finish_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.done = True
        todo.save()
        todo_serializer = TodoSerializer(todo)
        return Response(data={'todo': todo_serializer.data, 'message': f'The todo "{todo.title}" has been finished'}, status=status.HTTP_200_OK)
    except Todo.DoesNotExist:
        return Response({'message': f'Todo not found with id {todo_id}'}, status=status.HTTP_404_NOT_FOUND)
