from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from task_manager.views.category import CategoryViewSet
# from task_manager.views.subtask import SubTaskListCreateView,SubTaskDetailUpdateDeleteView
# from task_manager.views.task import TaskListDayAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = DefaultRouter()
router.register(r'category', CategoryViewSet)
# router.register('subtask', SubTaskViewSet, basename='subtask')
# router.register('task', TasksViewSet, basename='task')


urlpatterns = [
    # path('category/', include('task_manager.urls.category')),
    path('subtask/', include('task_manager.urls.subtask')),
    path('task/', include('task_manager.urls.task')),
    path('user/', include('task_manager.urls.user')),
    path('jwt-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls

