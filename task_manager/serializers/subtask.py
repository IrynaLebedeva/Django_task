from rest_framework import serializers

from task_manager.models import SubTask


class SubTaskCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SubTask
        fields = ('title', 'description','task', 'status', 'deadline', 'created_at',)

class SubTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = SubTask
        fields = ("id", "title", "description", "status", "deadline", "created_at", "owner")# можно убрать "description", "created_at"

