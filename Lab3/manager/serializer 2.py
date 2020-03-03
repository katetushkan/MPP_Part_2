from rest_framework import serializers

from manager.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'status',
            'deadline',
            'description',
            'file',
        )
        model = Task