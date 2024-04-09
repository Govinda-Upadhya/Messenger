from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from friends.models import Friendship
from friends.models import Chat
# Create your views here.
def messager(request,name):
    curr_user=request.user
    message_receiver=User.objects.get(username=name)
    print(message_receiver.username)
    groupname=Friendship.objects.get(user=curr_user,friend=message_receiver).groupname
    print(groupname)
    chats=Chat.objects.filter(group=groupname)
    print(chats)
    return render(request,'message.html',{
        'groupname':groupname,
        'chats':chats
    })
