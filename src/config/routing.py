from django.urls import path, include

from admin import consumers as admin_consumers
from chat import consumers as chat_consumers

ws_urlpatterns = [
    path('ws/admin/fruits/', admin_consumers.FruitConsumer.as_asgi()),
    path('ws/admin/update-last-operations/', admin_consumers.LastOperationsConsumer.as_asgi()),
    path('ws/admin/check-storage/', admin_consumers.CheckStorageConsumer.as_asgi()),
    path('ws/jokes/', chat_consumers.JokesConsumer.as_asgi()),
    path('ws/update-chat/', chat_consumers.ChatConsumer.as_asgi()),
]