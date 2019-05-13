from todo.models import Todo

def get_all_todo():
    return Todo.objects.all()


def get_todo_by_id(todo_id):
    todo = Todos.objects.get(id=todo_id)
    if todo is None:
        raise Todo.DoesNotExist
    else:
        return todo

def create_or_update_todo(todo):
    