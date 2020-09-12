from django.urls import path
from . import views
app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name="home"),
    path('todo_edit/<int:pk>', views.todo_edit, name="todo_edit"),
    path('todo_delete/<int:pk>', views.todo_delete, name="todo_delete")
]