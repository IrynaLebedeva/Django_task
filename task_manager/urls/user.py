from django.urls import path

from task_manager.views.user import UserCreateView, LogoutView, RefreshTokenView, LoginView


urlpatterns = [
    path('register/', UserCreateView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('refresh/', RefreshTokenView.as_view()),
    path('login/', LoginView.as_view())
]





