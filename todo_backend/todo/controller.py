from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status


def get_all_todos():

    todos = Todo.objects.all()
    todos_serialized = TodoSerializer(todos, many=True)
    return {
        'data': todos_serialized.data, 
        'status': status.HTTP_200_OK
    }


def get_todo_by_id(todo_id):

    try:
        todo = Todo.objects.get(id=todo_id)
        todo_serialized = TodoSerializer(todo)
        return {
            'data':todo_serialized.data, 
            'status': status.HTTP_200_OK
        }

    except Todo.DoesNotExist:
        return {
            'data':{
                'message':f'Todo not found with id {todo_id}'
            }, 
            'status': status.HTTP_404_NOT_FOUND
        }


def create_todo(todo):

    if 'title' not in todo:
        return {
            'data': {
                'message':'The todo title must be provided'
            },
            'status': status.HTTP_400_BAD_REQUEST
        }
    else:
        title = todo['title'].strip()
        if not title:
            return {
                'data': {
                    'message': 'The title must not be empty'
                },
                'status': status.HTTP_400_BAD_REQUEST
            }

    description = todo['description'] if 'description' in todo else ''

    new_todo = Todo(title=title, description=description, done=False)
    new_todo.save()
    new_todo_serialized = TodoSerializer(new_todo)

    return {
        'data': new_todo_serialized.data, 
        'status': status.HTTP_201_CREATED
    }


def update_todo(todo_id, new_todo):
    
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.title = new_todo['title'].strip() if 'title' in new_todo else todo.title
        todo.description = new_todo['description'] if 'description' in new_todo else todo.description
        todo.done = new_todo['done'] if 'done' in new_todo else todo.done

        if todo.title.strip():
            todo.save()
            todo_serialized = TodoSerializer(todo)
            return {
                'data': todo_serialized.data,
                'status': status.HTTP_200_OK
            }

        else:
            return {
                'data': {
                    'message': 'The title must not be empty',
                },
                'status': status.HTTP_400_BAD_REQUEST
            }
        
    except Todo.DoesNotExist:
        return {
            'data': {
                'message': f'Todo not found with id {todo_id}',
            },
            'status': status.HTTP_404_NOT_FOUND
        }


def delete_todo_by_id(todo_id):

    try:
        todo = Todo.objects.get(id=todo_id)
        title = todo.title
        todo.delete()
        return {
            'data': {
                'message': f'The todo "{title}" has been deleted'
                }, 
            'status': status.HTTP_204_NO_CONTENT
            }

    except TypeError:
        return {
            'data': {
                'message':'The todo id must be provided'
                }, 
            'status': status.HTTP_400_BAD_REQUEST
            }

    except Todo.DoesNotExist:
        return {
            'data': {
                'message':f'Todo not found with id {todo_id}'
                }, 
            'status': status.HTTP_404_NOT_FOUND
            }
        

def finish_todo(todo_id):
    
    try:
        todo = Todo.objects.get(id=todo_id)
        if todo.done:
            error = {
                'data': {
                    'message':f'The todo "{todo.title}" has already been finished'
                    }, 
                'status': status.HTTP_304_NOT_MODIFIED
                }
            return error

        else:
            todo.done = True
            todo.save()
            return {
                'data':{
                    'message':f'The todo "{todo.title}" has been finished'
                    }, 
                'status': status.HTTP_200_OK
                }

    except TypeError:
        error = {
            'data':{
                'message':'The todo id must be provided'
                },
            'status': status.HTTP_400_BAD_REQUEST
            }
        return error

    except Todo.TodoDoesNotExist:
        error = {
            'data': {
                'message':f'Todo not found with id {todo_id}'
                }, 
            'status': status.HTTP_404_NOT_FOUND
            }
        return error
