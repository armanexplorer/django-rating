from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import ContentListSerializer, RatingCreateSerializer
from .models import Content, Rating


class ContentListAPIView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()


class RatingCreateAPIView(CreateAPIView):
    serializer_class = RatingCreateSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
