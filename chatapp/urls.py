from django.urls import path
from chatbot.views import ChatAPIView

urlpatterns = [
    path("api/chat/", ChatAPIView.as_view()),
]
