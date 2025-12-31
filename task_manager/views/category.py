from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from task_manager.models import Category
from task_manager.serializers import CategoryCreateSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAdminUser()]

    @action(detail=False, methods=['get'])
    def count_tasks(self, request):
        categories = Category.objects.filter(is_deleted=False).annotate(tasks_count=Count('tasks')).order_by('name')
        result = {category.name: category.tasks_count for category in categories}
        return Response(result)