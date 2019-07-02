from django.test import TestCase
from rest_framework import status
from . import controller as todo_controller
from .models import Todo

# Create your tests here.
class TodoControllerTestCase(TestCase):

    def setUp(self):
        todo = {'title': 'todo test', 'description': 'this is a test todo item', 'done': False}
        todo_controller.create_todo(todo)

    def test_create_todo_without_title(self):
        todo = {
            'description': 'Todo description to fail',
        }
        new_todo = todo_controller.create_todo(todo)
        self.assertEqual(new_todo['status'], status.HTTP_400_BAD_REQUEST)


    def test_create_todo_with_empty_title(self):
        todo = {
            'title': '',
            'description': 'Test description'
        }

        new_todo = todo_controller.create_todo(todo)
        self.assertEquals(new_todo['status'], status.HTTP_400_BAD_REQUEST)

    
    def test_create_todo(self):
        todo = {
            'title': 'Test todo title'
        }
        new_todo = todo_controller.create_todo(todo)
        self.assertEquals(new_todo['status'], status.HTTP_201_CREATED)


    def test_create_todo_done_equals_true(self):
        todo = {
            'title': 'Test todo title',
            'done': True
        }

        new_todo = todo_controller.create_todo(todo)
        self.assertEqual(new_todo['data']['done'], False)

    
    def test_update_todo(self):
        todo = Todo.objects.get(title='todo test')
        todo_updated = {
            'title': todo.title,
            'description': 'change todo description',
            'done': True 
        }
        response = todo_controller.update_todo(todo.id, todo_updated)
        self.assertEquals(response['status'], status.HTTP_200_OK)