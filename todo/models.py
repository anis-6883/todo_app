from django.db import models

class TodoList(models.Model):
    todo_text    = models.CharField(max_length=264, verbose_name="Todo Text")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo_text[0:20]

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = 'TodoLists'

