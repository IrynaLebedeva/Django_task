from django.urls import path

from task_manager.views.subtask import SubTaskListCreateView,SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('', SubTaskListCreateView.as_view()),
    path('<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
]