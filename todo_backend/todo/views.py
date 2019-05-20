from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import controller
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET', 'POST'])
def create_and_list_todo(request):

    if request.method == 'POST':
            is_success, response = controller.create_todo(request.data)
            if is_success:
                return Response(response['todo'], status=response['status'])
            else:
                return Response(response['error_message'], status=response['status'])
    
    else:
        response = controller.get_all_todos()
        return Response(response['todos'], status=response['status'])


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_todo(request, todo_id):

    is_success, response = controller.get_todo_by_id(todo_id)
    if is_success:
        if request.method == 'GET':
            return Response(response['todo'], status=response['status'])

        elif request.method == 'PUT':           
            is_success, response = controller.update_todo(todo_id, request.data)
            if is_success:
                return Response(response['todo'], status=response['status'])
                
            else:
                return Response(response['error_message'], status=response['status'])

        elif request.method == 'DELETE':
            is_success, response = controller.delete_todo_by_id(todo_id)
            if is_success:
                return Response(response['message'], status=response['status'])

            else:
                return Response(response['error_message'], status=response['status'])

    else:
        return Response(response['error_message'], status=response['status'])


@api_view(['PUT'])
def finish_todo(request, todo_id):
    is_success, response = controller.finish_todo(todo_id)
    if is_success:
        return Response(response['message'], status=response['status'])
    else:
        return Response(response['error_message'], status=response['status'])