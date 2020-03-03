from rest_framework import generics

from rest_framework.permissions import IsAuthenticated


from manager.models import Task
from manager.serializer import TaskSerializer


class ListTask(generics.ListCreateAPIView):
   # permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


