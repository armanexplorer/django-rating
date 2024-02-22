from rest_framework.generics import ListAPIView

from .serializers import ContentListSerializer
from .models import Content


class ContentListAPIView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()


# class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()
#     permission_classes = (IsAuthenticated, UserIsOwnerTodo)

