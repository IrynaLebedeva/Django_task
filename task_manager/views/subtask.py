from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from paginators import SubTasksPagination
from task_manager.models import SubTask
from task_manager.serializers.subtask import SubTaskCreateSerializer, SubTaskSerializer

class SubTaskListCreateView(APIView):

    def get(self, request: Request):
        queryset = SubTask.objects.all().order_by('-id', 'title')  # пагинация на моей базе работает корректно только в этом случае,т.к. время создания в 1 день

        task_name = self.request.query_params.get('task_name', None)
        status = self.request.query_params.get('status', None)

        if task_name:
            queryset = queryset.filter(task__title__icontains=task_name)
        if status:
            queryset = queryset.filter(status__iexact=status)

        paginator = SubTasksPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = SubTaskSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)


    def post(self, request: Request):
        raw_data = request.data
        serializer = SubTaskCreateSerializer(data=raw_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskDetailUpdateDeleteView(APIView):
    def get_object(self, pk: int):
        try:
            subtask = SubTask.objects.get(id=pk)
            return subtask
        except SubTask.DoesNotExist:
            return Response({"error": "Subtask not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, pk: int):
        try:
            subtask = SubTask.objects.get(id=pk)
        except SubTask.DoesNotExist:
            return Response({"error": "Subtask not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubTaskCreateSerializer(subtask)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request: Request, pk: int):
        try:
            subtask = SubTask.objects.get(id=pk)
        except SubTask.DoesNotExist:
            return Response({"error": "Subtask not found"}, status=status.HTTP_404_NOT_FOUND)

        new_subtask = SubTaskCreateSerializer(instance=subtask, data=request.data)  # что обновить и чем обновить
        if not new_subtask.is_valid():
            return Response(data=new_subtask.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            new_subtask.save()
            return Response(data=new_subtask.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int):
        try:
            subtask = SubTask.objects.get(id=pk)
            subtask.delete()
            return Response(data={}, status=status.HTTP_204_NO_CONTENT)
        except SubTask.DoesNotExist:
            return Response({"error": "Subtask not found"}, status=status.HTTP_404_NOT_FOUND)














