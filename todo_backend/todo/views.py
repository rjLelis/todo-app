from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import controller


@api_view(['GET', 'POST'])
def create_and_list_todo(request):

    if request.method == 'POST':
        response = controller.create_todo(request.data)
        return Response(response['data'], status=response['status'])

    else:
        response = controller.get_all_todos()
        return Response(data=response['data'], status=response['status'])


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_todo(request, todo_id):

    response = controller.get_todo_by_id(todo_id)
    if response['status'] == 200:
        if request.method == 'GET':
            return Response(data=response['data'], status=response['status'])

        elif request.method == 'PUT':           
            response = controller.update_todo(todo_id, request.data)
            return Response(data=response['data'], status=response['status'])
                
        elif request.method == 'DELETE':
            response = controller.delete_todo_by_id(todo_id)
            return Response(data=response['data'], status=response['status'])

    else:
        return Response(data=response['data'], status=response['status'])


@api_view(['PUT'])
def finish_todo(request, todo_id):
    response = controller.finish_todo(todo_id)
    return Response(data=response['data'], status=response['status'])