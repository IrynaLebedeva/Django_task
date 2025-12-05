"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from task_manager.views.task import (create_task, get_tasks,
# get_task_detail, get_tasks_statistics)
# from task_manager.views.subtask import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("routers")),
    # path('api/v1/tasks_c/', create_task),
    # path('api/v1/tasks_g/', get_tasks),
    # path('api/v1/tasks/<int:pk>/', get_task_detail),
    # path('api/v1/tasks_stats/', get_tasks_statistics),
    # path('api/v1/subtasks_c/', SubTaskListCreateView.as_view()),
    # path('api/v1/subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
]
