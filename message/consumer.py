from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from friends.models import Chat
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("connected...")
        self.group_name= self.scope['url_route']['kwargs']['groupkanam']
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        self.send({
            "type":"websocket.accept"
        })
    def websocket_disconnect(self,event):
        print("disconnected")
        raise StopConsumer
    def websocket_receive(self,event):
        print("message from client ...",event['text'])
        message=json.loads(event['text'])
        print(message['msg'])
        sender=self.scope['user'].username
        message['user']=sender

        chat = Chat(
            cotent = message['msg'],
            group = self.group_name
            )
        chat.save()
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
                'type':'chat.message',
                'message':json.dumps(message)
        })
    def chat_message(self,event):
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })