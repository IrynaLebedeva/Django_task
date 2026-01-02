# from django.db.models import Count, Q
# from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.utils import timezone
# from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from paginators import TasksPagination

from task_manager.models import Task
from task_manager.permissions import IsOwner
from task_manager.serializers.task import TaskSerializer, TaskDetailSerializer, TaskCreateSerializer

"""
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['GET'])
def get_tasks_statistics(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    tasks_status = tasks.values('status').annotate(total=Count('id'))
    tasks_done = tasks.filter(Q(status="done") & Q(deadline__lt=timezone.now())).count()

    return Response({"total_tasks": total_tasks, "tasks_status": tasks_status, "tasks_done": tasks_done})

class TaskListDayAPIView(APIView):
    # WEEKDAYS = {
    #     "sunday": 1,
    #     "monday": 2,
    #     "tuesday": 3,
    #     "wednesday": 4,
    #     "thursday": 5,
    #     "friday": 6,
    #     "saturday": 7
    # }
    #
    # def get(self, request):
    #
    #     day = request.query_params.get("weekday")
    #
    #     if not day:
    #         tasks = Task.objects.all()
    #         serializer = TaskSerializer(tasks, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #     day_ = day.lower()
    #
    #     if day not in self.WEEKDAYS:
    #         return Response({"error": "Invalid weekday.Pls write 'monday','friday'"},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    #     day_index = self.WEEKDAYS[day]
    #
    #     tasks = Task.objects.filter(deadline__weekday=day_index)
    #     serializer = TaskSerializer(tasks, many=True)
    #
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    WEEKDAYS = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7,
        "понедельник": 0,
        "вторник": 1,
        "среда": 2,
        "четверг": 3,
        "пятница": 4,
        "суббота": 5,
        "воскресенье": 6,
    }

    def get(self, request):
        weekday_param = request.query_params.get("weekday")

        # Если параметр не передан — выдаем все задачи
        if not weekday_param:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        weekday_param = weekday_param.lower()

        # Проверяем существование дня недели
        if weekday_param not in self.WEEKDAYS:
            return Response(
                {"error": "Invalid weekday. Use names like 'monday' or 'вторник'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        weekday_index = self.WEEKDAYS[weekday_param]

        # Получаем задачи с нужным днём недели
        tasks = Task.objects.filter(deadline__week_day=weekday_index + 1)
        # В Django week_day: Sunday=1 ... Saturday=7, поэтому +1

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

"""
class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    pagination_class = TasksPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:    # админ видит все
            return Task.objects.all()
        return Task.objects.filter(owner=user) # пользователь видит только свои задачи

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser]
        return [IsAuthenticated, IsOwner]


class UserTasksView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)
















