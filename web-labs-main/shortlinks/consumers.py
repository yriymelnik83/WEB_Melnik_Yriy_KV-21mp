import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.user = self.scope["user"]
        self.group_name = 'notification'
        if not self.user.is_anonymous:
            self.user.is_online = True
            await sync_to_async(self.user.save)()

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        #return await super().connect()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        if not self.user.is_anonymous:
            self.user.is_online = False
            await sync_to_async(self.user.save)()
        #return await super().disconnect(code)
    
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_name = text_data_json['userName']
        print(user_name)
        event = {
            'type': 'send_message',
            'message' : message,
            'userName' : user_name,
        }
        
        await self.channel_layer.group_send(self.group_name, event)
        #return await super().receive(text_data, bytes_data)
    
    async def send_message(self,event):

        message = event['message']
        user_name = event['userName']
        await self.send(text_data=json.dumps({'message' : message, 'userName' : user_name }))