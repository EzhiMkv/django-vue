from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from restapi.models import Task
from restapi.serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
