from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

# from task_manager.views.category import ...
# from task_manager.views.subtask import SubTaskListCreateView,SubTaskDetailUpdateDeleteView
# from task_manager.views.task import TaskListDayAPIView


router = DefaultRouter()
# router.register('categpory', ...)
# router.register('subtask', SubTaskViewSet, basename='subtask')
# router.register('task', TasksViewSet, basename='task')


urlpatterns = [
    # path('category/', include('task_manager.urls.category')),
    path('subtask/', include('task_manager.urls.subtask')),
    path('task/', include('task_manager.urls.task')),
] + router.urls

