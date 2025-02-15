from .models import todoItem
from .serializers import todoItemSerializer
from rest_framework import generics

# Create your views here.

class ListTodoItem(generics.ListAPIView):
    queryset = todoItem.objects.all()
    serializer_class = todoItemSerializer