from django.db.models import Count, Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from task_manager.models import Task
from task_manager.serializers.task import TaskSerializer

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