# from django.contrib.auth.models import User, Group
from taskmanager.models import Task
from rest_framework import serializers
# from django.contrib.auth.models import User


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         read_only_fields = ['id']
#         fields = read_only_fields + ['username', 'email']


# class StatusSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = TaskStatus
#         read_only_fields = ['id']
#         fields = read_only_fields + ['status']

class NonModelSerializer(serializers.Serializer):
    """Сериализатор с не-модельными полями."""


class TodoSerializer(serializers.ModelSerializer):
    """Сериализатор для модели TodoList."""
    is_active = serializers.SerializerMethodField('get_task_status')
    user = serializers.SerializerMethodField('get_task_username')


    class Meta:
        model = Task
        read_only_fields = ["id"]
        fields = read_only_fields + ["name", "created", "is_active", "complete_time", "user"]

    def to_internal_value(self, data):
        if self.context["request"]._request.method == "POST":
            if not data.get("name"):
                data["name"] = "default_task"
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
    
    def get_task_status(self, obj):
        return obj.is_active
    
    def get_task_username(self, obj):
        if obj.user:
            return obj.user.__str__()
        return obj.user