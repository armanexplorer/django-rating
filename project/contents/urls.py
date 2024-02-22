from django.urls import path
from .views import ContentListAPIView, RatingCreateAPIView

app_name = 'contents'

urlpatterns = [
    path('', ContentListAPIView.as_view(), name="list"),
    path('Rate', RatingCreateAPIView.as_view(), name="rate")
]
