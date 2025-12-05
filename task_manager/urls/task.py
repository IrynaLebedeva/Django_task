from django.urls import path, re_path

from task_manager.views.task import (create_task, get_tasks,
get_task_detail, get_tasks_statistics)
from task_manager.views.task import TaskListDayAPIView

urlpatterns = [
    path('tasks_c/', create_task),
    path('tasks_g/', get_tasks),
    path('tasks/<int:pk>/', get_task_detail),
    path('tasks_stats/', get_tasks_statistics),
    path('day/', TaskListDayAPIView.as_view(), name='weekday'),
    path('', TaskListDayAPIView.as_view()),
]