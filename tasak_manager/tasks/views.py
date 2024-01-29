from rest_framework import generics
from tasks.models import ToDoItem
from tasks.serializers import ToDoSerializer
from rest_framework.response import Response
from rest_framework import status


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoSerializer
    
    
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoSerializer
    
class TodoListView(generics.ListAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoSerializer
    
class TodoUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoSerializer
    partial = True
    
    
class TodoDeleteView(generics.DestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Task"))

