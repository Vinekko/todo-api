from rest_framework import serializers
from .models import todoItem

class todoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoItem
        fields = '__all__'