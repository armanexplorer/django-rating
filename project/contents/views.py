from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ContentListSerializer, RatingCreateSerializer
from .models import Content, Rating


class ContentListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()


class RatingCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RatingCreateSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # TODO: the status of only update ratings should be changed to 200 instead of current 201
