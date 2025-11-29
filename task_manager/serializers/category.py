from rest_framework import serializers
from datetime import timezone

from task_manager.models import Category

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')


    def validate(self, data):
        if Category.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError("Category with this name already exists")
        return data


    def create(self, validated_data):
        new_name = validated_data.get('name')
        if Category.objects.filter(name=new_name).exists():
            raise serializers.ValidationError("Category with this name already exists")
        category = Category.objects.create(**validated_data)
        return category


    def update(self, instance, validated_data):
        new_name = validated_data.get('name', instance.name)
        if Category.objects.filter(name=instance.name).exists():
            raise serializers.ValidationError("Category with this name already exists")
        instance.name = new_name
        instance.save()
        return instance




