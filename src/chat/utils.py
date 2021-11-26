from typing import Optional

from channels.db import database_sync_to_async
from django.contrib.auth.models import User

from chat.models import ChatMessage


def get_length_of_last_joke() -> int:
    try:
        message = ChatMessage.objects.filter(author__email='shutnik@gmail.com').first()
        return len(message.text)
    except:
        return 100


def get_user_by_username(username: str) -> Optional[User]:
    try:
        return User.objects.get(username=username)
    except:
        return None


def get_last_chat_messages_for_chat_area() -> str:
    result = ''
    messages = ChatMessage.objects.all().select_related('author')[:40]
    for message in messages[::-1]:
        result += (message.publication_date.strftime("%d.%m.%Y %H:%M") + 
            ' ' + message.author.first_name + ': ' + message.text + '\n')
    return result.removesuffix('\n')


@database_sync_to_async
def create_message(message: str, user: User) -> str:
    message = ChatMessage.objects.create(text=message, author=user)
    return (message.publication_date.strftime("%d.%m.%Y %H:%M") + 
        ' ' + message.author.first_name + ': ' + message.text)