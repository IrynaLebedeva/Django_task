from django.urls import path

from task_manager.views.user import UserCreateView


urlpatterns = [
    path('', UserCreateView.as_view()),
]





