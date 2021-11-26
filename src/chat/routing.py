from django.urls import path

from chat import consumers

ws_urlpatterns = [
    path('ws/jokes/', consumers.JokesConsumer.as_asgi()),
]