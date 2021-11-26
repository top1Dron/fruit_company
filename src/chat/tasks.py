from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from django_celery_beat.models import IntervalSchedule, PeriodicTask, PeriodicTasks
import requests

from chat import utils as chat_utils
from chat.models import ChatMessage
from config.celery import app


channel_layer = get_channel_layer()


@shared_task
def get_joke():
    url = 'https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php'
    joke = requests.get(url).text
    message = ChatMessage.objects.create(text=joke, author=User.objects.get(email='shutnik@gmail.com'))
    async_to_sync(channel_layer.group_send)('jokes', {
        'type': 'send_jokes', 
        'text': message.text,
        'author': message.author.get_full_name(),
        'publication_date': message.publication_date.strftime("%d.%m.%Y, %H:%M")
    })
    PeriodicTask.objects.update_or_create(
        name='Get joke',      
        defaults={
            'name':'Get joke',
            'interval': IntervalSchedule.objects.get_or_create(
                every=chat_utils.get_length_of_last_joke(), 
                period=IntervalSchedule.SECONDS)[0], 
            'task':'chat.tasks.get_joke'}
    )


@shared_task
def update_chat():
    messages = chat_utils.get_last_chat_messages_for_chat_area()
    async_to_sync(channel_layer.group_send)('chat', {
        'type': 'update_chat', 
        'text': messages,
    })

get_joke_periodic_task = PeriodicTask.objects.update_or_create(
    name='Get joke',      
    defaults={
        'name':'Get joke',
        'interval': IntervalSchedule.objects.get_or_create(
            every=chat_utils.get_length_of_last_joke(), 
            period=IntervalSchedule.SECONDS)[0], 
        'task':'chat.tasks.get_joke'}
)

update_chat_periodic_task = PeriodicTask.objects.update_or_create(
    name='Update chat',
    defaults={
        'name': 'Update chat', 
        'task': 'chat.tasks.update_chat',
        'interval': IntervalSchedule.objects.get_or_create(
            every=3, 
            period=IntervalSchedule.SECONDS)[0]
    }
)