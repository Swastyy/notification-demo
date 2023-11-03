# notification_app/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_notification(self, event):
        message = event['message']
        sound = event['sound']

        await self.send(text_data=json.dumps({
            'message': message,
            'sound': sound,
        }))
