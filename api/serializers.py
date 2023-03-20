from rest_framework import serializers

from .models import taskTodo

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = taskTodo
        fields ='__all__'