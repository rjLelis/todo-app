from django.db import models

class Todo(models.Model):

    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} {self.title}'