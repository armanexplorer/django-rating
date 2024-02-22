from django.urls import path
from .views import ContentListAPIView

app_name = 'todos'

urlpatterns = [
    path('', ContentListAPIView.as_view(), name="list"),
]