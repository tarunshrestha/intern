import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message

class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"room_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json

        # Debug: Print received message
        print(f"Received message: {message}")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Debug: Print message before saving to DB
        # print(f"Message to save: {message}")

        await self.create_message(message)

        response_data = {
            'sender': message['sender'],
            'message': message['message']
        }

        # Debug: Print response data before sending to WebSocket
        # print(f"Sending response data: {response_data}")

        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': response_data}))

    @database_sync_to_async
    def create_message(self, data):
        try:
            room = Room.objects.get(room_name=data['room_name'])
            if not Message.objects.filter(message=data['message'], room=room).exists():
                Message.objects.create(room=room, sender=data['sender'], message=data['message'])
        except Room.DoesNotExist:
            # Handle the error if the room does not exist
            print(f"Room {data['room_name']} does not exist.")
        except Exception as e:
            # Log any other exceptions
            print(f"Error creating message: {e}")
