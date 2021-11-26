import json
from channels.generic.websocket import AsyncWebsocketConsumer

from admin.tasks import checking_storage


class FruitConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('fruits', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code=''):
        await self.channel_layer.group_discard('fruits', self.channel_name)

    async def update_apples(self, event):
        await self.send(text_data=json.dumps({
            'money': event['money'],
            'apples': event['apples'],
            'operation': event['operation']
        }))
    
    async def update_bananas(self, event):
        await self.send(text_data=json.dumps({
            'money': event['money'],
            'bananas': event['bananas'],
            'operation': event['operation']
        }))

    async def update_pineapples(self, event):
        await self.send(text_data=json.dumps({
            'money': event['money'],
            'pineapples': event['pineapples'],
            'operation': event['operation']
        }))

    async def update_peaches(self, event):
        await self.send(text_data=json.dumps({
            'money': event['money'],
            'peaches': event['peaches'],
            'operation': event['operation']
        }))


class LastOperationsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('last_operations', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code=''):
        await self.channel_layer.group_discard('last_operations', self.channel_name)

    async def update_last_operations(self, event):
        text_message = event['operations']
        await self.send(text_message)


class CheckStorageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('check_storage', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code=''):
        await self.channel_layer.group_discard('check_storage', self.channel_name)

    async def receive(self, text_data):
        if self.scope['user'].is_authenticated:
            result = checking_storage.apply_async()
            result.get()
            await self.send('Таска успешно выполнена')
        else:
            await self.send('Для выполнения этого действия вам нужно сначала авторизоваться!')