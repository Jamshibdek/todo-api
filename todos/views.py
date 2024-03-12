from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Todo
from .serializers import TodoSerialazer
# Create your views here.


class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialazer
    
    
    
class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialazer