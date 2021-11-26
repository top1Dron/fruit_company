import json

from channels.generic.websocket import AsyncWebsocketConsumer

from chat import utils


class JokesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('jokes', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code=''):
        await self.channel_layer.group_discard('jokes', self.channel_name)

    async def send_jokes(self, event):
        text_message = event['publication_date'] + ' ' + event['author'] + ': ' + event['text']
        await self.send(text_message)

    async def receive(self, text_data):
        message_data = json.loads(text_data)
        if self.scope['user'].is_authenticated:
            message_in_chat = await utils.create_message(message_data['message'], self.scope['user'])
            await self.send(message_in_chat)
        else:
            await self.send('Для отправки сообщений в чат нужно сначала авторизоваться!')


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('chat', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code=''):
        await self.channel_layer.group_discard('chat', self.channel_name)

    async def update_chat(self, event):
        text_message = event['text']
        await self.send(text_message)