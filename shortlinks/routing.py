from django.urls import path, re_path
from . import consumers

websocket_urlpatterns = [
    path('ws', consumers.NotificationConsumer.as_asgi()),
]