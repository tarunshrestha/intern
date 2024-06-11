from channels.generic.websocket import AsyncJsonWebsocketConsumer

class PracticeConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        if text_data == 'PING':
            await self.send('PONG')


# async def chat_message(self, event):
#     """
#     Called when someone has messaged our chat.
#     """
#     # Send a message down to the client
#     await self.send_json(
#         {
#             "room": event["room_id"],
#             "username": event["username"],
#             "message": event["message"],
#         },
#     )